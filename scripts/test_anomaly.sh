#!/bin/bash

MODE='test_anomaly'

SCRIPT_DIR=$(cd $(dirname $0); pwd)

python3 ${SCRIPT_DIR}/create.py \
    --dir "./ND-dataset/${MODE}" \
    --num 1000 \
    --dim 300 \
    --mean 3.0 \
    --std 0.1 \
    --seed 0
