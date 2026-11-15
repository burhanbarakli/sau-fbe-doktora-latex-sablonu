"""Word (FBE sablonu) PDF'i ile LaTeX PDF'ini yan yana tek PDF'te birlestirir.
Kullanim: python yan_yana.py word_cikti.pdf latex_cikti.pdf yan_yana.pdf
Sayfalar icerik benzerligine gore eslenir (compare_pdfs.py ile ayni DP);
karsiligi olmayan sayfanin yanina bos bir yer tutucu konur.
"""
import sys, re, difflib
import pymupdf

GAP, TOP, MARGIN = 24, 30, 12


def text(p):
    return re.sub(r'\s+', ' ', p.get_text()).strip()


def align(a, b):
    ta, tb = [text(p) for p in a], [text(p) for p in b]
    na, nb = len(ta), len(tb)

    def sim(i, k):
        x, y = ta[i], tb[k]
        if not x and not y:
            return 0.9
        if not x or not y:
            return 0.0
        return difflib.SequenceMatcher(None, x.split()[:120], y.split()[:120], autojunk=False).ratio()
    G = 0.35
    D = [[0.0] * (nb + 1) for _ in range(na + 1)]
    B = [[None] * (nb + 1) for _ in range(na + 1)]
    for i in range(1, na + 1):
        D[i][0], B[i][0] = -G * i, 'u'
    for k in range(1, nb + 1):
        D[0][k], B[0][k] = -G * k, 'l'
    for i in range(1, na + 1):
        for k in range(1, nb + 1):
            s = sim(i - 1, k - 1) if abs(i - k) <= 6 else 0.0
            D[i][k], B[i][k] = max((D[i - 1][k - 1] + s, 'd'), (D[i - 1][k] - G, 'u'), (D[i][k - 1] - G, 'l'))
    pairs, i, k = [], na, nb
    while i > 0 or k > 0:
        m = B[i][k]
        if m == 'd':
            pairs.append((i - 1, k - 1)); i -= 1; k -= 1
        elif m == 'u':
            pairs.append((i - 1, None)); i -= 1
        else:
            pairs.append((None, k - 1)); k -= 1
    return pairs[::-1]


def main():
    a, b = pymupdf.open(sys.argv[1]), pymupdf.open(sys.argv[2])
    for d in (a, b):  # /Rotate'u icerige isle (show_pdf_page dondurulmus sayfada kirpar)
        for p in d:
            if p.rotation:
                p.remove_rotation()
    out = pymupdf.open()
    font = pymupdf.Font('helv')
    for i, k in align(a, b):
        ra = a[i].rect if i is not None else None
        rb = b[k].rect if k is not None else None
        wa = ra.width if ra else rb.width
        ha = ra.height if ra else rb.height
        wb = rb.width if rb else wa
        hb = rb.height if rb else ha
        W = MARGIN + wa + GAP + wb + MARGIN
        H = TOP + max(ha, hb) + MARGIN
        pg = out.new_page(width=W, height=H)
        pg.draw_rect(pg.rect, color=None, fill=(0.88, 0.88, 0.88))
        boxA = pymupdf.Rect(MARGIN, TOP, MARGIN + wa, TOP + ha)
        boxB = pymupdf.Rect(MARGIN + wa + GAP, TOP, MARGIN + wa + GAP + wb, TOP + hb)
        for box, doc, idx, name in ((boxA, a, i, 'WORD (FBE sablonu)'), (boxB, b, k, 'LaTeX')):
            pg.draw_rect(box, color=(0.6, 0.6, 0.6), fill=(1, 1, 1), width=0.5)
            if idx is not None:
                pg.show_pdf_page(box, doc, idx)
                label = '%s  -  PDF sayfa %d' % (name, idx + 1)
            else:
                label = '%s  -  karsiligi yok' % name
                pg.insert_textbox(box, '(bu tarafta karsilik gelen sayfa yok)', fontsize=14,
                                  color=(0.5, 0.5, 0.5), align=1)
            pg.insert_text((box.x0, TOP - 10), label, fontsize=11, fontname='helv',
                           color=(0.75, 0, 0) if idx is None else (0.1, 0.1, 0.1))
    out.save(sys.argv[3], garbage=3, deflate=True)
    print('olusturuldu:', sys.argv[3], out.page_count, 'sayfa')


main()
