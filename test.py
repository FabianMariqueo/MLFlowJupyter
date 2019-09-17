import requests

url = "http://localhost:1234/invocations"

payload = "{\n\t\"data\":[\n\t\t\t[7.4,\t0.70,\t0.00,\t1.9,\t0.076,\t11.0,\t34.0,\t0.9978,\t3.51,\t0.56,\t9.4\t]\n\t\t]\n\t\t\n\t\n}"
headers = {
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.16.3",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "de8edae4-8657-4104-b6e8-67d5501ed2e4,eec9b3da-fe6b-4959-bd0c-24da5505d07c",
    'Host': "localhost:1234",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "93",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)