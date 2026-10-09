# Agenteak software-garapeneko lantaldeetan integratzeko eskuliburua (lan-karpeta)

Karpeta hau liburu berriaren lan-eremua da (UEUren unibertsitate-liburuen diru-poltsa, 2026ko deialdia).
Aurreko liburua, *Git Bertsioak Kontrolatzeko Sistemarako eskuliburua* (2024), osorik dago GitHubeko
`ilopezgazpio/Git_BKS_eskuliburua` biltegian; hemen liburu berrirako behar dena eta erreferentziarako
balio duena baino ez da gorde. Izenburua eta kapituluen izenburuak behin-behinekoak dira.

## Karpeten egitura

| Karpeta | Edukia |
|---|---|
| `00_deialdia_administrazioa/` | UEUren deialdia (URLa, poltsaren ezaugarriak, poltsadunen betebeharrak), 2022ko eskari-orria (eredu gisa), 2024ko ebaluazio-txostena, UEUko elkarrizketa eta `marketing_2024/` (posterra, katalogo-orria). |
| `01_idazketa_oharrak/` | Terminologia-erabakiak (`aspell` agindua barne), goiburuen neurriak eta letra-tipoa, LaTeX euskaraz erabiltzeko oharrak. |
| `latex/` | Liburu berriaren LaTeX proiektua: `main.tex`, `structure.tex`, `bibliography.bib`, `chapters/` (11 kapitulu) eta `Pictures/` (kapitulu berrien zenbakien arabera antolatua). `.github/workflows/main.yml` lan-fluxuak karpeta hau konpilatzen du. |
| `adibideak/` | Ekosistemaren adibide-proiektuak: `ekosistema_maven` (Java + Maven, test-karpetarekin), `ekosistema_java`, `ekosistema_python`. 8. kapituluko ariketen oinarria. Bakoitzak bere `.git` historia du (aurreko liburuko ariketena). |
| `aurreko_liburua_2024/` | 2024ko liburuaren kapituluak (`kapituluak/*.tex`), `main_2024.tex`, argitaratutako PDFa eta liburu berrian berrerabiliko **ez** diren irudiak (`irudiak/<kapitulu zaharra>/`), jatorrizko `.xoj` fitxategiekin. **Kontuz: `.xoj` jatorrizkoak ez daude GitHuben; hau da kopia bakarra.** |

## Aurkibidearen zirriborroa eta materialaren mapa

| Kap. | Izenburua (behin-behinekoa) | Fitxategia | Aurreko liburutik berrerabil daitekeena |
|---|---|---|---|
| 1 | Hitzaurrea eta helburuak | `01-hitzaurrea.tex` | 1. eta 2. kapitulu zaharrak (tonua, egitura). Pluralean idatzi; eskuak zikintzen hasi 20. orrialderako. |
| 2 | Taldeak eta rolak | `02-taldeak_rolak.tex` | 9. kapitulu zaharra, 1. ariketa (Belbin, rolen banaketa). |
| 3 | Erabiltzaile-historiatik agentearen zereginera | `03-zereginak.tex` | 2. kapitulu zaharra, "SDMak eta Git" (INVEST, agile vs ur-jauzi). Irudiak `Pictures/03/`. |
| 4 | Biltegia, lan-eremu partekatua | `04-biltegia.tex` | 8. kapitulu zaharra, metodologien atala (Git-flow, Github-flow). Irudiak `Pictures/04/`. CI: `.github/workflows/main.yml`. |
| 5 | Kodetzeko agenteak | `05-agenteak.tex` | Berria. Tresna zehatzak eranskinera eta biltegi lagunera. |
| 6 | Agent-scrum | `06-agent_scrum.tex` | 9. kapitulu zaharra (Scrum egokitua, backlog-ak); 2. kapitulua (garapen inkremental dinamikoa). |
| 7 | Ariketak: kaixo, agent-scrum! | `07-ariketak_kaixo.tex` | 5. kapitulu zaharra (ariketen formatua). |
| 8 | Ariketak: ekosistema agenteekin | `08-ariketak_ekosistema.tex` | 9. kapitulu zaharra osorik (Nami, Ane, Mikel, Gotzon); `adibideak/`; irudiak `Pictures/08/`. |
| 9 | Egiaztapena eta berrikuspena | `09-egiaztapena.tex` | 7. kapitulu zaharra, 5. ariketa (testen garrantzia). |
| 10 | Ohiko arazoak eta errezetak | `10-arazoak.tex` | 10. kapitulu zaharra (egitura arazoa -> errezeta). Irudiak `Pictures/10/`. |
| 11 | Eranskina: txantiloiak eta konfigurazioa | `11-eranskina.tex` | `.github/workflows/main.yml`. |

Kapitulu bakoitzaren `.tex` fitxategiaren hasieran iruzkin bat dago helburuarekin eta berrerabil daitekeen materialaren bide zehatzekin.
Kapituluen goiburuak (`\chapterimage`) aurreko liburukoak dira, behin-behinekoak: 1-7 zenbaki beraren goiburua, 8. kapituluak 9. zaharrarena, 9.ak 8. zaharrarena, 10.ak 10. zaharrarena, 11.ak goiburu hutsa.
Jatorrizko `.xoj` fitxategiak irudi bakoitzaren ondoan daude, berriro marrazteko.

Egiteke daudenak `structure.tex`-en: koadro nabarmenduen etiketa oraindik "Git" da (`\newtheorem{theoremeT}[dummy]{Git}`), eta `bibliography.bib`-ek aurreko liburuko erreferentzia guztiak ditu (`\nocite{*}` dago `main.tex`-en, garbitu bukaeran).

## Konpilatu

Dependentziak: `texlive-latex-extra`, `texlive-bibtex-extra`, `texlive-lang-french`, `texlive-publishers`, `biber`.

```
cd latex
pdflatex main.tex
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

