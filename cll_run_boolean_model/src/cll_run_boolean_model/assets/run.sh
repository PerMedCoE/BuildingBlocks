#!/usr/bin/env bash

export PATH=$PATH:/home/permed/MaBoSS-env-2.0-master/engine/src
cd /home/permed
python3 run_boolean_model.py $@
