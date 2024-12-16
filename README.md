# YLE koulukone data

[YLE Koulukone](https://yle.fi/a/74-20018233) aineisto sekä koulujen sijainnit [Paikkatietohakemistosta](https://www.paikkatietohakemisto.fi/geonetwork/srv/fin/catalog.search#/metadata/6a8b4061-7a48-4667-bbdb-13952726c79f) visualisoituna kartalle [Datasette](https://datasette.io/)n avulla. Aineistot löytyvät CSV ja SQLite -muodoissa [data/](data) hakemistosta.

[Testaa visualisointia](https://koulukone.samcode.fi/yle-koulukone/finnish_schools) ja katso miten koulut sijoittuvat kartalle.

## Käyttöönotto

```bash
# Install venv if needed
sudo apt install python3-venv
# Create environment
python3 -m venv .venv
# Activate environment
source .venv/bin/activate
# Install dependencies
pip install -r requirements.txt
# Install Datasette plugins
datasette install datasette-cluster-map
# Serve database
datasette serve --immutable data/yle-koulukone.db \
    --setting max_returned_rows 5000 \
    --metadata metadata.yaml
```

## Sarakekuvauksia

Voimassaolo (OLO):

- 0 = Voimassaoleva
- 1 = Lakkautettu tilastovuonna
- 2 = Yhdistynyt toiseen oppilaitokseen tilastovuonna
- 3 = Oppilaitos poistettu koululaitoksen oppilaitoksista
- 6 = Oppilaitoksessa ei ole toimintaa tilastovuonna
- 7 = Tekninen poisto

Oppilaitostyyppi (OLTYP):

- 11 = Peruskoulut
- 12 = Peruskouluasteen erityiskoulut
- 15 = Lukiot
- 19 = Perus- ja lukioasteen koulut
