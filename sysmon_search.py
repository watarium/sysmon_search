import requests
import sys
import json
import pandas as pd
import pprint

jsonstring = {
    "from": 0,
    "size":10000,
    "query": {
        "match": {
            "event_data.Image": {
                "query": "mimikatz.exe",
            }
        }
    }
}
def sendrest(url):
    if len(sys.argv) != 2:
        sys.exit("Usage: %s eslasticsearch_address:Port" %sys.argv[0])

    path = 'http://' + url[0] + '/winlogbeat-*/_search?pretty=true'
    response = requests.get(path, data = json.dumps(jsonstring))
    #print(json.dumps(jsonstring))
    #pprint.pprint(response.json())
    parser(response)

def parser(response):
    hitn = response.json()["hits"]["total"]
    eventlist = []

    for i in range(hitn):
        res_src = response.json()["hits"]["hits"][i]["_source"]
        eventdata = res_src["event_data"]["ProcessId"],res_src["@timestamp"],res_src["beat"]["name"],res_src["event_data"]["Image"],res_src["event_data"]["ImageLoaded"]
        taptolist = list(eventdata)
        eventlist.append(taptolist)
        #print(eventdata)
    pivot(eventlist)

def pivot(eventlist):
    eventdf = pd.DataFrame(eventlist)
    eventdf.columns = ["ProcessID","Time","Client","Image","ImageLoaded"]
    imagept = eventdf.pivot_table(index="ImageLoaded",columns="ProcessID",values="Time",aggfunc=lambda x: len(x),fill_value = 0)
    imagept.to_csv("imagept.csv")
    print(imagept)


if __name__ == "__main__":
    sendrest(sys.argv[1:])
