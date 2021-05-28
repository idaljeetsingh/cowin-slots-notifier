"""
    Script  : constants.py
    Author  : Daljeet Singh Chhabra
"""


TOKEN = "ACCESS TOKEN GOES HERE"
MONITOR = {
    "PIN CODE GOES HERE": [
        "YOUR TELEGRAM CHAT ID GOES HERE"
    ]
}

TELEGRAM_API_URL = "https://api.telegram.org/bot{}/".format(TOKEN)
COWIN_API_URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={}&date={}"
BREAK_TIME = 50
