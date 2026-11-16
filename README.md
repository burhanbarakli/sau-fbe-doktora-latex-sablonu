# SAÜ FBE Doktora Tezi LaTeX Şablonu

Sakarya Üniversitesi Fen Bilimleri Enstitüsü'nün (SAÜ FBE) resmi **Word doktora/yüksek lisans tez şablonunun**
ve **Lisansüstü Tez Yazım Kılavuzu**'nun (Senato 04.08.2022, 621-9) LaTeX karşılığıdır.

Şablon Word çıktısı ölçülerek hazırlanmış ve kılavuzun bütün kurallarıyla tek tek denetlenmiştir:
kenar boşlukları, başlık aralıkları, satır yükseklikleri, satır sonları, tablo/şekil başlıkları,
denklem numaraları, içindekiler ve listeler, sayfa numaraları.

**İlke: kılavuz esastır.** Kılavuzun açıkça belirlediği her konuda LaTeX kılavuza uyar; kılavuzun
belirlemediği konularda Word şablonu izlenir. Word şablonunun kılavuza aykırı olduğu yerlerde (aşağıda)
LaTeX çıktısı bilerek Word'den ayrılır.

> **Not:** Bu çalışma enstitünün resmi bir ürünü değildir. Tez tesliminden önce güncel kılavuzu ve
> enstitünün duyurularını kontrol ediniz. Word şablonu ve kılavuzun hakları SAÜ FBE'ye aittir.

**📖 Resimli kullanım kılavuzu:** <https://burhanbarakli.github.io/sau-fbe-doktora-latex-sablonu/>.
Kılavuz, neyin hangi dosyada ve hangi komutla değiştirildiğini numaralı ekran görüntüleriyle anlatır.
Kaynağı [`docs/`](docs/) klasöründedir.

## Word ve LaTeX karşılaştırması

| Dosya | İçerik |
|---|---|
| [`karsilastirma/yan_yana_word_latex.pdf`](karsilastirma/yan_yana_word_latex.pdf) | Her sayfada solda Word, sağda LaTeX çıktısı (79 sayfa) |
| [`word/SAU_FBE_Doktora_Tez_Sablonu.docx`](word/SAU_FBE_Doktora_Tez_Sablonu.docx) | Enstitünün resmi Word şablonu (karşılaştırmanın kaynağı) |
| [`word/SAU_FBE_Doktora_Tez_Sablonu_Word_ciktisi.pdf`](word/SAU_FBE_Doktora_Tez_Sablonu_Word_ciktisi.pdf) | Word şablonunun Word'den alınmış PDF'i |
| [`karsilastirma/latex_ciktisi.pdf`](karsilastirma/latex_ciktisi.pdf) | Bu şablonun LaTeX çıktısı |
| [`karsilastirma/SONUC_RAPORU.md`](karsilastirma/SONUC_RAPORU.md) | Denetim raporu: yöntem, ölçümler, Word şablonundaki hatalar, bilinçli farklar |

Özet sonuç: Word 77, LaTeX 79 sayfa; fark, kılavuz gereği bölümlerin sağ (tek) sayfadan başlaması için
eklenen 2 boş sayfadır. Kılavuza aykırı olmayan yerlerde çıktı Word ile örtüşür; farkların tamamı
Word şablonunun kılavuza aykırı noktalarından kaynaklanır (ayrıntılar raporda).

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
`sablon/latexmkrc` dosyası sayesinde yalnızca `latexmk tez.tex` yazmak da LuaLaTeX ile derler; Overleaf ve
VS Code LaTeX Workshop da bu dosyayı okur.

## Dosya yapısı

```
sablon/
  tez.tex            ana dosya: tez bilgileri ve bölümlerin sırası
  sauthesis.cls      biçim kuralları (kenar boşlukları, başlıklar, listeler, sayfa numarası...)
  sauwordline.lua    Word'ün satır kırma ve satır yüksekliği modeli
  onkisim/           teşekkür, kısaltmalar, simgeler, özet, summary
  bolumler/          bölümler, kaynaklar, ekler, özgeçmiş
  sekiller/          görseller
  latexmkrc          latexmk'yi LuaLaTeX'e ayarlar
docs/                kullanım kılavuzu (GitHub Pages), görseller ve görsel üretme aracı
word/                resmi Word şablonu ve PDF çıktısı
karsilastirma/       yan yana PDF, LaTeX çıktısı, denetim raporu ve araçlar
```

## Sınıf seçenekleri

```latex
\documentclass[doktora,notlar]{sauthesis}
```

| Seçenek | Anlamı |
|---|---|
| `doktora` / `yukseklisans` | Onay sayfasındaki "Doktora Tezi / Yüksek Lisans Tezi olarak kabul edilmiştir" ifadesi (kapaktaki tür `\teztipi` ile yazılır) |
| `notlar` / `notsuz` | `notlar`: şablondaki kırmızı/mavi açıklamalar, kapaktaki not kutusu ve "(Varsa)", "(Gerekliyse)", "(OCAK 2022)" gibi örnek notlar görünür. `notsuz`: bu notlar hiç basılmaz, metin içindeki renkli yazılar siyaha döner; verilmemiş "varsa" alanları (bilim dalı, ortak danışman, 20/22 cm jüri yerleri) kalkar. **Teslimden önce `notsuz` yapın ve şablon metinlerini kendi metninizle değiştirin.** |
| `wordline` (varsayılan) / `texline` | Word satır modeli (açgözlü satır kırma, Word satır yüksekliği) ya da klasik TeX dizgisi |

## Tez bilgileri

`tez.tex` başındaki komutlarla girilir: `\tezbasligi`, `\tezbasligitr`, `\tezbasligien`, `\tezbasligibeyan`,
`\teztipi` (`DOKTORA TEZİ` / `YÜKSEK LİSANS TEZİ`), `\yazar`, `\ogrencino` (iç kapakta yazar adının altına), `\yazarbeyan`, `\anabilimdali`, `\bilimdali`,
`\danisman`, `\ortakdanisman`, `\kapaktarihi`, `\savunmatarihi`, `\tesekkurimza`, `\beyantarihi`.
`\anabilimdali` ve `\bilimdali` boş bırakılırsa gri "Bir öğe seçin." yer tutucusu basılır; `notsuz` çıktıda
verilmemiş bilim dalı ve ortak danışman satırları hiç basılmaz. Etik kurul onayı gerekmiyorsa `\etikonayyok`
beyannamedeki ilgili cümleyi çıkarır.

Onay sayfasındaki metin `\yazar`, `\tezbasligibeyan`, `\savunmatarihi`, `\anabilimdali`, `\bilimdali` ve tez
türünden kendiliğinden oluşur (gerekirse `\onayyazar`, `\onaybaslik`, `\onayteztipi` ile elle verilir). Jüri:

```latex
\juribaskani{Prof. Dr. Ad SOYAD}{Sakarya Üniversitesi}        % 12 cm
\juridanisman{Prof. Dr. Ad SOYAD}{Sakarya Üniversitesi}       % 14 cm (verilmezse \danisman)
\juriortakdanisman{Doç. Dr. Ad SOYAD}{Sakarya Üniversitesi}   % 16 cm (verilmezse \ortakdanisman)
\juriuyesi{Prof. Dr. Ad SOYAD}{Ankara Üniversitesi}          % 18 cm; ikinci ve üçüncü kez: 20 ve 22 cm
```

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
| Ekler | `\ekler` sonra her ek için `\ek{Ekin adı}` → "EK A. Ekin adı", Şekil A.1, Tablo A.1 |
| Şablon notu (notsuz'da siyah) | `\notrenk{FF0000}{metin}` |
| Yatay sayfa | `\begin{landscape} ... \end{landscape}` |

## Uygulanan kurallar

- A4, ayna kenar boşlukları: üst 2,5 cm, alt 2,5 cm, iç (cilt) 4 cm, dış 2,5 cm (ön kısım dahil her sayfa).
- Times New Roman 12 pt; ana metin 1,5 satır, paragraf önce/sonra 6 nk, iki yana yaslı; paragraflar arasında boş satır yok.
- 1. derece başlık: büyük harf, koyu, önce 72 / sonra 18 nk, sağ (tek) sayfadan başlar.
  2. derece: önce 18 / sonra 12 nk; 3.–4. derece: önce 12 / sonra 6 nk.
- Teşekkür, içindekiler, listeler, özetler, kaynaklar, ekler, özgeçmiş, tablo/şekil başlıkları ve dipnotlar tek satır aralıklı.
- İçindekiler Teşekkür ile başlar; Tablo ve Şekil listelerinde girişler arasında önce 6 / sonra 6 nk.
- Şekil başlığı altta (önce 6 / sonra 12 nk), tablo başlığı üstte (önce 12 / sonra 6 nk);
  "Şekil 2.1." / "Tablo 2.1." koyu; tek satıra sığarsa ortalı, sığmazsa iki yana yaslı ve 2. satır
  numaradan sonraki metinle aynı hizada; devam eden tabloda "Tablo 2.3. (Devamı): …".
- Denklem metin bloğuna ortalı, numara (3.1) sağda, normal yazı, sonunda nokta yok.
- Dış kapak yazıları kapağın dış kenarına göre ortalı, tez başlığı 14 pt; iç kapakta tez başlığı 12 pt ve
  yazar adının altında öğrenci numarası; onay sayfasında jüri yuvaları 12/14/16 (ortak danışman)/18/20/22 cm.
- Ekler: "EK A. Ekin adı"; Şekil A.1, Tablo A.1. Özgeçmiş: "TEZDEN TÜRETİLEN YAYINLAR/SUNUMLAR".

### Sayfa numaraları

- Alt-orta, alttan 1,5 cm, Times New Roman 12 pt koyu. Yatay sayfalarda okuma yönündeki alt kenarın
  (uzun kenar) ortasında, alttan 1,5 cm, koyu.
- Dış kapak ve arkası numarasız; iç kapak (i) ve arkası (ii) sayılır ama numara basılmaz.
- Onay sayfasından itibaren aralıksız Roma rakamı (iii, iv, …), boş arka sayfalar dahil.
- Ana metinden itibaren Arap rakamı (1, 2, …). Numaralı bölümlerin (1., 2., 3., …) ilk sayfası
  numarasızdır ama sayılır; KAYNAKLAR, EKLER ve ÖZGEÇMİŞ ilk sayfaları numaralıdır.
  (Kılavuz bu konuda açık hüküm içermez; numaralı bölüm ilk sayfalarında da numara istenirse
  `sauthesis.cls` içindeki `\chapter` tanımında `\thispagestyle{sauempty}` kaldırılır.)
- `\bolumilksayfanosuz` bir sonraki `\chapter*` (ör. `\bolumsuz{...}`) sayfasını da numarasız yapar.

## Word şablonunun kılavuza aykırı noktaları

Denetimde Word şablonunun kılavuzla çelişen ya da kendi içinde tutarsız olduğu noktalar bulundu; LaTeX'te bu
noktalarda kılavuz uygulandı. Tam liste [`karsilastirma/SONUC_RAPORU.md`](karsilastirma/SONUC_RAPORU.md)
dosyasının 6. bölümünde, kılavuzun iki türlü okunabildiği yerler 7. bölümündedir. Örnekler:

- Sayfa numarası üç farklı yükseklikte (alttan ≈2,74 cm, ≈3,47 cm ve ≈1,80 cm); kılavuz 1,5 cm diyor.
- Yatay sayfalarda görünen numara elle konmuş, koyu olmayan dikey metin kutusu ve kısa kenarda.
- 3. bölüm çift sayfadan başlıyor; kılavuz bölümlerin sağ sayfadan başlamasını istiyor.
- Dış kapak yazı bloğuna göre ortalı; iç kapakta tez başlığı 14 pt ve öğrenci numarası yok.
- Onay sayfasında ortak danışman yuvası yok; etik beyanname İçindekiler'de.
- Ekler, özgeçmiş ve dipnotlar 1,5 satır aralıklı; kaynaklar ve özgeçmişte girişler arasında boş paragraflar var.
- 3.3.1.1 başlığından önce fazladan boş paragraf; İçindekiler'de "ÖZET" ve "EKLER" satırlarında noktalı sekme bozuk;
  "Table 2.4." yazım hatası.

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
