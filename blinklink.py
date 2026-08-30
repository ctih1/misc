import hashlib
import requests
import base64
import sys
import tqdm

with open(r"osulazer.zip", "rb") as f:
    content = f.read()

api = "https://bin.blinkl.ink"

# Retrieve a challenge to solve (expiry varies on many factors)
challenge_response = requests.get(f"{api}/api/challenge").json()
challenge, diff = challenge_response["challenge"], challenge_response["difficulty"]

nonce = 0
while True:
    h = hashlib.sha256(f"{challenge}{nonce}".encode()).hexdigest()
    if h.startswith("0" * diff):
        break
    nonce += 1

print("Nonce done")

strang = base64.b64encode(content).decode("utf-8")
n = 150000
parts = [strang[i : i + n] for i in range(0, len(strang), n)]

details = []
print(len(parts))
for part in tqdm.tqdm(parts):
    r = requests.post(
        f"{api}/api/paste",
        json={
            "paste": "does this thing work" * 2048,
            "challenge": challenge,
            "nonce": nonce,
        },
        timeout=60000,
    )

    details.append(r.json())

print(details)
