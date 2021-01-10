# cookiecutter-datascience-lite

Light [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for starting data science projects, contains minimal scaffolding to get started quickly. After installing the `cookiecutter` Python package, run `cookiecutter https://github.com/tnwei/cookiecutter-datascience-lite` to create a new project repo. 


## Motivation

I used [cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science) for a bit, personally grew to prefer starting projects with a clutter-free bare minimum project structure, and gradually expanding the project as needed. Thus this repo.


## Directory Structure

```
 ├── assets/        : Stores static files that are used in the project
 ├── code/          : Stores scripts and Jupyter notebooks
 │   └── data.py    : Python module to implement data loading functions
 │   └── utils.py   : Python module to implement utility functions
 ├── conf/          : Stores configuration files for the project
 ├── data/          : Stores data for the project
 ├── .gitignore     : List of files to skip tracking in git 
 ├── logs/          : Stores logs for the project
 ├── output/        : Stores project output, be it plots or predictions
 ├── README.md      : Project README
 ├── references/    : Stick reference documents here. Recommended to exclude from version control.
 └── TODO.md        : TODO list for project-specific task tracking
```


## Design intent
+ `code/` is specified minimally, containing both scripts and notebooks. This is for the convenience of sharing code in common Python modules. For more complex projects, it is left to the user to spin off dedicated `scripts`, `notebooks`, `src` directories and a `setup.py` file.
+ A default `data.py` is placed in `code/` for the data scientist to implement data loading functions as needed.
+ A default `utils.py` is placed in `code/` to house utility functions. 
+ Reasonable logging defaults provided in `conf/`, writes to `logs/`. Inspired by Kedro on this one.
+ `output` folder is not compartmentalized between reports, plots, prediction outputs etc. It is left to the user to create subfolders for larger projects. 
+ `.gitignore` defaults are minimally specified, no assumptions are made for tracking / not tracking repo folders in VCS. Left to user to decide e.g. whether to track `assets`, `TODO.md` etc.
+ At the moment, a `docs/` folder is not provisioned. Small projects have info contained in README and notebooks. Up to user to implement if scope calls for it.
