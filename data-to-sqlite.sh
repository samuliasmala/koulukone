#!/bin/bash

sqlite-utils insert data/yle-koulukone.db schools data/schools.csv --csv -d
sqlite-utils insert data/yle-koulukone.db locations data/locations.csv --csv -d
