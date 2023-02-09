import smtplib, ssl
import json
from dateutil import parser
from datetime import datetime
from SensitiveData import *

smtp_server = "smtp.gmail.com"
port = 465

message = ""

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

        Prices = list(filter(lambda Obj : parser.parse(Obj["valid_from"], ignoretz=True) >= datetime.now().replace(hour=23, minute=0, second=0, microsecond=0), Prices))
        print(Prices)

# def SortPrices(PricesArr):
    

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(email_sender, password)
    server.sendmail(email_sender, email_receiver, message)

formatEmail()