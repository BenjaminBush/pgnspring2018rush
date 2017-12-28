import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open('creds.json'))
scope = ['https://spreadsheets.google.com/feeds']
credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope) # get email and key from creds

file = gspread.authorize(credentials) # authenticate with Google
sheet = file.open("dbtest").sheet1 # open sheet
values = [u'Ben', u'Bush', u'ben.bush@wustl.edu', u'437178', u'3106584359', u'Senior', u'School of Engineering and Applied Sciences', u'Test']
sheet.append_row(values)