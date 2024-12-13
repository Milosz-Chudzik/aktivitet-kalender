#  trenings app

## Oversikt

**trenings applikasjon** er et Python-basert verktøy som bruker en kalender oversikt til å lagre og hente notater for spesifikke datoer.  Koden bruker en kobling til en SQL-database for å lagre notater for hver måned, og har en begrenset tilgang til året 2024.

## Funksjoner

- Viser måneds kalender for året 2024.
- Lar brukere:
  - Legge til notater på spesifikke datoer.
  - Se notater som er lagret for spesifikke datoer.
- Lagrer notater i en MySQL-database for datalagring.

## Dette trenger du for å kjøre koden 

- Python 3.x
- MySQL-server
- Python-pakker:
  - `mysql-connector-python`
  - `calendar`

## Oppsett

### 1. Installer Avhengigheter

Installer de nødvendige Python-pakkene ved å kjøre følgende kommando:

```bash
pip install mysql-connector-python
```

### 2. Databasekonfigurasjon

Sørg for at du har en MySQL-database med følgende struktur:

- Databasenavn: ("navnet på databasen din")
- Tabeller for hver måned:
  - `january`, `february`, ..., `december`
  - Hver tabell bør ha kolonnene: `date` (DATE) og `notes` (TEXT).

### 3. Oppdater Tilkoblings detaljer

Erstatt informasjonen i kode avsnittet med detaljene for din SQL-server:

```python
mydb = mysql.connector.connect(
    host="10.2.2.119", 
    user="din_bruker",
    password="ditt_passord",
    database="år"
)
```

### Brukerhandlinger

- **Se Kalender**: Viser kalenderen for den valgte måneden.
- **Legge til Notat**: Lar brukeren skrive et notat for en spesifikk dato.
- **Se Notat**: Henter og viser notatet for en spesifikk dato.
- **Gå Tilbake til Hovedmeny**: Naviger tilbake til måneds valget.

## Eksempel på Interaksjon

1. **Velg en Måned**: Skriv inn et tall mellom 1 og 12.
2. **Velg en Handling**:
   - Skriv `1` for å legge til et notat.
   - Skriv `2` for å se et notat.
3. **Skriv inn en Dato**: Oppgi en dato i formatet `YYYY-MM-DD`. Standard er `2024-01-01` hvis du lar feltet stå tomt.

## Notater

- Sørg for at databasen er korrekt konfigurert og kjører før du starter applikasjonen.
- Alle månedene er hardkodet; ekstra år krever kodeendringer.

## Fremtidige Forbedringer

- Forbedre kalenderen med enklere kode
- Få koden ut av terminalen

