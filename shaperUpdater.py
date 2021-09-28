#!/usr/bin/env python3
from time import sleep
#from apiKey import key
import sys
import requests
from requests.auth import HTTPBasicAuth
import urllib3
import json
urllib3.disable_warnings()

#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#head = {'apiKey' : 'KX55MEJ8DLXN3DVCRVTE', 'Content-Type' :'application/json;charset=UTF-8'}
url = "https://nxvw9ddm19.execute-api.ap-southeast-2.amazonaws.com/dev/currentBandwidth"
head = {"x-api-key" : 'KX55MEJ8DLXN3DVCRVTE'}
#access_token = 'KX55MEJ8DLXN3DVCRVTE'
#head = {'Authorization':'Bearer {access_token}'}
def read_bandwith():
    print ("Function one")
    print ("Connecting to API")
    response = requests.get(url,headers=head, verify=False)
    print ("Connected successfully " +str(response.status_code))
    print ("Reading the current bandwidth")
    if response.status_code == 200:
        print(response.text)
        resp_dict = json.loads(response.text)
        for key in resp_dict:
            print (key, ":", resp_dict[key])


def main():
    #print ("Hello World")
    read_bandwith()


if __name__ == "__main__":
    main()
