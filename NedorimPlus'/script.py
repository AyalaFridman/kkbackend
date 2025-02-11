import requests
import schedule
import time
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from db_config import object_manager
from models.models import Settings
from models.setting_schema import SettingSchema
import nedorim

def get_last_id():
    res = object_manager.get_objects(Settings, SettingSchema, filters=[Settings.key == "lastTransactionId"])
    return res[0].value
def save_last_id(last_id):
    update = {
        "key" : "lastTransactionId",
        "value" : last_id
    }
    object_manager.update_objects(Settings, SettingSchema, filters=[Settings.key == "lastTransactionId"], updates=update)

def send_request():
    print("in script")
    last_id = get_last_id()
    print(last_id)
    try:
        pass
        data = nedorim.get_history_json(last_id)
        print(len(data))
        if len(data) > 0:
            new_last_id = data[-1]["TransactionId"]
            print(new_last_id)
            save_last_id(new_last_id)
        
        print(f"Request successful: {data}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        

# Scheduling the script to run every 24 hours
# schedule.every(24).hours.do(send_request)
schedule.every(5).minutes.do(send_request)

print("Scheduler is running...")
while True:
    schedule.run_pending()
    time.sleep(1)
