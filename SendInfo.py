import smtplib, ssl
import json
import datetime
import pytz
from dateutil import parser
from pytz import timezone
from SensitiveData import *

message = f"Subject: Tariff Prices\n\nDate: {(datetime.datetime.now()).strftime('%m/%d')}\n\n"

smtp_server = "smtp.gmail.com"
port = 465

tz = timezone("Europe/London")

context = ssl.create_default_context()

"""
This will format the message to be sent
so that it will be human readable and easy
to copy paste for the client
"""
def formatEmail():
    with open("/home/pi/BatteryOptimisation/InverterInfo/Tariffs.json") as TariffPrices:
        PriceToCompare = 0
        TariffData = json.loads(TariffPrices.read())

        # Prices are a list of prices after a certain time
        Prices = TariffData["results"]

        # Converts all times valid to/from into date objects in the timezone
        for price in Prices:
            price["valid_from"] = parser.parse(price["valid_from"]).astimezone(tz)
            price["valid_to"] = parser.parse(price["valid_to"]).astimezone(tz)
        
        if Prices[0]["valid_from"].day != datetime.datetime.now().day:
            PriceToCompare = datetime.datetime.now().replace(hour=23, minute=0, second=0, microsecond=0).astimezone(tz)
        else:
            PriceToCompare = datetime.datetime.now().replace(day=(datetime.datetime.now().day - 1),hour=23, minute=0, second=0, microsecond=0).astimezone(tz)

        Prices = list(filter(lambda Obj : Obj["valid_from"] >= PriceToCompare, Prices))

        Prices.reverse()

        global message
        for price in Prices:
            if datetime.time(0,0) == price["valid_from"].time():
                message += f"Date: {(datetime.datetime.now() + datetime.timedelta(days=1)).strftime('%m/%d')} \r\n\r\n"
            
            message += f'Price (inc vat): {price["value_inc_vat"]}\r\nPeriod: {price["valid_from"].strftime("%H:%M")}-{price["valid_to"].strftime("%H:%M")}\r\n\r\n'

formatEmail()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    # Sends an email to the list of people in the email_reciever array
    server.login(email_sender, password)
    server.sendmail(email_sender, email_receiver, message)