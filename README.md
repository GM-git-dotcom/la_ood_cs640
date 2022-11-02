# Layer Adaptive Out-of-Distribution detection for CS640
LA-OOD implementation for the CS640 project.

# Team members
GM Harshvardhan, Harshil Gandhi, Kathakoli Sengupta.

# Overview

In this project, we will be using Wang's LA-OOD https://github.com/haoliangwang86/LA-OOD (paper: https://arxiv.org/pdf/2203.00192.pdf) for out-of-distribution detection on satellite images on So2Sat (https://github.com/zhu-xlab/So2Sat-LCZ42).


# Implementation (preliminary)
The implementation pipeline is as follows:

## 1. Train the backbone models
```python
python train_backbone_model.py --model vgg16 --dataset cifar10
```

## 2. Download the OOD datasets
Download the following dataset:
* Tiny ImageNet: https://image-net.org/index.php

save the unzipped files in ./data folder


## 3. Generate the dataset
Generate the InD and OOD datasets:
```python
python generate_datasets.py
```

## 4. Save the intermedia outputs
```python
python save_inter_outputs.py --model vgg16 --ind cifar10
```

## 5. Train OOD detectors
```python
python train_ood_detectors.py --model vgg16 --ind cifar10
```

The above step trains all the One-Class SVMs (OCSVMs) to detect whether an image is out-of-distribution or not.


## 6. Test: OOD detection
```python
python detect_oods.py --model vgg16 --ind cifar10
```
