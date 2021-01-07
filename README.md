# amazon-auto-buy
Amazon-Auto-Buy is a python library to buy product on amazon automatically using browser automation. 
It currently runs only on windows.

This module depends on the following python modules
* [requests](https://pypi.org/project/requests/)
* [datakund](https://pypi.org/project/datakund/)

#### DataKund
[datakund](https://pypi.org/project/datakund/) is needed for browser automation. As soon as this library is imported in code, automated browser will open up in which product will be bought. To buy first login will need to be done. Login can be done either with credentials or via cookies

Complete documentation for Amazon Automation available [here](https://amazon-api.datakund.com/en/latest/)

### Installation

```sh
pip install amazon-auto-buy
```

### Import
```sh
from amazon_auto_buy import *
```
