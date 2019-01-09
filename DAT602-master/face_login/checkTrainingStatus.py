#*****checkTrainingStatus.py*****#
import urllib, httplib, base64, json

group_id = 'users'
KEY = '750cc2f2c6fe4633a2ace4e9d7335867'

headers = {'Ocp-Apim-Subscription-Key': KEY}
params = urllib.urlencode({'personGroupId': group_id})
conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
conn.request("GET", "/face/v1.0/persongroups/"+group_id+"/training?%s" % params, "{body}", headers)
response = conn.getresponse()
data = json.loads(response.read())
print(data)
conn.close()
