# cookiecutter-datascience-lite

Light [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for starting data science projects, contains minimal scaffolding to get started quickly. After installing the `cookiecutter` Python package, run `cookiecutter https://github.com/tnwei/cookiecutter-datascience-lite` to create a new project repo. 

Note: This repo is a WIP, predominantly focused on usage on Linux.


## Motivation

Used [cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science) for a bit, personally grew to prefer starting projects with a clutter-free bare minimum project structure, and gradually expanding the project as needed.

## Directory Structure

```
 ├── assets/        : Stores static files that are used in the project
 ├── code/          : Stores scripts and Jupyter notebooks
 │   └── data.py    : Python module to implement data loading functions
 ├── data/          : Stores data for the project
 ├── .gitignore     : List of files to skip tracking in git
 ├── output/        : Stores project output, be it plots or predictions
 ├── README.md      : Project README
 ├── references/    : Stick reference documents here. Recommended to exclude from version control.
 └── TODO.md        : TODO list for project-specific task tracking
``` 
