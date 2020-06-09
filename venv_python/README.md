# venv CheatSheet

Frequently used python virtual environment commands

## venv Commands

Create a new env (This creates a directory by the name of env\
in working directory)\
`pythone -m venv env_name`

Activate env\
`source env_name/bin/activate`

Deactivate env\
`deactivate`

## venv wrapper

Install\
`pip install virtualenvwrapper`

Check following link for further details\
[venv wrapper](https://realpython.com/python-virtual-environments-a-primer/#managing-virtual-environments-with-virtualenvwrapper)

## Add venv in jupyter notebook

``` bash
pip install ipykernel
python -m ipykernel install --user --name env_name --display-name "Python-Anything"
```
