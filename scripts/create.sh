#!/bin/bash

MODE='create'

SCRIPT_DIR=$(cd $(dirname $0); pwd)

python3 ${SCRIPT_DIR}/create.py \
    --dir "./NormalDistribution/${MODE}" \
    --num 100 \
    --dim 300 \
    --list "./list/params.txt" \
    --seed 0
