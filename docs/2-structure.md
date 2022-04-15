# Structure overview

We create a project repo called `iris` for sake of demonstration. The repo will have the following directory structure:

```
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

This cookiecutter creates the following folders upon init:

+ Code and notebooks are stored in the folder named after the project slug, in this case `iris`. 
+ `data` is self-explanatory. 
+ All artifacts generated goes into `output`, but if they are reusable like models, data pipelines etc, they go into `assets`. 
+ `logs` stores logging output. 

This cookiecutter also creates a default README and reasonable default dotfiles (See 3-recipes.md)

These are the core folders, occasionally more stuff is required. Some of these are included in `.template`. Read more in 3-optional-structure. 

## Code

### Subdir structure

This is how my code folder tends to look like:

```
iris/
├── 1.0-data-extraction.ipynb
├── 1.1-data-extraction.ipynb
├── 2.0-eda.ipynb
├── 2.1-eda.ipynb
├── 3.0-baseline-model.ipynb
├── 4.0-explore-specific-feature-X.ipynb
├── 5.0-explore-specific-feature-y.ipynb
├── 6.0-integrate-ml-with-business-logic.ipynb
├── 6.1-integrate-ml-with-business-logic.ipynb
├── 6.2-integrate-ml-with-business-logic.ipynb
├── 7.0-hyperparameter-search.ipynb
├── data.py
├── utils.py
├── net.py
├── pipeline.py
...
```

I chose to stick both modules and notebooks in the same folder. This is for the convenience of sharing code in common Python modules, as opposed to having separate folders for notebooks and scripts. The project slug is chosen as the code directory name, because it makes it easy to package as a Python library if required. This works because notebooks and markdown files are ignored during packaging unless explicitly included. 

Two placeholder modules are specified:

+ A default `data.py` for data loading functions, and
+ A default `utils.py` for utility functions, which includes a preconfigured logger.

Given that this is the working folder, occasionally markdown files are included for brainstorming purposes. 

### Semver system

Use sem ver when it comes to notebooks and scripts. Each new line of inquiry is its own major version. Updates are minor versions. Modules that store importable code and are meant to be reused do not follow this semver system.

Used to just call this folder `code/`, but that actually conflicts with a std lib! 

## Data

### Structuring the subdir

Can make the data folder as extensive as possible, or as simple as possible. 

You can treat it like a bucket, storing every single thing for really small projects. Or you can also organize them organically, e.g. group by date or by type. 

Typically, I create `raw` and `processed` subdirs for locally stored data to differentiate between data received as-is, and data that has been processed somewhat and ready for further use. 

For more extensive examples, can study how cookiecutter data science or Kedro organize their folders. TODO: Leave links

### Data README

If there's a lot of data, create a README to record what file does what. Also useful for storing URLs for data stored in the cloud. 

Example README:

```
TODO
```

### Mounting a hard drive (Linux)

Might even consider linking the data to a large hard drive. Cheat sheet below:

```bash
# Link data/ to a folder in /mnt/data/iris-data
TODO

# Unlink the folder
# Warning: calls delete under the hood, be careful with this command!
TODO
```

## Assets and outputs

A single `output` folder stored the results of running code. Can be anything between reports, plots, saved prediction outputs etc.
`assets` serve the same purpose, but with the idea that the contents should be usable across multiple notebooks / scripts, and need to be stored at the end of the project. Typically saved models fall into this category.

Outputs can be a simple dump folder, or extensively sort them into plots / results etc
+ `output` folder is not compartmentalized between reports, plots, prediction outputs etc. It is left to the user to create subfolders for larger projects. 
