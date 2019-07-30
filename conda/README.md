# Conda cheatsheet

Commonly used anaconda commands

Create new env named py35\
`conda create --name py35 python=3.5`

Activate\
`source activate py35`

Get list of all env\
`cona env list`

Make a copy of existing env\
`conda create --clone py35 --name py35-2`

Delete environment\
`conda env remove -n <env_name>`

List all package\
`conda list`

Deactivate current env\
source deactivate

Install a package\
`conda install <pacakge_name>`

Update a package\
`conda update <pacakge_name>`

Detect new conda env in jupyter notebook:\
(Install following pacakage in new conda env)\
`conda install nb_conda`

Run jupyter notebook from command line\
```
jupyter-notebook
jupyter-notebook --port 1234
jupyter-notebook --port 1234 --ip 0.0.0.0
```

Add conda environment to jupyter lab
[StackOverflow](https://stackoverflow.com/questions/53004311/how-to-add-conda-environment-to-jupyter-lab)
```
$ conda activate cenv
(cenv)$ conda install ipykernel
(cenv)$ ipython kernel install --user --name=<any_name_for_kernel>
(cenv($ conda deactivate
```


Other cheatsheets:

[Cheatsheet 1](http://know.continuum.io/rs/387-XNW-688/images/conda-cheatsheet.pdf)
[Cheatsheet 2](https://jacknorthrup.com/Multiple-Program-Languages-Documentation/conda-cheatsheet.pdf)

