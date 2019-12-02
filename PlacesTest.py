
import requests, json
from urllib import urlopen

def main():
    address = "tallahassee"
    api_key = 'AIzaSyABlmN66Scj0b9xr85WiduJPhigsMJoHy0'

    # url variable store url
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

    # The text string on which to search
    query = raw_input('Search query:')

    # get method of requests module
    # return response object
    r = requests.get(url + 'query=' + query +
                     '&key=' + api_key)

    # json method of response object convert
    #  json format data into python format data
    x = r.json()

    # now x contains list of nested dictionaries
    # we know dictionary contain key value pair
    # store the value of result key in variable y
    y = x['results']

    # keep looping upto length of y

    for i in range(len(y)):
        # Print value corresponding to the
        # 'name' key at the ith index of y
        print(y[i]['geometry']['location'])
        print(y[i]['name'])

        #address = y[i]['formatted_address']

       # url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + address
        #jsonurl = urlopen(url)

        #text = json.loads(jsonurl.read())
        #print (text['results'][0]["formatted_address"])
        #print (text['results'][0]["geometry"]['location']["lat"])
        #print (text['results'][0]["geometry"]['location']["lng"])



if __name__ == "__main__":
    main()
