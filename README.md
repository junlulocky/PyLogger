# PyLogger
A light weight python logger package for logging research results etc. Currently more to my own appetite.


## Installation

```
[for master version] pip3 install git+https://github.com/junlulocky/PyLogger.git (Highly Recommended)
```


## Examples

Details:

| Code | Description |
|:-------:| ----------- |
| [example](./examples/logger_info.py) | example for how to use the logger info func |


### loger info
```python
from pylogger import set_logger

name = 'test'
save_path = './tmp_res/res_alpha-{}'.format(name)  ## it will automatically create the folder of res_alpha-test
logger = set_logger(save_path=save_path)

something = 'something'
logger.info('best hyperparmeter: {}'.format(something))  ## save information to log
```
