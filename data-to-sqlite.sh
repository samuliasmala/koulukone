#!/bin/bash
rm data/yle-koulukone.db
sqlite-utils insert data/yle-koulukone.db schools data/schools.csv --csv -d --pk=tunn
sqlite-utils insert data/yle-koulukone.db locations data/locations.csv --csv -d --pk=tunn

python transform-locations.py
