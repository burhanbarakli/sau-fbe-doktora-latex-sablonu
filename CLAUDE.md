# Claude için notlar

Bu depo, SAÜ FBE lisansüstü tez şablonunun LaTeX sürümüdür. Kullanıcı tezini `sablon/` içinde yazar.

- Derleme yalnızca **LuaLaTeX** ile: `sablon` klasöründe `latexmk tez.tex` (`latexmkrc` LuaLaTeX'i seçer).
  pdfLaTeX / XeLaTeX ile derleme hata verir.
- Kullanıcının değiştireceği dosyalar: `sablon/tez.tex` (tez bilgileri, jüri, bölüm sırası),
  `sablon/onkisim/*.tex`, `sablon/bolumler/*.tex`, `sablon/sekiller/`.
- `sablon/sauthesis.cls` ve `sablon/sauwordline.lua` biçim kurallarını (kılavuz + Word ölçüleri) taşır;
  kullanıcı açıkça istemedikçe değiştirme.
- Bütün komutlar ve örnekler: `README.md` ve https://burhanbarakli.github.io/sau-fbe-doktora-latex-sablonu/
  (kaynağı `docs/index.html`).
- Kaynaklar varsayılan olarak `bolumler/kaynaklar.tex`'e elle (`\kaynak`, `kaynaklistesi`) yazılır. Kullanıcı
  Zotero/`.bib` isterse `tez.tex`'teki `\input{bib-ayar}` ve `\addbibresource` satırlarını aç, `kaynaklar.tex`'i
  `\bolumsuz{KAYNAKLAR}` + `\printbibliography[heading=none]` yap (ayrıntı: `sablon/bib-ayar.tex`, README).
- Teslim çıktısı için `\documentclass[...,notsuz]{sauthesis}` kullanılır.
- `docs/`, `karsilastirma/` ve `word/` tez yazımı için gerekmez; kullanıcı istemedikçe dokunma.
