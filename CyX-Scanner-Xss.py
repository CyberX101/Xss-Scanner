import requests
import os
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
os.system('clear')
#color 
red = '\033[31m'
green = '\033[32m'

CyX = (f'''{red}

   ___    __  __   ___                              __  __       
  / __|  _\ \/ /__/ __| __ __ _ _ _  _ _  ___ _ _ __\ \/ / ______
 | (_| || |>  <___\__ \/ _/ _` | ' \| ' \/ -_) '_|___>  < (_-<_-<
  \___\_, /_/\_\  |___/\__\__,_|_||_|_||_\___|_|    /_/\_\/__/__/
      |__/                                                       



{green} @CyberX10



''')
print(CyX)

def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")


def get_form_details(form):
    details = {}
    action = form.attrs.get("action", "").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details


def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    print(f"{green}[+] Submitting malicious payload to {target_url}")
    print(f"{green}[+] Data: {data}")
    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        # GET request
        return requests.get(target_url, params=data)


def CyX_Xss_Scanner(url):
   
    forms = get_all_forms(url)
    print(f"{red}[+] Detected {len(forms)} forms on {url}.")
    js_script = "<Script>alert('hi')</scripT>"
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"{red}[+] {green}XSS Detected on {url}")
            print(f"{red}[*] {green}Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable


if __name__ == "__main__":
    import sys
    url = input(f'{red}Enter Url Target : ')
    print(CyX_Xss_Scanner(url))
      
Cyx = input('Do you want to follow our channel on Telegram ? (y/n)')
if Cyx == 'y':
    webbrowser.open("https://t.me/CyX_Security")
elif Cyx == 'n':
    print('(#_#)')
    exit()
    



    



