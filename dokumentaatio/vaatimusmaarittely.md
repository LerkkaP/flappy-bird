# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on pygame -kirjastolla toteutettu **Flappy Bird** -tyylinen _peli_. Pelissä lennetään linnulla putkien välistä ja tarkoituksena on saada mahdollisimman suuri pistetulos eli lentää mahdollisimman pitkälle. Jos lintu putoaa maahan tai osuu putkiin, peli loppuu ja sen voi aloittaa alusta.

## Perusversion toiminnallisuus

### Alkutilanne

- Välkkyvä aloituskuva
- Pelin voi aloittaa painamalla **space-näppäintä** tai **vasenta hiirinäppäintä**

### Pelitilanne

- Maa liikkuu
- Pistemäärä on alussa 0
- Lintua voi lentää klikkaamalla **space**-näppäintä tai **vasenta hiirinäppäintä**
- Ruudulla näkyvä pistemäärä päivittyy kun kahden putken välistä lennetään onnistuneesti
- Peli päättyy jos lintu osuu putkiin tai maahan

### Lopputilanne

- Näytetään saatu tulos ja kaikkien aikojen paras tulos
- Pelin voi aloittaa uudestaan painamalla **restart** painiketta tai **space-näppäintä**

## Jatkokehitysideoita

- Split screen version lisääminen
- Objektien lisääminen joita keräämällä saa lisäpisteitä
- Eri vaikeustasojen lisääminen:
  - Kasvava nopeus
  - Ylimääräisten objektien lisääminen, joita tulee väistellä
