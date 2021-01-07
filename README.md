### Introduction
Amazon-Auto-Buy is a python library that uses browser automation to purchase items on Amazon automatically. 
At present, it runs on windows only.

Complete Documentation available [here](https://amazon-api.datakund.com/en/latest/)

### Installation

```sh
pip install amazon-auto-buy
```

### Usage
1. Install [Edit This Cookie Extension](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg?hl=en) in browser
2. Login to amazon.com in your browser
3. Open extension & click on export cookies tab to copy cookies to clipboard
4. Then in the code paste your cookies in _login_cookie function_
   * cookies
5. There are two ways of purchasing product:-
   #### Credit/Debit Card
   1. Login with cookies as defined above with _login_cookie function
   2. Select Payment Method by passing ``payment_method`` in ``select_payment_method`` i.e "State Bank of India"
   3. Fill cvv by passing ``cvv`` in ``fill_cvv`` function
   4. Now place order by calling ``place_order`` function
   5. Then run the code ```python Amazon_Buy_With_Card.py```
   #### Net Banking
   1. Login with cookies as defined above with _login_cookie function
   2. Select Payment Method by passing ``payment_method`` in select_payment_method i.e "Net Banking"
   3. Select bank by passing bank name in ``select_bank``
   4. Now place order by calling ``place_order`` function
   5. Then run the code ```python Amazon_Buy_With_Net_Banking.py```

### Example Cookies
```[
{
    "domain": ".amazon.com",
    "expirationDate": 1671116358.392265,
    "hostOnly": false,
    "httpOnly": false,
    "name": "__Secure-3PAPISID",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "Y1zkx3HJhktM4Y__/A-aOUDHse1TaSaKpQ",
    "id": 1
},
{
    "domain": ".amazon.com",
    "expirationDate": 1672322803.302724,
    "hostOnly": false,
    "httpOnly": true,
    "name": "__Secure-3PSID",
    "path": "/",
    "sameSite": "no_restriction",
    "secure": true,
    "session": false,
    "storeId": "0",
    "value": "5AcqKCt5MuBkjOpLW7PdfNs83knLqt-qVZJzCriY_4_cftxmyExDbYRS65ezLjpKa_Xc7Q.",
    "id": 2
},
...
...

]
```

### datakund
It uses [datakund](https://pypi.org/project/datakund/) internally to do browser automation
