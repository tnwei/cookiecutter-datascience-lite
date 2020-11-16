import sys
import os

### Print output path ----------------------------------------------

project_name = "{{ cookiecutter.project_name }}"
project_path = os.path.abspath(os.path.join("..", project_name))

print("New project directory created at %s" % project_path)

### Print helpful statements ---------------------------------------

### Exit -----------------------------------------------------------

sys.exit(0)
