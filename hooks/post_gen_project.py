import sys
import os

### Print output path ----------------------------------------------

project_name = "{{ cookiecutter.project_name }}"
project_path = os.path.abspath(os.path.join("..", project_name))

print("New project directory created at %s" % project_path)
print()

### Print helpful statements ---------------------------------------

print(
"""A default .pre-commit-config.yaml is included in the project dir.
To use it, install `pre-commit` and run `pre-commit install` in
the project dir. Refer to https://pre-commit.com/ for more info.""")
print()

### Exit -----------------------------------------------------------

sys.exit(0)
