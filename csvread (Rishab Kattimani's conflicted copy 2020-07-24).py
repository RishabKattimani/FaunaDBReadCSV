#-------------------------------------------------------------------------------
# Imports
from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient
from csv import *
from datetime import datetime, date
import config as config
#-------------------------------------------------------------------------------
# Variables & Setup
client = FaunaClient(secret=config.secret) # Connection To Fauna

# ------------------------------------------------------------------------------
#  Reading CSV File
with open('data.csv', 'r') as read_obj:

    csv_reader = reader(read_obj)

#-------------------------------------------------------------------------------
# Getting Age
    for row in csv_reader:

        date_str = row[2]

        date_object = datetime.strptime(row[2], '%m/%d/%Y').date()

        today = date.today()

        age = (today.year - date_object.year)
#-------------------------------------------------------------------------------
# Age Groups
        if age >= 19 and age <= 60:
            AgeGroup  = "Adult"

        if age >= 60 and age <= 1000:
            AgeGroup  = "Senior"

        if age >= 9 and age <= 19:
            AgeGroup  = "Teen"

        if age >= 0 and age <= 9:
            AgeGroup  = "Child"
#-------------------------------------------------------------------------------
# Pushing Data To FaunaDB
        print (age, AgeGroup)

        client.query(
           q.create(
             q.collection("BollywoodActor"),
             {"data": {"Name": row[0], "Image": row[1], "DOB": row[2], "Age": age, "AgeGroup": AgeGroup}}
           ))
