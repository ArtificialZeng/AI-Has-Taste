# PDF audit

Status: **PASS**  
Artifact: `output/pdf/sts15-pasch-diameter.pdf`  
Pages: 5  
Final SHA-256: `ec6c19cff46f9441f6901b792735950771a7b0ea438f293a280eef70197695a7`

## Metadata and identity

- Title: *The Pasch-switch quotient graph of STS(15) has diameter 11*
- Author metadata and body author: Zijian Zeng
- Affiliation: Institute of Computer Science and Digital Innovation, UCSI
  University, Kuala Lumpur, 56000, MALAYSIA
- Emails: `zijianzeng@foxmail.com` and
  `1002266693@ucsiuniversity.edu.my`
- No additional author appears.

## Page-by-page visual inspection

The final PDF was rendered at 150 dpi with Poppler and every page was
inspected.

| Page | Contents checked | Result |
|---:|---|---|
| 1 | title, author, abstract, introduction | pass |
| 2 | complete main theorem, definitions, start of construction | pass |
| 3 | catalogue hash, independent replay, exact-count table | pass |
| 4 | diameter pairs/path/layers, hashes, audit limitations | pass |
| 5 | computational disclosure, references, affiliation, both emails | pass |

The first rendering exposed a theorem split across pages; `needspace` was
added and the PDF was rebuilt. The final rendering has no clipping,
overlap, broken glyphs, table overflow, or unreadable hash line.
