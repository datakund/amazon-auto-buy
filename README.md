## Amazon-Auto-Buy-Python
Amazon-Auto-Buy is a python library that uses browser automation to purchase items on Amazon automatically. 
At present, it runs on windows only.

Complete Documentation available [here](https://amazon-api.datakund.com/en/latest/)

### Installation

```sh
pip install amazon-auto-buy
```

### Import

```sh
from amazon_auto_buy import *
```

### Login

To buy a product on amazon first we need to login to amazon. There are two ways of login:-
* Credentials
* Cookies

#### Credentials

```sh
amazon.login(email="",password="")
```

#### Cookies

```sh
amazon.login_cookie(cookies=list_of_cookies)
```

##### Example Cookies

To login with cookies [Edit this Cookie Extension](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg?hl=en) can be added to browser and login to amazon.com , then export cookies and paste in above function of ``login_cookie``. Below is the example of cookies.

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

### Buy Product

To click on buy button can ``buy`` function by passing amazon product link in **product_url**.
```sh
amazon.buy(product_url='product link')
```

### Select Payment method

Select payment method by calling ``select_payment_method`` function and pass payment method in **payment_method**. For example, "State Bank of India", "Upi", "Net Banking".
```sh
amazon.select_payment_method(payment_method='Punjab National Bank Debit Card')
```

### Select Bank

Select bank by calling ``select_bank`` function and pass bank name in **bank**. For example, "State Bank of India"
```sh
amazon.select_bank(bank='Punjab National Bank Debit Card')
```

### Fill cvv

Fill cvv by calling function ``fill_cvv`` and pass cvv number in **cvv**.
```sh
amazon.fill_cvv(cvv='345')
```

### Place Order

Finally place order by calling function ``place_order``.
```sh
amazon.place_order()
```

### datakund
It uses [datakund](https://pypi.org/project/datakund/) internally to do browser automation
