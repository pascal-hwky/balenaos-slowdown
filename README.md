# balenaOS slowdown

The Python script `benchmark.py` in this repository runs significantly slower on a **Jetson Nano Dev Kit** with **balenaOS 2.47** than it does with **balenaOS 2.45**. The Python script uses TFLite to do 100 inferences on a neural network and reports its timing. The results can be seen below and reproduced by running the following command if you have the balena CLI installed and an application `<app-name>` set-up with a Jetson Nano:

```
balena push <app-name>
```

The timing results are reported below. As you can see, balenaOS 2.47 causes the benchmark to run 75% slower.

## 2.45

`balenaOS 2.45.1+rev3 (production), 
supervisor 10.3.7`

```
Finished 100 inferences.
Max time: 156 [ms]
Min time: 78 [ms]
Avg time: 81 [ms]
```

## 2.47

`balenaOS 2.47.1+rev1 (production), 
supervisor 10.3.7`

```
Finished 100 inferences.
Max time: 593 [ms]
Min time: 326 [ms]
Avg time: 376 [ms]
```
