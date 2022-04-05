# Structure overview

Place Tree here similar to README

```
$ tree
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

## Data

`data/` folder. Suggestions:Create a README within `data/` to record brief descriptions of locally stored files, as well as URLs to data stored in buckets etc

Example README:

```

```

Might even consider linking the data to a large hard drive. Cheat sheet below:

```

```

Can make it as extensive as possible, or as simple as possible. Personally like to separate between `raw` and `processed` for locally stored data. Extensive examples can look at cookiecutter data science or kedro (include examples below)

## Code

Example from a real project (names modified):

```
TODO tree
```

+ `code/` is specified minimally, containing both scripts and notebooks. This is for the convenience of sharing code in common Python modules. For more complex projects, it is left to the user to spin off dedicated `scripts`, `notebooks`, `src` directories and a `setup.py` file.
+ A default `data.py` is placed in `code/` for the data scientist to implement data loading functions as needed.
+ A default `utils.py` is placed in `code/` to house utility functions. 
+ Reasonable logging defaults provided in `conf/`, writes to `logs/`. Inspired by Kedro on this one.

+ A subdir with the name of the project slug designed to store scripts, notebooks and the occasional markdown file during development
+ Use project slug because then it becomes easier to package into a Python package if need be. Notebooks and markdown files will be ignored unless explicitly included. 
+ setup.py template included for packaging. Out of many methods for Python packaging, still the simplest and most efficient way to do it. See dedicated packaging section
+ Numbered 1.0, 2.0, 3.0 etc. Modifications upon previous versions are stored by incrementing minor versions.
+ Modules for reusable code doesn't have numbers
+ Mainstays of the code folder is a data.py and utils.py. data.py for everything involved with loading data, utils.py for small utility functions.
+ Used to be just called `code/` but that actually conflicts with a std lib! 


## Configuration

If a lot of configuration is required e.g. training deep learning models, suggest to open a new `conf/` folder and store configuration files there.


## References

Put files here that are not directly involved in development, but are somewhat related. e.g. old handover code, supporting info from Powerpoints od Docx files, PDFs etc

## Docs

Dump any project documentation into `docs/`. 
+ At the moment, a `docs/` folder is not provisioned. Small projects have info contained in README and notebooks. Up to user to implement if scope calls for it.

Can do it as an information dump:

```
TODO tree of informal info dump
```

If time permits, can set things up with neat documentation. 

See Documentation section

## Assets and outputs

A single `output` folder stored the results of running code. Can be anything between reports, plots, saved prediction outputs etc.
`assets` serve the same purpose, but with the idea that the contents should be usable across multiple notebooks / scripts, and need to be stored at the end of the project. Typically saved models fall into this category.

Outputs can be a simple dump folder, or extensively sort them into plots / results etc
+ `output` folder is not compartmentalized between reports, plots, prediction outputs etc. It is left to the user to create subfolders for larger projects. 

## Dotfiles

TODO: Explain what the dotfiles do, link to recipes for what they do
