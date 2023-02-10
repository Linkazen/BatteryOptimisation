import smtplib, ssl
import json
import datetime
from dateutil import parser
from SensitiveData import *

message = f"Subject: Tariff Prices\n\nDate: {(datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%m/%d')}\n\n"

smtp_server = "smtp.gmail.com"
port = 465

context = ssl.create_default_context()

"""
This will format the message to be sent
so that it will be human readable and easy
to copy paste for the client
"""
def formatEmail():
    with open("InverterInfo/Tariffs.json") as TariffPrices:
        TariffData = json.loads(TariffPrices.read())

        Prices = TariffData["results"]

        Prices = list(filter(lambda Obj : parser.parse(Obj["valid_from"], ignoretz=True) >= datetime.datetime.now().replace(hour=23, minute=0, second=0, microsecond=0), Prices))

        Prices.reverse()

        global message
        for price in Prices:
            message += f'Price (inc vat): {price["value_inc_vat"]}\r\nPeriod: {parser.parse(price["valid_from"]).strftime("%H:%M")}-{parser.parse(price["valid_to"]).strftime("%H:%M")}\r\n\r\n'
        

formatEmail()

print(message)

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(email_sender, password)
    server.sendmail(email_sender, email_receiver, message)

