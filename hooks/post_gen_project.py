import sys
import os

### Print output path ----------------------------------------------

project_slug = "{{ cookiecutter.project_slug }}"
project_path = os.path.abspath(os.path.join("..", project_slug))

print("New project directory created at %s" % project_path)
print()

### Print helpful statements ---------------------------------------

print(
    f"""A default .pre-commit-config.yaml is included in the project dir.
To use it, install `pre-commit`, `cd` into the project dir and run:

$ cd {project_slug}
$ git init
$ pre-commit install -t commit-msg -t pre-commit

Refer to https://pre-commit.com/ for more info."""
)
print()

### Exit -----------------------------------------------------------

sys.exit(0)
