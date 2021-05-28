"""
    Script  : main.py
    Author  : Daljeet Singh Chhabra
"""

import time
import datetime
import urllib.parse
import requests

from constants import *


def send_message(text, chat_id):
    text = urllib.parse.quote_plus(text)
    url = TELEGRAM_API_URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text, chat_id)
    resp = requests.get(url)
    if resp.status_code == 200:
        print("Message Sent...")
    else:
        print("Unable to send message!")


def get_slots(pin_code):
    headers = {
        "accept": "text/html",
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Mobile Safari/537.36',
        "Accept-Language": "en-US"
    }
    today = datetime.datetime.today().strftime('%d-%m-%Y')
    tomorrow = (datetime.datetime.today() + datetime.timedelta(days=1)).strftime('%d-%m-%Y')
    da_tomorrow = (datetime.datetime.today() + datetime.timedelta(days=2)).strftime('%d-%m-%Y')

    slots = []

    for _date in (today, tomorrow, da_tomorrow):
        resp = requests.get(COWIN_API_URL.format(pin_code, _date), headers=headers)
        if resp.status_code == 200:
            centers = resp.json()
            for center in centers['sessions']:
                if center.get('available_capacity_dose1') > 0:
                    msg = f"Date: {_date} | Center: {center.get('name')} | Vaccine: {center.get('vaccine')} | " \
                          f"Available Dose1: {center.get('available_capacity_dose1')} | Capacity: {center.get('available_capacity')} "
                    slots.append(msg)

    if len(slots) > 0:
        return True, slots
    else:
        return False, slots


def main():
    while True:
        print("--{} ----- Getting updates".format(datetime.datetime.now()))

        if len(MONITOR) > 0:
            # Ping the CoWin API and check slots
            print("Pinging the CoWin API and checking slots...")
            pin_codes = MONITOR.keys()
            for code in pin_codes:
                telegram_users_chat_id = MONITOR[code]
                available, slots = get_slots(code)
                if available:
                    print('Slots available...')
                    msg = f'Hi, {len(slots)} slot(s) available in "{code}"\n~~~~~~~~~~~~~~~~~~~\nDetails:\n\n'
                    slots_text = "\n\n".join(slots)
                    msg += slots_text
                    msg += '\n\n~~~~~~~~~~~~~~~~~~~\n\nVisit https://selfregistration.cowin.gov.in/ to book ' \
                           'slot.\n\nThanks '

                    for chat_id in telegram_users_chat_id:
                        print(f'Sending message to {chat_id}...')
                        send_message(msg, chat_id)
                    time.sleep(BREAK_TIME)


if __name__ == '__main__':
    print('Starting the CoWin vaccine slot finder...')
    main()
