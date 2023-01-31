import requests
import json
def detect_text(path):
    #url of the api we're using
    api_url = "https://api.ocr.space/parse/image"

    #info for the request we want to make, api key gives us access, url specifies what image we want to read
    json = {'apikey': 'K83018353188957', 'url':'https://media.sproutsocial.com/uploads/meme-example.jpg'}

    #we make our request with the api url and the associated info
    results = requests.post(api_url, json)

    #results are stored in JSON format
    json = results.json()

    #print out those results
    print(json)

# call our main method with the specified image, right now it's using a web-hosted image
# instead of a local file, so the "test.jpeg" parameter isn't doing anything.
detect_text("test.jpeg")