import http.client

conn = http.client.HTTPSConnection("loteriascaixa-api.herokuapp.com")
payload = ''
headers = {}
conn.request("GET", "/api/lotofacil/latest", payload, headers)
res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
