import requests
def upload():
    """KYC2上传文件"""
    proxies={"http":None,"https":None}
    url='https://api.onfido.com/v3/documents'
    requests.get(url,proxies=proxies)
    header={"authorization":"Bearer eyJhbGciOiJFUzUxMiJ9.eyJleHAiOjE2NzU0MjA4MjksInBheWxvYWQiOnsiYXBwIjoiY2ZlY2ZiN2ItNjk0OC00ZGUyLWExMDMtZTg0NDM2MjU3ZWE5IiwiY2xpZW50X3V1aWQiOiI4NzE1NDg5Yi0yNWI1LTRhM2EtYTE4OS03NzRmNzkzNGE0NDUiLCJpc19zYW5kYm94Ijp0cnVlLCJpc190cmlhbCI6ZmFsc2UsInJlZiI6Imh0dHBzOi8vZGV2Lm1hbW9ydWNyeXB0by5pby8qIiwic2FyZGluZV9zZXNzaW9uIjoiZjg3MGUxMWEtOGIxOS00YTI3LTgzYmUtY2VkM2E0ZDc3Y2RlIn0sInV1aWQiOiJwbGF0Zm9ybV9zdGF0aWNfYXBpX3Rva2VuX3V1aWQiLCJ1cmxzIjp7ImRldGVjdF9kb2N1bWVudF91cmwiOiJodHRwczovL3Nkay5vbmZpZG8uY29tIiwic3luY191cmwiOiJodHRwczovL3N5bmMub25maWRvLmNvbSIsImhvc3RlZF9zZGtfdXJsIjoiaHR0cHM6Ly9pZC5vbmZpZG8uY29tIiwiYXV0aF91cmwiOiJodHRwczovL2FwaS5vbmZpZG8uY29tIiwib25maWRvX2FwaV91cmwiOiJodHRwczovL2FwaS5vbmZpZG8uY29tIiwidGVsZXBob255X3VybCI6Imh0dHBzOi8vYXBpLm9uZmlkby5jb20ifX0.MIGIAkIBmhVuhQQzF8FUmOoI1DywC-Q14wjNXOk1aUeL_1j2wck7OG6buyGXpgG9SYALI009VxfQOfWMa_XRwbFk7aE-QkACQgHhaAO8MlwNzw0aVPVT7BCgF2lxRJlBqIS2xuo6tqP3V6Ps86K8cNhT5C0bY7DXFybsmOB2mYcJzbF_U2PmJ6hOVw","content-type":"multipart/form-data"}
    files={"file":('IDcard1.jpg',open("C:/Users/shawn.xiao/Pictures/e54765c472346a43645654952f5ce56.jpg","rb"),"multipart/form-data")}
    data={"type":"national_identity_card","issuing_country":"CHN"}
    res=requests.post(url=url,headers=header,files=files,params=data)
    print(res.status_code,res.text)

print(upload())