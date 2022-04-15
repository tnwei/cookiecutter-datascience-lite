# Recipes


A few recipes for common use cases.

## Logging

Reasonable logging defaults provided in `utils.get_logger`. Writes to `logs/`. Inspired by Kedro on this one. Returns a Python logging object that writes to `projectroot/logs/` under the logger's name.
This configuration can be tweaked referring to https://docs.python.org/3/library/logging.config.html:
Import using: 

```
from utils import get_logger 

logger = get_logger(__name__)
logger.info("Loop completed")
logger.debug("This line should not appear in logs!")
logger.warning("This msg shows up if memory leaks are occuring")
```

Initially used a yaml file to configure the logger. Opted instead to store config in code, as it allows writing logs to file using the logger's name. Plus it requires installing pyyaml to start with, rather this just works out of the box. 


## Batch jobs (including but not limited to hyperparameter sweeps)

For DS, batch jobs typically involve running hyperparameter sweeps for training deep learning / machine learning models. But there are also many cases where batch jobs need to be run e.g. heavy data processing scripts 

Put logic into a script, specify configuration files and use `hydra` to queue and run batch jobs. For deep learning jobs, link up with either Weights and Biases or self-hosted MLFlow (TODO mlflow-docker link here)

## Documentation

Options:

+ Jupyter Book (can publish pdf and website) -> for extensive documentation, knits as a structured website / book
+ mkdocs (website) -> simple to set up
+ pandoc (pdf) -> knits into an article report

Original text:

This cookiecutter uses `mkdocs` for documentation. Write your docs in Markdown in the `docs/` directory, and modify `mkdocs.yml` in the project root accordingly. See [mkdocs website](https://www.mkdocs.org/) for more info.

## Packaging

Many ways according to blogposts. Link them here and explain them.

Found that the best way to do this is to simply use setup.py. Most DS env management uses conda and pip, which is quite compatible with the traditional setup.py. Rules out PyEnv and Poetry which do their own environment management. Might be old and might not be the best, but least hassle and gets things working overwhelming majority of the time

Single source versionining decided to use a VERSION.txt file after reading. Does not overcomplicate with additional tools or dependencies.

https://martin-thoma.com/python-package-versions/
https://packaging.python.org/en/latest/guides/single-sourcing-package-version/

If you prefer other packaging methods like PyEnv and Poetry, feel free to roll your own

`pip install .` the package. You can also do `pip install . -e` so that you don't need to upgrade the installation, but I recall facing strange errors with them that went away after I recreated my Python env and stuck to `pip install .`

## Tests

Simple stuff like using pytest. Import code from the code folder and run them here.

Concept of unit test and integration tests. Should test especially if have key pieces of logic that needs to be relied on. Don't bother testing once-off and unimportant logic.

## Git commit linting

## Python code qualiy

+ ast for if the code runs in the first place
+ black for consistent code style

## Env management cheat sheet

Conda cheat sheet?
+ Create new env
+ Switch new env
+ Remove env
+ Show packages
+ Save to env yaml

Good practices for conda that paid out:
+ Usually have a base env where JLab and `nb_conda_kernels` is installed, while other envs just have ipykernel installed so that they are accessible from the central JLab. Allows for working on any project using the right kernel
+ Install mamba in base conda env, use mamba as a drop-in replacement for conda. Resolves pretty fast
+ Store everything in env yaml

Without conda, use virtualenv.

Virtualenv cheat sheet:
+ TODO


## Pre-commit

This cookiecutter comes with a default `.pre-commit-config.yaml`. After pre-commit is installed, run the following in the project directory to set up the commit hooks:

```
pre-commit install
pre-commit install --hook-type commit-msg
```
