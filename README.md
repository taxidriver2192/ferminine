# Feminine Planway Scraper

## Beskrivelse

Dette projekt består af to Python-scripts, der scraper data fra en Planway-webside og genererer en HTML-side med de hentede data. Formålet er at lette visningen af behandlinger og priser fra en Planway-baseret klinik.

## Filer

### `main.py`
Dette script scraper data fra en specificeret Planway-side og gemmer resultaterne i en JSON-fil.

#### Funktioner:
- Sender en GET-request til en Planway-URL.
- Parser HTML-indholdet for at finde kategorier og tilhørende services.
- Gemmer de hentede data i en JSON-fil (`produkter/services.json`).

### `generate_website.py`
Dette script læser JSON-dataene genereret af `main.py` og konverterer dem til en HTML-side.

#### Funktioner:
- Læser JSON-dataene fra `produkter/services.json`.
- Genererer en HTML-side (`produkter/services.html`) med kategorier og services, inkl. billeder og detaljerede beskrivelser.

## Installation og brug

``` sh
git clone https://github.com/taxidriver2192/ferminine.git
cd ferminine
```

``` sh
python main.py
```

``` sh
python generate_website.py
```
