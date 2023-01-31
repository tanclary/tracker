from __future__ import print_function
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# We want to use the sheets API, and we have our credentials that basically say
# "Hey you can read/write from/to this spreadhseet"
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'credentials.json'

#Credentials
creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Spreadsheet ID
SPREADSHEET_ID = '1-YyaXWPFTFYzaIdT1Ot3WL1uG2k1xQykmCSItOy5zag'

# this block of code is wrapped in a try/except block so that if the call fails,
# it will print an error and we can see the error.
try:
    #construct our service that is going to make the API call for us
    service = build('sheets', 'v4', credentials=creds)

    # get the sheets service
    sheet = service.spreadsheets()

    #this makes the actual call that 'gets' the datat from our sheets. It
    # knows what to get because we give it our unique sheet ID and the range
    # we want to retrieve.
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range="Data!A2:M39").execute()

    #get the values returned from our call
    values = result.get('values', [])

    #print these results
    print(values)
except HttpError as err:
    #if there's an error, print it
    print(err)