# stock-trading-notification-alert

sends you an sms when the stock price of the company that you want goes above or below a certain percentage(which you can set).

![Screenshot](https://user-images.githubusercontent.com/84438200/149450102-c1e4c08e-aeb2-4926-a19f-853afb88177c.jpg)

## HOW TO USE THE SCIRPT

1. Go to [Alphavantage.co](https://www.alphavantage.co/) and get your free api key and paste that key on line 10 in `main.py`
2. Go to [newsapi.org](https://newsapi.org/) and get your api key and paste it on line 12 in `main.py`
3. Go to [twilio.com](https://www.twilio.com/) and sign up to get your ACCOUNT_SID, AUTH_TOKEN, TRIAL_NUMBER.
4. Paste these 3 things on lines 15, 16, 17 respectively in `main.py`.
5. Enter your current phone number which you used while signing up for twilio on line 20 

### if you want to receive sms alerts on a different phone number you'll need to verify it with twilio first you can do that by going to your twilio dashboard and clicking on verified numbers and adding your phone number(otp will be sent for verification)

![image](https://user-images.githubusercontent.com/84438200/149449903-6a7fb89a-a12c-4d4b-87bd-cc63ba6ad080.png)

### if you want to change the percentage of increase/decrease of the stock (default is 1) you can do that by changing the number on line 52 in the `if statement`
![image](https://user-images.githubusercontent.com/84438200/149450361-670fbcfc-fd8b-4031-8cf4-33a1a5d9a88c.png)
