import httplib, urllib, base64, json

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': '750cc2f2c6fe4633a2ace4e9d7335867',
}

params = urllib.urlencode({
    # Request parameters
    # 'start': '{string}',
    # 'top': '1000',
})

try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("GET", "/face/v1.0/persongroups/users/persons?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print (data);
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
