# cookiecutter-datascience-lite (WIP, overhaul in progress)

Light [cookiecutter](https://github.com/cookiecutter/cookiecutter) template for starting data science projects. Minimal enough to stay out of your way when starting a project, sufficiently adaptable to remain useful as the project evolves.  

## Motivation

I used [cookiecutter-data-science](https://github.com/drivendata/cookiecutter-data-science) and [Kedro](https://kedro.readthedocs.io/en/stable/) for a bit, personally grew to prefer starting projects with a clutter-free bare minimum project structure, and gradually expanding the project as needed. Thus this repo.

## Example usage

After installing the `cookiecutter` Python package, run `cookiecutter gh:tnwei/cookiecutter-datascience-lite` to create a new project repo. Example:

```bash
tnwei@rama:~/projects$ cookiecutter gh:tnwei/cookiecutter-datascience-lite

project_name [Project name]: Iris Species Classification
project_slug [iris-species-classification]: iris
New project directory created at /home/tnwei/projects/iris

A default .pre-commit-config.yaml is included in the project dir.
To use it, install `pre-commit`, `cd` into the project dir and run:

$ cd iris
$ git init
$ pre-commit install -t commit-msg -t pre-commit

Refer to https://pre-commit.com/ for more info.
```

Created repo structure:

```bash
tnwei@rama:~/projects/iris$ tree
.
├── assets
├── data
├── iris
│   ├── data.py
│   └── utils.py
├── logs
├── output
└── README.md
```
