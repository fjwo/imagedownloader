from asyncio import subprocess
import requests 

def print_banner(title="") :
    subprocess.call("clear")

web=input("Paste your website link:")
r = requests.get(web)

print(r.content)
with open("output.png", "wb") as f:
    f.write(r.content)
