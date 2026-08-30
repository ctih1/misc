import dns.resolver
from dns.resolver import Answer, NoNameservers
import time
import requests

last_ip: str = ""

while True:
    try:
        ans: Answer = dns.resolver.resolve("ddns.koti.frii.site", "A")
        if len(ans) >= 1:
            ip = str(ans[0])

            if ip != last_ip:
                print(f"New IP {ip}")
                requests.post("https://discord.com/api/webhooks/nothingtoseehere", json={
                    "content": f"New IP `{ip}`"
                })
            last_ip = ip
        else:
            print("Failed to get answer.")
            print(ans)
    except NoNameservers:
        pass
    time.sleep(600)
