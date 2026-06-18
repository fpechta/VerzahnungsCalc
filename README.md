# VerzahnungsCalc

Kleine Django-Anwendung zur Berechnung von Verzahnungsgeometrien (Teilkreis-,
Kopfkreis- und Fußkreisdurchmesser) basierend auf Modul und Zähnezahl.

## Stack

- Python 3 / Django
- SQLite (lokale Entwicklung)
- Server-side Templates (kein Frontend-Framework)

## Setup

```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

Danach im Browser: http://127.0.0.1:8000/

## Projektstruktur

```
verzahnungscalc/   Projekt-Settings, URL-Konfiguration
gears/             App: Model, View, Berechnungslogik, Template
  gear_calculator.py   reine Berechnungsfunktionen, unabhängig von Django
  models.py            Gear-Model (ORM) inkl. Berechnungsmethoden
  views.py             GET/POST-Handling, Speicherung
  templates/gears/calculator.html
```

## Berechnete Größen

- Teilkreisdurchmesser: `d = m * z`
- Kopfkreisdurchmesser: `da = m * (z + 2)`
- Fußkreisdurchmesser: `df = m * (z - 2.5)`

## Geplante Erweiterungen

- Übersetzungsverhältnis für zweites Zahnrad (`i = z2 / z1`)
- Admin-Interface
- CSV-Import (Simulation einer Migration aus Altsystemen wie MS Access)
