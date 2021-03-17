#!/bin/bash

MODE='train'

SCRIPT_DIR=$(cd $(dirname $0); pwd)

python3 ${SCRIPT_DIR}/create.py \
    --dir "./ND-dataset/${MODE}" \
    --num 5000 \
    --dim 300 \
    --mean 0.0 \
    --std 1.0 \
    --seed 0
