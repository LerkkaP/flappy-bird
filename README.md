# Ohjelmistotekniikka, harjoitustyö

## Flappy Bird

**Flappy Bird** on 2D-peli, jossa on tarkoituksena lentää mahdollsimman pitkälle samalla väistäen putkia.

## Huomio

Peli vaatii toimiakseen vähintään Pythonin version __3.9__, jotta __Matplotlib__ toimii.

## Dokumentaatio

- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Käyttöohje](dokumentaatio/kayttoohje.md)
- [Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)
- [Changelog](dokumentaatio/changelog.md)
- [Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](dokumentaatio/testaus.md)
- [GithubRelease](https://github.com/LerkkaP/otharjoitustyo/releases/tag/viikko6)

## Käyttöönotto

1. Suorita seuraava komento asentaaksesi tarvittavat riippuvuudet

```bash
poetry install
```

2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Invoke-komennot

Sovelluksen käynnistys:

```bash
poetry run invoke start
```

Testien ajaminen:

```bash
poetry run invoke test
```

Testikattavuusraportin luominen:

```bash
poetry run invoke coverage-report
```

Pylintin ajaminen

```bash
poetry run invoke lint
```

Automaattinen formatointi

```bash
poetry run invoke format
```

## Viimeisin GitHub release

Ohjelman viimeisimpään GitHub releaseen pääsee [täältä](https://github.com/LerkkaP/otharjoitustyo/releases/tag/viikko7)

## Pelin grafiikat ja ääniefektit

Pelin grafiikat ja ääniefektit ovat peräisin [täältä](https://github.com/samuelcust/flappy-bird-assets) (poislukien Pygamen omat tekstit)

Niiden käyttöoikeus on myönnetty seuraavan MIT-lisenssin mukaisesti:

MIT License

Copyright (c) 2019 Samuel Custodio

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
