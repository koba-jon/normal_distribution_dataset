# Normal Distribution Dataset
1-dimensional shape dataset generated by random numbers of normal distribution


## Usage

### Original Dataset

#### Get
```
$ git clone https://github.com/koba-jon/normal_distribution_dataset.git
$ cd normal_distribution_dataset/ND-dataset
$ ls -l
```

#### Hierarchy

- train : training data (5000 pieces) of 300 dimensions generated by random numbers of N(0, 1)
```
train
|--0000.dat
|--0001.dat
...
|--4999.dat
```

- test(normal) : test data (1000 pieces) of 300 dimensions generated by random numbers of N(0, 1)
```
test_normal
|--000.dat
|--001.dat
...
|--999.dat
```

- test(anomaly) : test data (1000 pieces) of 300 dimensions generated by random numbers of N(3, 0.1)
```
test_anomaly
|--000.dat
|--001.dat
...
|--999.dat
```

### Create Dataset

```
$ vi create.sh
```

`--dir` : output directory <br>
`--num` : total number of data <br>
`--dim` : dimensions on one data <br>
`--mean` : mean of Normal Distribution <br>
`--std` : standard deviation of Normal Distribution <br>
`--seed` : seed of random number <br>

```
#!/bin/bash

MODE='create'

SCRIPT_DIR=$(cd $(dirname $0); pwd)

python3 ${SCRIPT_DIR}/create.py \
    --dir "./ND-dataset/${MODE}" \
    --num 100 \
    --dim 300 \
    --mean 0.0 \
    --std 1.0 \
    --seed 0
```

```
$ sh create.sh
```
