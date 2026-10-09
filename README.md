# Software-ingeniaritza agentikoa: lantalde hibridoak kudeatzeko eskuliburua (lan-karpeta)

Karpeta hau liburuaren lan-eremua da (UEUren unibertsitate-liburuen diru-poltsa, 2026ko deialdia).

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

Kapitulu bakoitzaren `.tex` fitxategiaren hasieran iruzkin bat dago helburuarekin eta berrerabil daitekeen materialarekin.


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

