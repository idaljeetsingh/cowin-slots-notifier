# CoWin Vaccine Slot Notifier

Get notification on Telegram as soon as slot is available for the entered pin-code

## Setup

Clone the repository and install requirements

```
$ git clone https://github.com/idaljeetsingh/cowin-slots-notifier
$ cd cowin-slots-notifier
$ pip install -r requirements.txt 
```

- Head over to Telegram's <a href="https://t.me/botfather">Bot Father</a> and create a bot for your account.
- Now go to <a href="https://t.me/myidbot">IDBot</a> and get the Chat ID of your account.

In the file `constants.py`, do the following:
- Paste the "Access Token" from BotFather & "Chat ID" from IDBot.
- Enter the city's pin-code that you want to track and paste the chat ID against it. 

## Using the script

Once all the setup is completed, simply run the python script main.py

````
python main.py
````
The script will check for slots every 50 seconds (configure "BREAK_TIME" in `constants.py`) and if slots for Dose1 are avaiable, it will send notification on Telegram. 

#### Note: There is a rate limit on using the api, configure the BREAK_TIME and pin-codes accordingly
