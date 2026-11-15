"""Word PDF ile LaTeX PDF'ini sayfa sayfa karsilastirir.
Kullanim: python compare_pdfs.py word.pdf latex.pdf [rapor.txt]
Her sayfa icin: sayfa numarasi (altbilgi), satir sayisi, ilk/son satir, metin farki,
eslesen satirlarin dikey (dy) ve yatay (dx) sapmalari.
"""
import sys, re, difflib
import pymupdf


def norm(s):
    s = s.replace(' ', ' ').replace('…', '...').replace('’', "'").replace('“', '"').replace('”', '"')
    s = re.sub(r'\s+', ' ', s).strip()
    return s


def page_lines(p):
    W, H = p.rect.width, p.rect.height
    out = []
    for b in p.get_text('dict')['blocks']:
        if b['type'] != 0:
            continue
        for l in b['lines']:
            t = norm(''.join(s['text'] for s in l['spans']))
            if not t:
                continue
            x0, y0, x1, y1 = l['bbox']
            y1 = [sp for sp in l['spans'] if sp['text'].strip()][0]['origin'][1]  # taban cizgisi
            sz = max(s['size'] for s in l['spans'])
            bold = any('Bold' in s['font'] or (s['flags'] & 16) for s in l['spans'] if s['text'].strip())
            out.append({'t': t, 'x0': x0, 'y0': y0, 'x1': x1, 'y1': y1, 'sz': sz, 'b': bold,
                        'dir': l.get('dir', (1, 0))})
    # merge fragments on the same baseline (Word splits justified words)
    out.sort(key=lambda r: (round(r['y1']), r['x0']))
    merged = []
    for r in out:
        if merged and abs(merged[-1]['y1'] - r['y1']) < 2.0 and r['dir'] == merged[-1]['dir']:
            m = merged[-1]
            m['t'] = m['t'] + ' ' + r['t']; m['x1'] = max(m['x1'], r['x1']); m['x0'] = min(m['x0'], r['x0'])
            m['b'] = m['b'] or r['b']
        else:
            merged.append(dict(r))
    return merged


def footer_number(lines, H):
    cands = [l for l in lines if l['y0'] > H * 0.86 and re.fullmatch(r'[ivxlcdm]+|\d+', l['t'])]
    return cands[-1] if cands else None


def main():
    a, b = pymupdf.open(sys.argv[1]), pymupdf.open(sys.argv[2])
    out = open(sys.argv[3], 'w', encoding='utf-8') if len(sys.argv) > 3 else sys.stdout
    out.write('WORD sayfa=%d  LATEX sayfa=%d\n' % (a.page_count, b.page_count))
    # Sayfa eslemesi: icerik benzerligine gore monoton eslesme (LaTeX'te bos/ek sayfa olabilir)
    ta_all = [' '.join(l['t'] for l in page_lines(p)) for p in a]
    tb_all = [' '.join(l['t'] for l in page_lines(p)) for p in b]
    # dinamik programlama (Needleman-Wunsch): benzerlik toplami max, atlama cezasi 0.35
    na, nb = a.page_count, b.page_count

    def sim(i, k):
        x, y = ta_all[i], tb_all[k]
        if not x.strip() and not y.strip():
            return 0.9
        if not x.strip() or not y.strip():
            return 0.0
        wa, wb = x.split(), y.split()
        return difflib.SequenceMatcher(None, wa[:120], wb[:120], autojunk=False).ratio()
    S = [[sim(i, k) if abs(i - k) <= 6 else 0.0 for k in range(nb)] for i in range(na)]
    G = 0.35
    D = [[0.0] * (nb + 1) for _ in range(na + 1)]
    B = [[None] * (nb + 1) for _ in range(na + 1)]
    for i in range(1, na + 1):
        D[i][0] = -G * i; B[i][0] = 'u'
    for k in range(1, nb + 1):
        D[0][k] = -G * k; B[0][k] = 'l'
    for i in range(1, na + 1):
        for k in range(1, nb + 1):
            c = [(D[i - 1][k - 1] + S[i - 1][k - 1], 'd'), (D[i - 1][k] - G, 'u'), (D[i][k - 1] - G, 'l')]
            D[i][k], B[i][k] = max(c)
    pairs = []
    i, k = na, nb
    while i > 0 or k > 0:
        m = B[i][k]
        if m == 'd':
            pairs.append((i - 1, k - 1)); i -= 1; k -= 1
        elif m == 'u':
            pairs.append((i - 1, None)); i -= 1
        else:
            k -= 1
    pairs.reverse()
    out.write('SAYFA ESLEMESI (Word->LaTeX): ' + ' '.join('%d->%s' % (i + 1, (k + 1) if k is not None else '-') for i, k in pairs) + '\n')
    tot_dy = []
    for i, k in pairs:
        pa = a[i]
        pb = b[k] if k is not None else None
        la = page_lines(pa) if pa else []
        lb = page_lines(pb) if pb else []
        fa = footer_number(la, pa.rect.height) if pa else None
        fb = footer_number(lb, pb.rect.height) if pb else None
        la_body = [l for l in la if l is not fa]
        lb_body = [l for l in lb if l is not fb]
        ori_a = ('L' if pa and pa.rect.width > pa.rect.height else 'P') if pa else '-'
        ori_b = ('L' if pb and (pb.rect.width > pb.rect.height or pb.rotation in (90, 270)) else 'P') if pb else '-'
        out.write('\n=== Sayfa %d->%s  [%s|%s]  no: W=%s(y=%.1f,x=%.1f)  L=%s(y=%.1f,x=%.1f)  satir W=%d L=%d\n' % (
            i + 1, (k + 1) if k is not None else '-', ori_a, ori_b, fa['t'] if fa else '-', fa['y1'] if fa else 0, (fa['x0'] + fa['x1']) / 2 if fa else 0,
            fb['t'] if fb else '-', fb['y1'] if fb else 0, (fb['x0'] + fb['x1']) / 2 if fb else 0,
            len(la_body), len(lb_body)))
        ta = [l['t'] for l in la_body]
        tb = [l['t'] for l in lb_body]
        if ta:
            out.write('  W ilk: %s\n  W son: %s\n' % (ta[0][:90], ta[-1][:90]))
        if tb:
            out.write('  L ilk: %s\n  L son: %s\n' % (tb[0][:90], tb[-1][:90]))
        sm = difflib.SequenceMatcher(None, ta, tb, autojunk=False)
        dys = []
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == 'equal':
                for k in range(i2 - i1):
                    x, y = la_body[i1 + k], lb_body[j1 + k]
                    dys.append((y['y1'] - x['y1'], y['x0'] - x['x0'], x['t'][:50]))
            else:
                for k in range(i1, i2):
                    out.write('  - W[%5.1f,%5.1f] %s\n' % (la_body[k]['x0'], la_body[k]['y1'], ta[k][:110]))
                for k in range(j1, j2):
                    out.write('  + L[%5.1f,%5.1f] %s\n' % (lb_body[k]['x0'], lb_body[k]['y1'], tb[k][:110]))
        if dys:
            big = [d for d in dys if abs(d[0]) > 1.0 or abs(d[1]) > 1.0]
            out.write('  eslesen=%d  dy[min,max]=[%.1f,%.1f]  dx[min,max]=[%.1f,%.1f]  sapma>1pt=%d\n' % (
                len(dys), min(d[0] for d in dys), max(d[0] for d in dys), min(d[1] for d in dys), max(d[1] for d in dys), len(big)))
            for d in big[:6]:
                out.write('     dy=%+.1f dx=%+.1f  %s\n' % d)
            tot_dy += dys
    if tot_dy:
        out.write('\nTOPLAM eslesen satir=%d, |dy|<=1pt: %d, |dx|<=1pt: %d\n' % (
            len(tot_dy), sum(1 for d in tot_dy if abs(d[0]) <= 1), sum(1 for d in tot_dy if abs(d[1]) <= 1)))


main()
