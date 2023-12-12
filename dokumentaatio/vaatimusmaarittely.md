# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on pygame -kirjastolla toteutettu **Flappy Bird** -tyylinen _peli_. Pelissä lennetään linnulla putkien välistä ja tarkoituksena on saada mahdollisimman suuri pistetulos eli lentää mahdollisimman pitkälle. Jos lintu putoaa maahan tai osuu putkiin, peli loppuu ja sen voi aloittaa alusta.

## Perusversion toiminnallisuus

### Alkutilanne

- Välkkyvä aloituskuva &#9745;
- Pelin voi aloittaa painamalla **space-näppäintä** tai **vasenta hiirinäppäintä** &#9745;

### Pelitilanne

- Maa liikkuu &#9745;
- Pistemäärä on alussa 0 &#9745;
- Lintua voi lentää klikkaamalla **space**-näppäintä tai **vasenta hiirinäppäintä** &#9745;
- Putket liikkuvat ja niiden välistä voi lentää &#9745;
- Ruudulla näkyvä pistemäärä päivittyy kun kahden putken välistä lennetään onnistuneesti &#9745;
- Peli päättyy jos lintu osuu putkiin tai maahan &#9745;

### Lopputilanne

- Pisteet tallennetaan tietokantaan &#9745;
- Näytetään saatu tulos ja kaikkien aikojen paras tulos &#9745;
- Pelin voi aloittaa uudestaan painamalla **restart** painiketta &#9745;
- **figure** painikkeesta voi nähdä tilastoja

## Jatkokehitysideoita

- Split screen version lisääminen
- Objektien lisääminen joita keräämällä saa lisäpisteitä
- Eri vaikeustasojen lisääminen:
  - Kasvava nopeus
  - Ylimääräisten objektien lisääminen, joita tulee väistellä
