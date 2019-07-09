
# Git CheatSheet

List of frequently used git commands

## nvidia-smi
[Details](https://www.andrey-melentyev.com/monitoring-gpus.html)

## GPU Memory allocation
Prevent TensorFlow to allocate all GPU memory
[StackOverflow](https://stackoverflow.com/questions/34199233/how-to-prevent-tensorflow-from-allocating-the-totality-of-a-gpu-memory)

Keep a watch on GPU Usage:\
`watch -d -n 1 nvidia-smi`
(-d: shows the changes between two refresh cycles)


## Conda env setup

Create new env\
```conda 
conda create --name keras
conda activate keras
conda install keras-gpu
```
