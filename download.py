import urllib.request
import os

urls = {
    'assets/images/clients/ramco-cements-logo.png': 'https://www.ramcocements.in/assets/img/ramco-logo.png',
    'assets/images/clients/ultratech-cement-logo.png': 'https://www.ultratechcement.com/content/dam/ultratechcement/logo/ultratech-brand-logo.png',
    'assets/images/clients/preethi-logo.png': 'https://www.preethi.in/images/logo.png'
}

req_headers = {
    'User-Agent': 'Mozilla/5.0'
}

for path, url in urls.items():
    try:
        req = urllib.request.Request(url, headers=req_headers)
        with urllib.request.urlopen(req) as response, open(path, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
            print(f"Downloaded {path} ({len(data)} bytes)")
    except Exception as e:
        print(f"Failed {path}: {e}")
