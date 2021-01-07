from amazon_auto_buy import *

amazon.login_cookie(cookies=list_of_cookies)

amazon.buy(product_url='product link')

amazon.select_payment_method(payment_method='Net Banking')

amazon.select_bank(bank='Axis Bank')

amazon.place_order()
