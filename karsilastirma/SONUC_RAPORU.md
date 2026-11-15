# SAÜ FBE Doktora Tez Şablonu — Word ↔ LaTeX Senkron Denetimi: Sonuç Raporu

## 1. Kaynaklar
- Word şablonu: enstitü sitesi "Doktora Tez Teslim Süreci" sayfasındaki `sau-lisansustu-tez-sablonu` →
  `word/SAU_FBE_Doktora_Tez_Sablonu.docx` (yüksek lisans sayfasındaki dosya ile bayt bayt aynı).
- Kılavuz: Lisansüstü Tez Yazım Kılavuzu (enstitü sitesi; Senato 04.08.2022, 621-9).
- Word PDF: Word'ün kendi dışa aktarımı (alanlar ve içindekiler güncellenerek) → `word/SAU_FBE_Doktora_Tez_Sablonu_Word_ciktisi.pdf`.
- LaTeX PDF: `sablon/tez.tex` (LuaLaTeX) → `karsilastirma/latex_ciktisi.pdf`; yan yana: `karsilastirma/yan_yana_word_latex.pdf`.

## 2. Yöntem
1. docx XML'den stiller, numaralandırma, bölüm (section) ayarları, alanlar ve OMML denklemler çıkarıldı;
   içerik bir dönüştürücüyle LaTeX'e birebir aktarıldı.
2. Biçim değerleri Word PDF'inden bp hassasiyetinde ölçüldü (taban çizgileri, girintiler, aralıklar).
3. Word'ün dizgi davranışı LuaLaTeX'te taklit edildi (`sauwordline.lua`):
   - açgözlü satır kırma ve boşlukların en fazla %22,7 sıkıştırılması (610 satırlık örnekte %99,3 uyum),
   - Word satır kutusu modeli (1,5 satır = 20,7 bp; ilk taban çizgisi +11,22 bp; ardışık paragraf aralıkları max(önce, sonra)),
   - sayfa altında yalnız alt çıkıntının (2,58 bp) kenar boşluğuna sayılması.
4. Alt ajanlarla denetim: 4 paralel denetim (sayfalama ve listeler, denklem ve içerik, tablo ve şekil,
   stil ve yerleşim) → düzeltme → doğrulama ajanı → düzeltme.
   (Ara ajan raporları bu depoya konmamıştır; son durum aşağıdadır.)

## 3. Son durum (sayfa sayfa ayrıntı: `karsilastirma.txt`, `araclar/compare_pdfs.py` çıktısı)
| Ölçüt | Sonuç |
|---|---|
| Sayfa sayısı | Word 77, LaTeX 77 |
| Sayfa eşlemesi | Birebir: Word s.N → LaTeX s.N (1–77); her sayfanın numarası (ya da numarasızlığı) aynı |
| Eşleşen metin satırı | 1228 satır; bunların 820'sinde dikey sapma ≤ 1 pt, 1170'inde yatay sapma ≤ 1 pt |
| Birebir sayfa | 30 sayfanın tüm satırları ≤ 1 pt (kapaklar, onay, beyanname, ithaf, teşekkür, özet, summary, 1. bölümün tamamı, kaynakça sayfaları dahil) + 15 boş sayfa çifti |
| Sayfa numarası | Dikey sayfalarda taban çizgisi farkı 0,00 pt (ön kısım y=764,3; 1. bölüm–ilk yatay sayfa arası y=743,6; sonrası y=791,0). Rakamların yatay konumu ≤ 0,1 pt (Word numaradan sonra bir boşluk bıraktığı için kutu merkezi 1,5 pt sağda görünür). Yatay sayfalarda Word gibi koyu olmayan, sol kenarda döndürülmüş numara |
| İçindekiler / listeler | Girdiler, sıra, girinti (113,4 / 124,7 / 137,5 / 149,4), noktalı satır aynı; her iki PDF'te sayfa numaraları kendi gerçek sayfalarıyla tutarlı |
| Satır sonları | 250 tam eşleşen paragrafın 229'unda birebir; kalan farklar Word'ün belgelenmemiş iç metriklerinden |
| Denklemler | (3.1)–(3.3): numara biçimi, dik harfler, öncesi/sonrası aralıklar Word ile aynı |
| Tablolar / şekiller | Boyut, çizgiler, satır yüksekliği (32,7 bp), başlık konumu ve aralıkları, asılı girinti Word ile aynı |

## 4. Sayfalama mantığı (ilk sayfada sayfa no var mı?)
| Sayfa | Word | LaTeX | Kılavuz 3.5 |
|---|---|---|---|
| Dış kapak (1. sayfa) ve arkası | numarasız | numarasız | numarasız ✓ |
| İç kapak (i) ve arkası (ii) | numarasız | numarasız | sayılır ama yazılmaz ✓ |
| Onay sayfası | iii | iii | iii ✓ |
| Ön kısım | iv … xxvii (Roma); son boş sayfa numarasız | iv … xxvii (Roma); son boş sayfa numarasız | Roma ✓ |
| Bölüm ilk sayfaları | 1., 3., 4. bölüm numarasız; 2., 5., 6. bölüm, Kaynaklar, Ekler, Özgeçmiş numaralı | 1.–6. bölümün hepsi numarasız (kullanıcı kararı); Kaynaklar, Ekler, Özgeçmiş numaralı | kural yok |
| Ana metin | 2, 3, … (Arap) | 2, 3, … (Arap) | Arap ✓ |

### 4.1 Word şablonunun kendi tutarsızlıkları (LaTeX bu noktalarda kılavuza uyar)
1. 1., 3. ve 4. bölümlerin ilk sayfasında (s.31, 46, 53) sayfa no yok ("farklı ilk sayfa" ayarı açık, ilk sayfa altbilgisi tanımsız); 2., 5., 6. bölümlerde ve Kaynaklar'da var. Ne şablonda ne kılavuzda bununla ilgili bir kural var. Kullanıcı kararıyla LaTeX'te 1.–6. bölümlerin hepsinin ilk sayfası numarasız (sayfa sayılır); bu yüzden s.35, 61 ve 63'te (2., 5., 6. bölüm başları) Word'de numara var, LaTeX'te yok.
2. Ön kısım sonundaki boş sayfa (s.30) numarasız; LaTeX'te de numarasız.
3. **3. bölüm çift sayfadan (16) başlıyor**: Word'de bölümler "sonraki sayfa" bölüm sonuyla başlar; boş sayfa yalnızca 5. bölüm, EKLER ve ÖZGEÇMİŞ öncesinde var. LaTeX (`wordbirebir`) aynısını yapar; bu yüzden sayfa sayısı ve numaralar Word ile aynıdır. (Kılavuz 3.2.1 bölümlerin sağ sayfadan başlamasını ister; `wordbirebir` kaldırılırsa LaTeX her bölümü sağ sayfadan başlatır.)
4. Sayfa no yüksekliği üç farklı değerde: ön kısım y≈764 (alttan 2,75 cm), s.32–38 y≈744, s.40+ y≈791 (alttan 1,8 cm). Kılavuz 1,5 cm diyor. Nedeni altbilgilerdeki boş paragraflar: s.32–38'deki altbilgide numaranın altında iki satırlık boş sekme paragrafı var, bu da numarayı yukarı itip metin alanını kısaltıyor. LaTeX `wordbirebir` seçeneğiyle üçünü de taklit ediyor; seçenek kaldırılırsa ana metinde tek hiza (y=791) kullanılır.
5. İçindekiler'de "ÖZET" ve "EKLER" satırlarında noktalı sekme bozuk; "ŞEKİL VE Tablolar" ve "GEREKLİ İSE bölüm başlığı" büyük harf kuralına aykırı. "Table 2.4." yazım hatası. KISALTMALAR, 5. bölüm ve ÖZGEÇMİŞ başlıkları diğerlerinden farklı yükseklikte.
6. Word'de denklemler metin bloğunun 27–32 pt solunda, numaralar sağ kenarın dışında; LaTeX kılavuza göre ortalıyor.
7. Yatay sayfalarda Word'deki görünen numara elle konmuş dikey bir metin kutusu (kalın değil, konumu sayfadan sayfaya değişiyor); altbilgideki asıl numara beyaz kutuyla örtülü. LaTeX (`wordbirebir`) numarayı Word s.44'teki konuma, koyu olmayan yazıyla koyar.

### 4.2 Bilinçli farklar
- Dış kapaktaki not kutusu metni LaTeX'e uyarlandı ("`\documentclass[notsuz]{sauthesis}` seçilmeli"); `notsuz` seçeneği tüm kırmızı/mavi notları kaldırır.
- Dipnot satır aralığı: Word 1,5, kılavuz tek → LaTeX tek satır.
- 3.3.1.1 başlığı (s.49): Word'de başlıktan önce fazladan boş bir paragraf var, bu yüzden üst boşluk 59,4 pt (diğer 4. derece başlıklarda 32,7 pt). Kılavuz 3.4'e göre ("başlıklardan önce 12 nk"; "paragrafların arasında boş satır bulunmamalıdır") LaTeX'te 32,7 pt (kullanıcı kararı: kural geçerli).

## 5. Kalan küçük farklar
- Çift sayfaya düşen yatay sayfada (s.44) üst kenar 2,5 cm; Word her yatay sayfada 4 cm kullanıyor.
- 11 paragrafta tek kelimelik satır sonu farkı (Word'ün sıkıştırma eşiği sabit değil).
- "lim" Word'de Cambria Math, LaTeX'te Times New Roman ile basılıyor.

## 6. Kullanım
```
cd sablon
latexmk -lualatex tez.tex
```
Ayrıntılar: depo kökündeki `README.md`.
