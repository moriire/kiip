import requests
import uuid
secret_key="FLWSECK_TEST-a20c409b11e3feffabd8cdfd1303700f-X"
endpoint="https://api.flutterwave.com/v3/payments"
GET, POST=requests.get, requests.post
headers={"Authorization":"Bearer "  +secret_key, "Content-Type": "application/json"}
r_url='google.com'
po_all={0: "account",
1: "card",
#2: "banktransfer",
#3: "mpesa",
#4: "mobilemoneyrwanda",
#5: "mobilemoneyzambia",
6: "qr",
#7: "mobilemoneyuganda",
8: "ussd",
#9: "credit",
#10: "barter",
#11: "mobilemoneyghana",
#12: "payattitude",
#13: "mobilemoneyfranco",
#14: "paga",
#15: "1voucher",
#16: "mobilemoneytanzania"
        }

class Transaction:
    headers=headers
    def __init__(self, redirect_url,payment_options=None, tx_ref=None, currency='NGN'):
        self.redirect_url=redirect_url
        self.currency=currency
        if payment_options==None: self.payment_options=list(po_all.values())
        else: self.payment_options
        if tx_ref==None: self.tx_ref=uuid.uuid4().hex
        else: tx_ref
    def s_charge(self, amount, **kwargs):
        """
        kwargs:
        amount(string): amount to be charged
        email(string, required): email address
        kwarg:
        first_name(string) --> Mo
        last_name(string) --> Riire
        phone(string) --> xxxxxxxx
        """
        data={'tx_ref':self.tx_ref, "amount": amount, 'payment_options':self.payment_options, 'currency':self.currency, 'customer': kwargs,  'redirect_url':self.redirect_url}
        request=POST(endpoint, headers=self.headers, json=data)
        response=request.json()
        return response['data']['link']
x=Transaction(r_url)
y=x.s_charge(1000, email='ibmabdulsalam@gmail.com')
print(y)
