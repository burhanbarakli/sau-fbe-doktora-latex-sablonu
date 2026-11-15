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
   → kılavuz uyum denetimi → düzeltme. (Ara ajan raporları bu depoya konmamıştır; son durum aşağıdadır.)

## 3. İlke

**Kılavuz esastır.** Kılavuzun açıkça hükme bağladığı her konuda LaTeX kılavuza uyar; kılavuzun
belirlemediği konularda Word şablonu izlenir. Word şablonunun kılavuza aykırı olduğu yerlerde
LaTeX çıktısı bilerek Word'den ayrılır (aşağıda 5).

## 4. Son durum (ayrıntı: `karsilastirma.txt`)
| Ölçüt | Sonuç |
|---|---|
| Sayfa sayısı | Word 77, LaTeX 79 (fark: kılavuz 3.2.1 gereği bölümlerin sağ sayfadan başlaması için 2 boş sayfa) |
| Sayfa eşlemesi | Word s.1–45 → LaTeX s.1–45; s.46–52 → +1; s.53–77 → +2 |
| Eşleşen metin satırı | 1183 satır; 570'inde dikey sapma ≤ 1 pt, 989'unda yatay sapma ≤ 1 pt. Ön kısımda ve 1. bölümde metin alanı kılavuza göre (alt kenar 2,5 cm) Word'den uzun olduğu için satırlar bu sayfalarda kayar. |
| Birebir sayfa | 16 sayfanın tüm satırları ≤ 1 pt + 15 boş sayfa çifti |
| Sayfa numarası | Her sayfada alttan 1,5 cm (taban çizgisi y=799,4 bp), alt-orta, Times New Roman 12 pt koyu. Yatay sayfalarda okuma yönündeki alt kenarın (uzun kenar) ortasında, alttan 1,5 cm, koyu. |
| Kenar boşlukları | Her dikey sayfada üst 2,5 / alt 2,5 / iç (cilt) 4 / dış 2,5 cm (ön kısım dahil) |
| İçindekiler / listeler | İçindekiler Teşekkür ile başlar; Tablo ve Şekil listelerinde girişler arasında önce 6 / sonra 6 nk; tek satır aralığı; noktalı doldurma |
| Denklemler | (3.1)–(3.3): numara biçimi, dik harfler, öncesi/sonrası 6 nk, metin bloğuna ortalı |
| Tablolar / şekiller | Başlık konumu ve aralıkları kılavuza göre; uzun başlıkta 2. satır, numaradan sonraki metinle aynı hizada (≤ 0,6 pt); "Tablo 1.1. (Devamı): …" |

## 5. Sayfalama
| Sayfa | Word | LaTeX | Kılavuz 3.5 |
|---|---|---|---|
| Dış kapak ve arkası | numarasız | numarasız | numarasız ✓ |
| İç kapak (i) ve arkası (ii) | numarasız | numarasız | sayılır ama yazılmaz ✓ |
| Onay sayfası | iii | iii | iii ✓ |
| Ön kısım | iv … xxvii; son boş sayfa numarasız | iv … xxviii; son boş sayfa da numaralı | aralıksız Romen ✓ |
| Bölüm ilk sayfaları | 1., 3., 4. bölüm numarasız; 2., 5., 6. bölüm numaralı | 1.–6. bölüm numarasız (kullanıcı kararı); Kaynaklar, Ekler, Özgeçmiş numaralı | açık hüküm yok; numarasız bırakılacak sayfa olarak yalnız kapaklar ve i–ii sayılmış (bkz. 7) |
| Ana metin | Arap rakamı | Arap rakamı | Arap ✓ |

## 6. Word şablonunun kılavuza aykırı noktaları (LaTeX'te kılavuz uygulandı)
1. Sayfa numarası üç farklı yükseklikte: ön kısım alttan ≈2,74 cm, ana metin s.2–8 ≈3,47 cm, sonrası ≈1,80 cm (kılavuz: 1,5 cm). Nedeni altbilgilerdeki boş paragraflar; s.2–8 ve ön kısımda metin alanı da kısalıyor.
2. Yatay sayfalarda görünen numara elle konmuş, koyu olmayan dikey metin kutusu ve kısa kenarda; altbilgideki asıl numara beyaz kutuyla örtülü (kılavuz: okuma yönünde alt-orta, koyu).
3. 3. bölüm çift sayfadan başlıyor; bölümler "sonraki sayfa" bölüm sonuyla başlıyor (kılavuz 3.2.1: sağ sayfadan).
4. Ön kısmın sonundaki boş sayfa numarasız (kılavuz: aralıksız numaralandırma).
5. Dış kapak yazıları yazı bloğuna göre ortalı (kılavuz 3.8.1.1: kapağın dış kenarına göre). İç kapakta tez başlığı 14 pt (kılavuz: 12 pt) ve öğrenci numarası satırı yok.
6. Onay sayfasında 16 cm'deki "Ortak Danışman" yuvası yok, 18 cm'deki zorunlu jüri üyesi "Gerekliyse" diye işaretli, 22 cm yuvası yok.
7. Etik beyanname İçindekiler'de (kılavuz 4.4: İçindekiler Teşekkür ile başlar).
8. Tablo ve Şekil listelerinde girişler arasında 6 nk aralık yok (kılavuz 4.5).
9. Ek başlığı yalnız "EK A" (kılavuz 4.10: "Ek A. Ekin adı"); EKLER ve ÖZGEÇMİŞ 1,5 satır aralıklı (kılavuz 3.4: 1 satır).
10. Kaynaklar ve özgeçmişte girişler arasında boş paragraflar var (kılavuz 3.4: paragraflar arasında boş satır bulunmamalı).
11. Özgeçmişte "TEZDEN TÜRETİLEN ESERLER" yazıyor (kılavuz 4.11: "TEZDEN TÜRETİLEN YAYINLAR/SUNUMLAR").
12. "(Devamı)" sonrasında iki nokta yok (kılavuz 3.6: "Tablo 1.1. (Devamı): …"); uzun başlıkta 2. satır girintisi sabit, numaradan sonraki metinle aynı hizada değil.
13. Dipnotlar 1,5 satır aralıklı (kılavuz 3.4: 1 satır).
14. 3.3.1.1 başlığından önce fazladan boş paragraf (üst boşluk 59,4 pt; diğer 4. derece başlıklarda 32,7 pt).
15. Denklemler metin bloğuna göre ortalı değil, numaralar sağ kenarın dışına taşıyor.
16. Diğer: İçindekiler'de "ÖZET" ve "EKLER" satırlarında noktalı sekme bozuk; "Table 2.4." yazım hatası; "ŞEKİL VE Tablolar" ve "GEREKLİ İSE bölüm başlığı" büyük harf kuralına aykırı.

## 7. Açık kalan konular (kılavuzun iki türlü okunabildiği yerler)
- **Bölüm ilk sayfası numarası:** Kılavuz numarasız bırakılacak sayfa olarak yalnız dış kapak ve arkasını, iç kapak (i) ve arkasını (ii) sayar; kılavuzun kendi PDF'inde birinci derece başlıklı sayfada numara vardır. Kullanıcı kararıyla LaTeX'te 1.–6. bölümlerin ilk sayfası numarasızdır.
- **Ek denklemleri:** Kılavuz 3.7 "A.1.1", 4.10 "(A 1.1)" örneği verir; LaTeX şu an (A.1) basar (şablonda ekte denklem yok).
- **Aralıkların birleşmesi:** "Önce 6 / sonra 6 nk" ardışık paragraflarda birleşik (6 nk) uygulanır (Word davranışı); toplanarak 12 nk okunabilir.
- **Kapak ve onay sayfası konumları:** "Üst kenardan 15 cm" vb. satırın üst kenarına göre uygulanmıştır (taban çizgisi ≈ 0,4 cm aşağıda).
- **"(Devamı)" koyu mu, denklem yazı tipi (Cambria Math / Times New Roman), uzun alıntı satır aralığı:** kılavuzda açık değil; Word izlenir.

## 8. Kullanım
```
cd sablon
latexmk -lualatex tez.tex
```
Ayrıntılar: depo kökündeki `README.md`.
