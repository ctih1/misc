import os
from typing import List, Dict
import ipaddress
from ipaddress import IPv4Network, IPv6Network, IPv4Address, IPv6Address
import time
from tqdm import tqdm
from mapchartpy import Map
import re
import json
import colorsys

IpNetwork = IPv4Network | IPv6Network
IpAddress = IPv4Address | IPv6Address

Zone = str
ZONES: List[str] = os.listdir("zones")

def hsl_to_hex(hue, saturation, light) -> str:
    rgb = colorsys.hsv_to_rgb(hue/360,
                                saturation/100,
                                light)
    rgbhex = "".join("%02X" % round(i*255) for i in rgb)
    return rgbhex


blocks: Dict[Zone, List[IpNetwork]] = {}

start = time.time()
ips = []
with open("ips.txt", "r") as f:
    ips = [s.strip() for s in f.readlines()]

print(f"Loading IPs: {time.time() - start}")

start = time.time()
for zone in ZONES:
    zone_name: str = zone[:2]

    if zone_name not in blocks:
        blocks[zone_name] = []

    lines: List[str] = []
    with open(f"zones/{zone}", "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        blocks[zone_name].append(ipaddress.ip_network(line.strip()))

print(f"Loading zones: {time.time() - start}")

start = time.time()
countries: Dict[Zone, int] = {k:0 for k in list(blocks.keys())}

w_map = Map()
highest = 0

for ip in tqdm(ips):
    address: IpAddress = ipaddress.ip_address(ip)
    area: str | None = ""

    for zone, networks in blocks.items():
        for network in networks:
            if address in network:
                area = zone
                break
        if area:
            break
    area = area or "unknown"

    countries[area] += 1
    if countries[area] > highest:
        highest = countries[area]


for country, amount in countries.items():
    if amount > 0:
        print(f"{country}: {amount}")


country_codes = {}
with open("countries.json", "r") as f:
    country_codes = json.load(f)

for country, amount in countries.items():
    if amount == 0:
        continue

    real = country_codes.get(country.upper())
    if not real:
        print(f"Not find for {country}")
        continue

    real = real.replace(" ", "_")

    intens = amount / highest

    if real == "Czech_Republic":
        real = "Czechia"
    
    if real == "Russian_Federation":
        real = "Russia"

    if real == "Korea":
        real = "South_Korea"

    color = "#" + hsl_to_hex(286, 100, 0.85-((1-intens)*0.55))
    w_map.fill_country(real, color, f"{amount}")



with open("out.json", "w") as f:
    json.dump(w_map.get_file(), f)
