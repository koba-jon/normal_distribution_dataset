import argparse
import os
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--dir', type=str, default='./ND-dataset')
parser.add_argument('--num', type=int, default=100)
parser.add_argument('--dim', type=int, default=300)
parser.add_argument('--mean', type=float, default=0.0)
parser.add_argument('--std', type=float, default=1.0)
parser.add_argument('--seed', type=int, default=0)
args = parser.parse_args()

os.makedirs(args.dir, exist_ok=False)
np.random.seed(args.seed)

digit = len(str(args.num - 1))

for i in range(args.num):
    fname = args.dir + f'/{str(i).zfill(digit)}.dat'
    data = np.random.normal(args.mean, args.std, (args.dim))
    np.savetxt(fname, data)
