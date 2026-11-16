r"""Kullanim kilavuzu gorsellerini uretir: sablon PDF sayfalarini numarali isaretlerle PNG'ye cevirir.

Kullanim:  python gorsel_uret.py SABLON.pdf ORNEK.pdf CIKTI_KLASORU
  SABLON.pdf : sablonun degistirilmemis ciktisi (tez.tex, notlar acik)
  ORNEK.pdf  : bilgileri doldurulmus, notsuz ornek cikti
"""
import sys
import os
import pymupdf as fz

RED = (0.84, 0.16, 0.16)
ZOOM = 1.6

# Parca: ('metin', k)  -> k. eslesme (None: hepsinin birlesimi)
#        ('rect', x0, y0, x1, y1) -> sabit dikdortgen (pt, sol ust koseden)
#        ('img', k)    -> sayfadaki k. gorselin cercevesi
# Grup : parcalarin birlesimi -> bir dikdortgen. Isaret: (numara, [grup, grup...], rozet yeri)
# Rozet yeri: 'l' kutunun solu, 'r' kutunun sagi, 'L' metin blogunun sol kenar boslugu, 'R' sag kenar boslugu
SAYFALAR = {
    'dis_kapak': ('s', 0, None, [
        (1, [[('TEZ BAŞLIĞI BURAYA YAZILIR', 0), ('GEREKLİ İSE İKİNCİ VE ÜÇÜNCÜ SATIR KULLANILABİLİR', 0),
              ('ÜÇ SATIRA SIĞDIRINIZ', 0)]], 'l'),
        (2, [[('YÜKSEK LİSANS/DOKTORA TEZİ', 0)]], 'l'),
        (3, [[('Öğrenci Adı SOYADI', 0)]], 'l'),
        (4, [[('Bir öğe seçin.', 0), ('Anabilim Dalı', 0)]], 'r'),
        (5, [[('Bir öğe seçin.', 1), ('Bilim Dalı', 0), ('(Varsa)', 0)]], 'r'),
        (6, [[('AY YIL', 0), ('(OCAK 2022)', 0)]], 'l'),
        (7, [[('rect', 129.8, 476.7, 491.4, 574.4)]], 'l'),
    ]),
    'dis_kapak_ornek': ('o', 0, None, []),
    'ic_kapak': ('s', 2, None, [
        (1, [[('Öğrenci Numarası (Örnek: D205001001)', 0)]], 'l'),
        (2, [[('Tez Danışmanı: Unvan Ad SOYAD', 0)]], 'l'),
        (3, [[('(Varsa) Ortak Danışman: Unvan Ad SOYAD', 0)]], 'l'),
    ]),
    'ic_kapak_ornek': ('o', 2, None, []),
    'onay': ('s', 4, (0, 50, 595.28, 700), [
        (1, [[("rect", 111, 139, 541, 207)]], "L"),
        (2, [[('rect', 111, 340, 541, 370)]], 'L'),
        (3, [[('rect', 111, 397, 541, 427)]], 'L'),
        (4, [[('rect', 111, 453, 541, 483)]], 'L'),
        (5, [[('rect', 111, 510, 541, 540)]], 'L'),
        (6, [[('rect', 111, 567, 541, 597)]], 'L'),
        (7, [[('rect', 111, 624, 541, 654)]], 'L'),
    ]),
    'onay_ornek': ('o', 4, (0, 50, 595.28, 700), []),
    'beyanname': ('s', 6, (0, 50, 595.28, 560), [
        (1, [[('“TEZ BAŞLIĞI YAZILACAK”', 0)]], 'R'),
        (2, [[('etik kurul', 0)], [('onay belgesi', 0), ('metinden çıkartılır)', 0)]], 'R'),
        (3, [[('(……/……/20…..).', 0)]], 'l'),
        (4, [[('Öğrencinin Adı Soyadı', 0)]], 'l'),
    ]),
    'tesekkur': ('s', 10, (0, 50, 595.28, 420), [
        (1, [[('Teşekkür bölümünün', 0), ('kişilere bu kısımda', 0), ('ve soyadı yazılır.', 0)]], 'L'),
        (2, [[('Ad Soyad', 0)]], 'l'),
    ]),
    'kisaltmalar': ('s', 14, (0, 50, 595.28, 330), [
        (1, [[('AIC', 0), ('Akaike Information Criteria', 0)]], 'L'),
    ]),
    'ozet': ('s', 22, (0, 50, 595.28, 330), [
        (1, [[('TÜRKÇE TEZ BAŞLIĞI BURAYA YAZILIR', 0)]], 'l'),
        (2, [[('ÖZET', 0)]], 'l'),
    ]),
    'baslik_1': ('s', 30, (0, 50, 595.28, 560), [
        (1, [[('1. GİRİŞ (BİRİNCİ DERECE BAŞLIK)', 0)]], 'L'),
        (2, [[('1.1.', 0), ('İlk Harfler Büyük)', 0)]], 'L'),
    ]),
    'baslik_2': ('s', 31, (0, 50, 595.28, 600), [
        (1, [[('1.2.1. Tezin ikincil amacı', 0)]], 'L'),
        (2, [[('1.2.1.1.', 0), ('diğerleri küçük', 0)]], 'L'),
        (3, [[('Beşinci derece başlık nasıl: ilk harf büyük diğerleri küçük', 0)]], 'L'),
    ]),
    'sekil_tablo': ('s', 63, (0, 50, 595.28, 520), [
        (1, [[('img', 0)]], 'l'),
        (2, [[('Şekil 5.1. Beşinci bölümde örnek şekil.', 0)]], 'l'),
        (3, [[('Tablo 5.1. Beşinci bölümde örnek tablo.', 0)]], 'l'),
    ]),
    'devami': ('s', 42, (0, 50, 595.28, 260), [
        (1, [[('Tablo 2.3. (Devamı):', 0)]], 'l'),
    ]),
    'yatay': ('s', 38, None, []),
    'denklem': ('s', 48, (0, 50, 595.28, 330), [
        (1, [[('(3.1)', 0)]], 'r'),
        (2, [[('(3.2)', 0)]], 'r'),
    ]),
    'dipnot': ('s', 58, (0, 250, 595.28, 841.89), [
        (1, [[('kullanılabilir', 0)], [('rect', 111, 722, 541, 773)]], 'L'),
    ]),
    'kaynaklar': ('s', 68, (0, 50, 595.28, 330), []),
    'ekler': ('s', 74, (0, 50, 595.28, 260), [
        (1, [[('EKLER', 0)]], 'L'),
        (2, [[('EK A. Haritalar', 0), ('EK B. Tablolar', 0)]], 'L'),
    ]),
    'ek_a': ('s', 75, (0, 50, 595.28, 360), [
        (1, [[('EK A. Haritalar', 0)]], 'L'),
        (2, [[('Şekil A.1.', 0)]], 'l'),
    ]),
    'ozgecmis': ('s', 78, (0, 50, 595.28, 520), []),
}


def bul(page, parca):
    if parca[0] == 'rect':
        return fz.Rect(*parca[1:])
    if parca[0] == 'img':
        xref = page.get_images()[parca[1]][0]
        return fz.Rect(page.get_image_rects(xref)[0])
    metin, k = parca
    rs = page.search_for(metin)
    if not rs:
        raise SystemExit(f'bulunamadi: s.{page.number + 1} {metin!r}')
    if k is None:
        r = fz.Rect(rs[0])
        for x in rs[1:]:
            r |= x
        return r
    return fz.Rect(rs[k])


def rozet(page, x, y, n):
    page.draw_circle((x, y), 8.5, color=RED, fill=RED, width=0)
    s = str(n)
    w = fz.get_text_length(s, fontname='hebo', fontsize=10)
    page.insert_text((x - w / 2, y + 3.6), s, fontname='hebo', fontsize=10, color=(1, 1, 1))


def main(sablon, ornek, cikti):
    os.makedirs(cikti, exist_ok=True)
    for ad, (kaynak, no, kirp, isaretler) in SAYFALAR.items():
        doc = fz.open(sablon if kaynak == 's' else ornek)
        page = doc[no]
        if page.rotation:
            page.remove_rotation()
        # tek numarali sayfada metin blogu 113.4-538.6 pt, cift numaralida 70.9-496.1 pt
        sol, sag = (113.4, 538.6) if no % 2 == 0 else (70.9, 496.1)
        for n, gruplar, yer in isaretler:
            kutular = []
            for g in gruplar:
                r = bul(page, g[0])
                for pc in g[1:]:
                    r |= bul(page, pc)
                if g[0][0] != 'rect':
                    r = fz.Rect(r.x0 - 3, r.y0 - 2, r.x1 + 3, r.y1 + 2)
                page.draw_rect(r, color=RED, fill=RED, fill_opacity=0.06, width=1.3)
                kutular.append(r)
            r = kutular[0]
            y = (r.y0 + r.y1) / 2
            x = {'l': r.x0 - 12, 'r': r.x1 + 12, 'L': sol - 16, 'R': sag + 16}[yer]
            rozet(page, x, y, n)
        clip = fz.Rect(*kirp) if kirp else None
        pix = page.get_pixmap(matrix=fz.Matrix(ZOOM, ZOOM), clip=clip)
        pix.save(os.path.join(cikti, ad + '.png'))
        print(ad, pix.width, 'x', pix.height)


if __name__ == '__main__':
    main(*sys.argv[1:4])
