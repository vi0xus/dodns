#!/usr/bin/python
import json
import requests

url = 'https://api.digitalocean.com/v2/domains/DOMAIN.COM/records/DNSRECORDID'
auth = 'Bearer YOURAUTHTOKEN'

def getExternalIp():
        r = requests.get('http://ip.tr3nx.net/')
        return r.text

def getExistingIp():
        headers = {
                'Content-Type': 'application/json',
                'Authorization': auth
        }
        r = requests.get(url, headers=headers)
        return r.json()['domain_record']['data']

def updateIp(newip):
        headers = {
                'Content-Type': 'application/json',
                'Authorization': auth
        }
        data = {
                'data': newip
        }
        r = requests.put(url, headers=headers, data=json.dumps(data))
        return r.json()

existingIp = getExistingIp()
externalIp = getExternalIp()

if (externalIp <> existingIp):
        print "External ip: " + externalIp
        print "Existing ip: " + existingIp
        print "Updating dns record..."
        updateIp(externalIp)
        print "External ip: " + externalIp
        print "Existing ip: " + getExistingIp()

print "DNS up to date. [" + externalIp + "] -> [" + existingIp + "]"