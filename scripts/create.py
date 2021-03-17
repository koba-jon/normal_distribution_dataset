import argparse
import os
import random
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--dir', type=str, default='./NormalDistribution')
parser.add_argument('--num', type=int, default=100)
parser.add_argument('--dim', type=int, default=300)
parser.add_argument('--list', type=str, default='./list/params.txt')
parser.add_argument('--seed', type=int, default=0)
args = parser.parse_args()

os.makedirs(args.dir, exist_ok=False)
random.seed(args.seed)
np.random.seed(args.seed)

digit = len(str(args.num - 1))

params = np.loadtxt(args.list)

param_all = []
for i in range(args.dim):
    param_all += [random.choice(params)]

for i in range(args.num):
    data = []
    for j in range(args.dim):
        data += [np.random.normal(param_all[j][0], param_all[j][1])]
    fname = args.dir + f'/{str(i).zfill(digit)}.dat'
    np.savetxt(fname, data)
