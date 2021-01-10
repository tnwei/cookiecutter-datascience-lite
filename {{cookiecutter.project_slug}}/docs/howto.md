# How-tos

### Logging

This cookiecutter has a `utils.get_logger` function defined in `code/`, with reasonable default configurations that writes brief logs to stdout, and detailed logs into the `logs/` directory. This configuration can be tweaked referring to https://docs.python.org/3/library/logging.config.html:
+ **Using a config file**. A default logging config is provided in `conf/logging.yml`. Note that loading this config file requires the `pyyaml` package to be installed. Overrides the following option.
+ **Hard-coded config in the function itself**. If the `pyyaml` is not installed, or if the specified YAML config file is not found, the function has some hard-coded configs that can be tweaked. 

```
# Instead of 
import logging
logger = logging.getLogger(__name__)

# Use
from utils import get_logger
logger = get_logger(__name__)
```



