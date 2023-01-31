import requests
import google.auth

###############################################################################
# This is currently the 'main' file which is actually just reading the text   #
# from an image. Right now, this is just some meme I found on the internet.   #
###############################################################################
def detect_text(path):
    # url of the api we're using
    api_url = "https://api.ocr.space/parse/image"

    # info for the request we want to make, api key gives us access, url specifies what image we want to read
    json = {'apikey': 'K83018353188957', 'url':'https://media.sproutsocial.com/uploads/meme-example.jpg'}

    # we make our request with the api url and the associated info
    results = requests.post(api_url, json)

    # results are stored in JSON format
    jsonResults = results.json()

    # get the parsed results from the json
    parsedResults = jsonResults.get('ParsedResults')

    # get the actual text of these results (don't worry about this too much
    # the stuff want is just nested deep in the results
    parsedText = parsedResults[0].get('ParsedText')

    # finally, print the text. eventually we don't want to print, but it's a good start.
    print(parsedText)

    #############################
    # Current Output from this: #
    # "I DON'T THINK THAT MEMES #
    # WHAT YOU THINK IT MEMES"  #
    #############################

def update_values(spreadsheet_id, range_name, value_input_option, _values):
    creds, _ = google.auth.default()


# call our main method with the specified image, right now it's using a web-hosted image
# instead of a local file, so the "test.jpeg" parameter isn't doing anything.
detect_text("test.jpeg")