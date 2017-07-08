import requests
import sys
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
    parser(response)

def parser(response):
    hitn = response.json()["hits"]["total"]

    for i in range(hitn):
        print(response.json()["hits"]["hits"][i]["_source"]["@timestamp"])
        print(response.json()["hits"]["hits"][i]["_source"]["event_data"]["Image"])
        print(response.json()["hits"]["hits"][i]["_source"]["event_data"]["ImageLoaded"])
        print("")


if __name__ == "__main__":
    sendrest(sys.argv[1:])
