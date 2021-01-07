Amazon-Auto-Buy is a python library that automatically uses browser automation to purchase items on Amazon. 
At present, it runs on windows only.

Complete Documentation available [here](https://youtube-api.datakund.com/en/latest/)

### Installation

```sh
pip install amazon-auto-buy
```

### Usage
1. Install [Edit This Cookie Extension](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg?hl=en) in browser
2. Login to youtube.com in your browser
3. Open extension & click on export cookies tab to copy cookies to clipboard
4. Then in the code paste your cookies in _login_cookie function_
   * cookies
5. Fill in all the inputs required in _upload function_
   * title
   * description
   * video_path
   * kid_type
   * type
5. Then run the code ```python youtube_video_upload.py```

### Example Cookies
```[
{
    "domain": ".youtube.com",
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
    "domain": ".youtube.com",
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
