import bs4
import requests
import sys
import re
import json
import pprint

jsonstring = {
    "from": 0,
    "size":10000,
    "query": {
        "match": {
            "event_data.Image.keyword": {
                "query": "C:\\tools\\mimikatz_20150621\\x64\\mimikatz.exe",
            }
        }
    }
}
def sendrest(url):
    if len(sys.argv) != 2:
        sys.exit("Usage: %s eslasticsearch_address:Port" %sys.argv[0])

    path = 'http://' + url[0] + '/winlogbeat-*/_search?pretty=true'
    response = requests.get(path, data = json.dumps(jsonstring))
    print(json.dumps(jsonstring))
    pprint.pprint(response.json())



    # soup = bs4.BeautifulSoup(res.text,"lxml")
    # text = soup.title.string
    # sents = soup.find_all(['p','div','pre'])
    # for sent in sents:
	 #    text += sent.text
    #
    # text = re.sub('[\n\r\t]',' ',text)
    # text = re.sub(r'\ +',' ',text)
    # text = re.sub(r'\|',' ',text)
    # print(text)

if __name__ == "__main__":
    sendrest(sys.argv[1:])


#全ての時刻を集めて、そのバラツキをみればよさそう。それに加えてImageが同じものであること。