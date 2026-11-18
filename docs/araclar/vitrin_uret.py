r"""README'deki vitrin gorselini (docs/img/vitrin.png) ornek tezden uretir.

Kullanim:  python vitrin_uret.py ORNEK.pdf CIKTI.png
  ORNEK.pdf : bilgileri doldurulmus, notsuz ornek cikti (docs/ornek_tez.pdf)
Sayfalar metinle bulunur; sablonun sayfa sayisi degisse de betik degismez.
"""
import sys
import pymupdf as fz
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ARKA = (243, 241, 238)
YAZI = (80, 80, 85)
SAYFA_G, SAYFA_Y, ARA, KENAR, UST = 328, 464, 32, 41, 41
G, Y = KENAR * 2 + 6 * SAYFA_G + 5 * ARA, 600


def bul(doc, metin, baslangic=0, olmasin=None):
    for i in range(baslangic, len(doc)):
        t = doc[i].get_text()
        if metin in t and not (olmasin and olmasin in t):
            return i
    raise SystemExit(f'sayfa bulunamadi: {metin!r}')


def main(ornek, cikti):
    doc = fz.open(ornek)
    icindekiler = bul(doc, 'İÇİNDEKİLER')
    sayfalar = [
        (0, 'Dış kapak'),
        (bul(doc, 'Tez Jürisi'), 'Onay sayfası'),
        (icindekiler, 'İçindekiler'),
        (bul(doc, '1. GİRİŞ', icindekiler + 1, olmasin='İÇİNDEKİLER'), 'Bölüm başlangıcı'),
        (bul(doc, '2.2. Yatay Sayfada Şekil Örneği', icindekiler + 1, olmasin='LİSTESİ'), 'Şekiller'),
        (bul(doc, '3.3. Denklemler', icindekiler + 1, olmasin='LİSTESİ'), 'Denklemler'),
    ]
    tuval = Image.new('RGB', (G, Y), ARKA)
    try:
        font = ImageFont.truetype('segoeui.ttf', 24)
    except OSError:
        font = ImageFont.load_default()
    for k, (no, etiket) in enumerate(sayfalar):
        x = KENAR + k * (SAYFA_G + ARA)
        pix = doc[no].get_pixmap(dpi=200)
        img = Image.frombytes('RGB', (pix.width, pix.height), pix.samples).resize((SAYFA_G, SAYFA_Y), Image.LANCZOS)
        golge = Image.new('L', (SAYFA_G + 40, SAYFA_Y + 40), 0)
        ImageDraw.Draw(golge).rectangle((20, 22, SAYFA_G + 20, SAYFA_Y + 22), fill=70)
        golge = golge.filter(ImageFilter.GaussianBlur(6))
        tuval.paste(Image.new('RGB', golge.size, (180, 175, 170)), (x - 20, UST - 20), golge)
        tuval.paste(img, (x, UST))
        d = ImageDraw.Draw(tuval)
        w = d.textlength(etiket, font=font)
        d.text((x + (SAYFA_G - w) / 2, 520), etiket, font=font, fill=YAZI)
    tuval.save(cikti, optimize=True)
    print(f'{cikti}: sayfalar {[s[0] + 1 for s in sayfalar]}')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(*sys.argv[1:])
