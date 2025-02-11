
from datetime import datetime
import json
import os
import sys
import requests

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services import donor_service

# from services import donor_service


baseURL="https://kesherhk.info/ConnectToKesher/ConnectToKesher"

def get_trans_json():
    # Get all transactions for a company
    body={
        "userName": "2180378WS1195",
        "password": "l4WBZfAbFmjD1ZOFdZoGe1SzPOlSof3BAltuPgMekYI2bOIsQE",
        "func": "GetTrans",
        "format": "json",
        "fromDate": "2024/08/11",
        "toDate": "2025/01/13"
    }
        
    try:
        # שליחת הבקשה
        response = requests.post(baseURL, json=body)   
        # בדיקת סטטוס הבקשה
        if response.status_code == 200:
            # החזרת המידע במידה והבקשה הצליחה
            return response.json()
        else:
            # טיפול בשגיאות
            print(f"Error: {response.status_code}")
            print(response.text)
            return None
    except requests.exceptions.RequestException as e:
        # טיפול בחריגות
        print(f"Request failed: {e}")
        return None
    
def save_to_json_file(data, filename):
    # שמירה של הנתונים בקובץ JSON
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Data successfully saved to {filename}")
    except IOError as e:
        print(f"Failed to save data to {filename}: {e}")
        
def add_donations_to_db():
    anonymous=False
    file_name = "transactions.json"
    with open(file_name, "r", encoding="utf-8") as file:
        loaded_data = json.load(file)
        for donation in loaded_data: 
            if donation.get("Tz")=="" or donation.get("FirstName")=="":
                # anonymous=True
                pass
            else:                
                donor=donor_service.get_donors_by_tz(donation.get("Tz"))
                if donor==[]:
                    address = " ".join(part for part in [donation.get("Address"), donation.get("ApartmentNumber")]if part)
                    new_donor={
                        "zeout": donation.get("Tz"),
                        "last_name":donation.get("LastName"),
                        "first_name": donation.get("FirstName"),
                        "address":address ,
                        "city":donation.get("City") or "", 
                        "phone": donation.get("Phone"),
                        "husband_phone": donation.get("Phone2"),
                        "wife_phone": "",
                        "mail": donation.get("Mail"),
                    }
                    donor_service.create_new_donor(new_donor)  
                    donor=donor_service.get_donors_by_tz(new_donor["zeout"])              
            donation_data = {
                    "donors_id":donor[0].id,
                    "source":"קהילות",
                    "amount": float(donation.get("Total", 0))/100,
                    "currency": donation.get("Currency", ""),
                    "transactionTime": datetime.fromisoformat(donation.get("TranDate", "").replace("Z", "+00:00")) if donation.get("TranDate") else None,
                    "lastNum":donation.get("NumCard")[-4:] ,
                    "transactionType": donation.get("CreditType", ""),
                    "groupe": donation.get("Comment", ""),
                    "tashloumim": donation.get("NumPayments", 0),
                    "firstTashloum": float(donation.get("FirstPayment", 0)) if donation.get("FirstPayment") else None,
                    "nextTashloum": float(donation.get("MonthPayment", 0)) if donation.get("MonthPayment") else None,
                }
            donor_service.add_donation(donation_data)             
# transactions = get_trans_json()
# if transactions:
#     save_to_json_file(transactions, "transactions.json")
add_donations_to_db()