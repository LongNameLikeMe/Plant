import requests
import base64

#植物识别

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/plant"

f = open('./images/test1.jpg', 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = '24.90b680f3c09b56e80a5c96774be0e85f.2592000.1628004848.282335-24492982'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())