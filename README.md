# SAÜ FBE Doktora Tezi LaTeX Şablonu

Sakarya Üniversitesi Fen Bilimleri Enstitüsü'nün (SAÜ FBE) resmi **Word doktora/yüksek lisans tez şablonunun**
ve **Lisansüstü Tez Yazım Kılavuzu**'nun (Senato 04.08.2022, 621-9) LaTeX karşılığıdır.

Şablon, Word çıktısıyla **sayfa sayfa aynı** olacak şekilde ölçülerek hazırlanmıştır:
kenar boşlukları, başlık aralıkları, satır yükseklikleri, satır sonları, tablo/şekil başlıkları,
denklem numaraları, içindekiler ve listeler, sayfa numaraları.

> **Not:** Bu çalışma enstitünün resmi bir ürünü değildir. Tez tesliminden önce güncel kılavuzu ve
> enstitünün duyurularını kontrol ediniz. Word şablonu ve kılavuzun hakları SAÜ FBE'ye aittir.

## Word ve LaTeX karşılaştırması

| Dosya | İçerik |
|---|---|
| [`karsilastirma/yan_yana_word_latex.pdf`](karsilastirma/yan_yana_word_latex.pdf) | Her sayfada solda Word, sağda LaTeX çıktısı (77 sayfa) |
| [`word/SAU_FBE_Doktora_Tez_Sablonu.docx`](word/SAU_FBE_Doktora_Tez_Sablonu.docx) | Enstitünün resmi Word şablonu (karşılaştırmanın kaynağı) |
| [`word/SAU_FBE_Doktora_Tez_Sablonu_Word_ciktisi.pdf`](word/SAU_FBE_Doktora_Tez_Sablonu_Word_ciktisi.pdf) | Word şablonunun Word'den alınmış PDF'i |
| [`karsilastirma/latex_ciktisi.pdf`](karsilastirma/latex_ciktisi.pdf) | Bu şablonun LaTeX çıktısı |
| [`karsilastirma/SONUC_RAPORU.md`](karsilastirma/SONUC_RAPORU.md) | Denetim raporu: yöntem, ölçümler, Word şablonundaki hatalar, bilinçli farklar |

Özet sonuç: iki PDF de 77 sayfa ve her sayfa karşılığıyla eşleşiyor. 1228 eşleşen satırın 820'sinde
dikey sapma ≤ 1 pt; 30 sayfa satır satır aynı. Kalan farkların çoğu Word şablonundaki tutarsızlıklardan
kaynaklanır (ayrıntılar raporda).

## Gereksinimler

**Tezi derlemek için:**

| Gereksinim | Ayrıntı |
|---|---|
| TeX dağıtımı | [TeX Live](https://tug.org/texlive/) 2022 veya üstü, ya da güncel [MiKTeX](https://miktex.org/) (LaTeX çekirdeği 2021-06 veya üstü) |
| Derleyici | **LuaLaTeX** (pdfLaTeX/XeLaTeX desteklenmez; satır modeli Lua ile yazılmıştır) |
| Derleme aracı | `latexmk` (önerilir; TeX Live ve MiKTeX ile gelir) |
| LaTeX paketleri | `fontspec`, `unicode-math`, `babel` (turkish), `geometry`, `xcolor`, `graphicx`, `float`, `array`, `multirow`, `longtable`, `pdflscape`, `amsmath`, `eso-pic`, `ulem`, `etoolbox`, `titlesec`, `titletoc`, `footmisc`, `caption`, `calc`, `hyperref`, `enumitem` (hepsi standart dağıtımda var; MiKTeX eksikleri kendisi kurar) |
| Yazı tipleri | **Times New Roman** ve **Cambria Math** (Windows ve Microsoft Office ile gelir). Yoksa otomatik olarak **TeX Gyre Termes** ve **STIX Two Math** / TeX Gyre Termes Math kullanılır; bu durumda satır sonları Word'den biraz farklı olabilir. |

Linux'ta Microsoft yazı tipleri için örnek: `sudo apt install ttf-mscorefonts-installer` (Cambria Math bu pakette yoktur; STIX Two Math kullanılır).
Overleaf'te derleyici olarak **LuaLaTeX** seçilmelidir.

**Karşılaştırma araçları için (isteğe bağlı):** Python 3.9+ ve [`requirements.txt`](requirements.txt)
(`pip install -r requirements.txt`).

## Hızlı başlangıç

```bash
cd sablon
latexmk -lualatex tez.tex
```

ya da `lualatex tez.tex` komutunu üç kez çalıştırın (içindekiler ve listeler için). Çıktı: `sablon/tez.pdf`.

## Dosya yapısı

```
sablon/
  tez.tex            ana dosya: tez bilgileri ve bölümlerin sırası
  sauthesis.cls      biçim kuralları (kenar boşlukları, başlıklar, listeler, sayfa numarası...)
  sauwordline.lua    Word'ün satır kırma ve satır yüksekliği modeli
  onkisim/           teşekkür, kısaltmalar, simgeler, özet, summary
  bolumler/          bölümler, kaynaklar, ekler, özgeçmiş
  sekiller/          görseller
word/                resmi Word şablonu ve PDF çıktısı
karsilastirma/       yan yana PDF, LaTeX çıktısı, denetim raporu ve araçlar
```

## Sınıf seçenekleri

```latex
\documentclass[doktora,notlar,wordbirebir]{sauthesis}
```

| Seçenek | Anlamı |
|---|---|
| `doktora` / `yukseklisans` | Tez türü |
| `notlar` / `notsuz` | Şablondaki kırmızı/mavi açıklama notlarını ve kapaktaki not kutusunu göster/gizle. **Teslimden önce `notsuz` yapın.** |
| `wordline` (varsayılan) / `texline` | Word satır modeli (açgözlü satır kırma, Word satır yüksekliği) ya da klasik TeX dizgisi |
| `wordbirebir` | Word şablonunun altbilgi ve sayfa akışı özelliklerini de kopyalar (aşağıya bakın). Kaldırılırsa tüm sayfa numaraları aynı hizada olur ve her bölüm sağ (tek) sayfadan başlar. |

## Tez bilgileri

`tez.tex` başındaki komutlarla girilir: `\tezbasligi`, `\tezbasligitr`, `\tezbasligien`, `\tezbasligibeyan`,
`\teztipi` (`DOKTORA TEZİ` / `YÜKSEK LİSANS TEZİ`), `\yazar`, `\yazarbeyan`, `\anabilimdali`, `\bilimdali`,
`\danisman`, `\ortakdanisman`, `\kapaktarihi`, `\savunmatarihi`, `\tesekkurimza`.
`\anabilimdali` ve `\bilimdali` boş bırakılırsa gri "Bir öğe seçin." yer tutucusu basılır.

## Yazım komutları

| Amaç | Komut |
|---|---|
| 1.–4. derece başlık | `\chapter{}`, `\section{}`, `\subsection{}`, `\subsubsection{}` |
| 5. derece (numarasız) başlık | `\baslikbes{}` |
| Numarasız 1. derece başlık (İçindekiler'e girer) | `\bolumsuz{}` |
| Şekil (başlık altta) | `\begin{figure}[H] \centering \includegraphics[width=..]{..} \caption{..} \label{..} \end{figure}` |
| Tablo (başlık üstte) | `\begin{table}[H] \caption{..} \centering \begin{tabular}..\end{tabular} \end{table}` |
| Devam eden tablo | `\begin{table}[H] \ContinuedFloat \caption[]{\devami{} Başlık.} ...` |
| Numaralı denklem → (3.1) | `\begin{denklem} ... \label{..} \end{denklem}` |
| Uzun alıntı | `\begin{alinti} ... \end{alinti}` |
| Kısaltma / simge | `\kisaltma{AIC}{Akaike ...}`, `\simge{C}{...}` |
| Kaynak girdisi (asılı girinti) | `\kaynak{Yazar, A. (2020). ...}` |
| Ekler | `\ekler` sonra her ek için `\ek{}` → EK A, Şekil A.1, Tablo A.1 |
| Yatay sayfa | `\begin{landscape} ... \end{landscape}` |

## Uygulanan kurallar

- A4, ayna kenar boşlukları: üst 2,5 cm, alt 2,5 cm, iç (cilt) 4 cm, dış 2,5 cm.
- Times New Roman 12 pt; ana metin 1,5 satır, paragraf önce/sonra 6 nk, iki yana yaslı.
- 1. derece başlık: büyük harf, koyu, önce 72 / sonra 18 nk. 2. derece: önce 18 / sonra 12 nk;
  3.–4. derece: önce 12 / sonra 6 nk.
- Özet, liste sayfaları, kaynaklar, başlıklar ve dipnotlar tek satır aralıklı.
- Şekil başlığı altta (önce 6 / sonra 12 nk), tablo başlığı üstte (önce 12 / sonra 6 nk);
  "Şekil 2.1." / "Tablo 2.1." koyu; tek satıra sığarsa ortalı, sığmazsa iki yana yaslı ve asılı girintili.
- Denklem numarası (3.1) sağda, normal yazı, sonunda nokta yok.

### Sayfa numaraları

- Alt-orta, Times New Roman 12 pt koyu.
- Dış kapak ve arkası numarasız; iç kapak (i) ve arkası (ii) sayılır ama numara basılmaz.
- Onay sayfasından itibaren Roma rakamı (iii, iv, …); ön kısmın sonundaki boş sayfa numarasız.
- Ana metinden itibaren Arap rakamı (1, 2, …). Numaralı bölümlerin (1., 2., 3., …) ilk sayfası
  numarasızdır ama sayılır; KAYNAKLAR, EKLER ve ÖZGEÇMİŞ ilk sayfaları numaralıdır.
- `\bolumilksayfanosuz` bir sonraki `\chapter*` (ör. `\bolumsuz{...}`) sayfasını da numarasız yapar.
- `wordbirebir` açıkken Word şablonundaki şu özellikler de kopyalanır: 1. bölümden ilk yatay sayfaya kadar
  numara 47 pt daha yukarıdadır ve metin alanı daha kısadır (Word altbilgisindeki boş paragraf);
  yatay sayfalarda numara koyu değildir; ana metindeki bölümler bir sonraki sayfadan başlar ve
  Word'deki boş sayfalar `bolum5`, `ekler`, `ozgecmis` dosyalarının başındaki `\cleardoublepage` ile verilir.

## Word şablonunda tespit edilen hatalar

Denetimde Word şablonunun kendi içinde bazı tutarsızlıklar bulundu. Bunlar ve LaTeX'in bu noktalarda neyi esas
aldığı [`karsilastirma/SONUC_RAPORU.md`](karsilastirma/SONUC_RAPORU.md) dosyasının 4. bölümündedir. Örnekler:

- Sayfa numarası üç farklı yükseklikte (alttan ≈2,75 cm, ≈3,5 cm ve ≈1,8 cm); kılavuz 1,5 cm diyor.
- Bölüm ilk sayfalarının bir kısmı numaralı, bir kısmı numarasız ("farklı ilk sayfa" ayarı yalnızca üç bölümde açık).
- 3. bölüm çift sayfadan başlıyor; kılavuz bölümlerin sağ sayfadan başlamasını istiyor.
- 3.3.1.1 başlığından önce fazladan boş paragraf var (kılavuz: "paragrafların arasında boş satır bulunmamalıdır").
- Yatay sayfalarda görünen numara elle konmuş dikey metin kutusu; altbilgideki asıl numara beyaz kutuyla örtülü.
- İçindekiler'de "ÖZET" ve "EKLER" satırlarında noktalı sekme bozuk; "Table 2.4." yazım hatası.

## Karşılaştırmayı yeniden üretmek

```bash
pip install -r requirements.txt
python karsilastirma/araclar/compare_pdfs.py word/SAU_FBE_Doktora_Tez_Sablonu_Word_ciktisi.pdf sablon/tez.pdf rapor.txt
python karsilastirma/araclar/yan_yana.py word/SAU_FBE_Doktora_Tez_Sablonu_Word_ciktisi.pdf sablon/tez.pdf yan_yana.pdf
```

`compare_pdfs.py` sayfaları içerik benzerliğine göre eşler ve her sayfa için sayfa numarasını, satır sayılarını,
metin farklarını ve eşleşen satırların dikey/yatay sapmalarını yazar. `yan_yana.py` iki PDF'i tek PDF'te yan yana koyar.

## Katkı

Hata bildirimleri ve öneriler için GitHub Issues kullanabilirsiniz. Kılavuz veya Word şablonu güncellenirse
lütfen bildirin.

## Lisans

LaTeX sınıfı, Lua modülü ve araçlar [MIT lisansı](LICENSE) ile dağıtılır. `word/` klasöründeki Word şablonu ve
şablon metinleri Sakarya Üniversitesi Fen Bilimleri Enstitüsü'ne aittir; karşılaştırma amacıyla, enstitünün
sitesinde herkese açık yayımlanan haliyle konmuştur.
