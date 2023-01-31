from __future__ import print_function
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

###############################################################################
# Creates a request to write data to the spreadsheet. Right now, this data    #
# is hardcoded.                                                               #
###############################################################################

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

    #create list of values we want to append, for now these are hard-coded.
    append_values = [[1, "01/31/23", 9, 10, 2, 3, 4, 8, 6, 4, 12, 13, "yo"]]

    # make the request to append data to the spreadsheet, we use 'append'
    # because we want it to write the data to the next available row
    # in the specified sheet/range
    request = service.spreadsheets().values().append(spreadsheetId=SPREADSHEET_ID,
                                                     range="TrackerTest!A1:M1",
                                                     valueInputOption="USER_ENTERED",
                                                     insertDataOption="INSERT_ROWS",
                                                     body={"values": append_values}).execute()
    # print the output of the request
    print(request)
except HttpError as err:
    # if there's an error, print it
    print(err)