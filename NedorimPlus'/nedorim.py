from datetime import datetime
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import requests
import pandas as pd
import math
from services import donor_service

# from models.models import DonorsBase
# from models.donor_schema import DonorSchema
from passwords import MosadId, ApiPassword
import json

baseUrl = "https://matara.pro/nedarimplus/Reports/Manage3.aspx?"


def get_donations_csv():
    url = (
        baseUrl
        + "Action=GetTormimCsv&MosadNumber="
        + MosadId
        + "&ApiPassword="
        + ApiPassword
        + "&ToMail=0"
    )
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        content_type = response.headers.get("Content-Type")
        print(content_type)
        with open("output2.xlsx", "wb") as file:
            file.write(response.content)
        print("The CSV file was saved successfully as 'output.csv'")
        df = pd.read_csv("output.csv", encoding="ISO-8859-1", engine="python")
        df.to_excel("output_file.xlsx", index=False, engine="openpyxl")
        # csv_data = response.content.decode('ISO-8859-1')
        # df = pd.read_csv(io.StringIO(csv_data))
        # print(df)
    else:
        return {
            "error": "Failed to retrieve donations",
            "status_code": response.status_code,
        }


def get_keva_json():
    url = (
        baseUrl
        + "Action=GetKevaJson&MosadId="
        + MosadId
        + "&ApiPassword="
        + ApiPassword
    )
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        results = response.json()
        # print(results)
        return results
    else:
        return {
            "error": "Failed to retrieve donations",
            "status_code": response.status_code,
        }


def get_keva_id_json(KevaId):
    print(KevaId)
    url = (
        baseUrl
        + "Action=GetKevaId&MosadId="
        + MosadId
        + "&ApiPassword="
        + ApiPassword
        + "&KevaId"
        + KevaId
    )
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        results = response.json()
        print(results)
        return results
    else:
        return {
            "error": "Failed to retrieve donations",
            "status_code": response.status_code,
        }


def get_keva_csv():
    url = (
        baseUrl
        + "Action=GetKevaCSV&MosadNumber="
        + MosadId
        + "&ApiPassword="
        + ApiPassword
        + "&ToMail=0"
    )
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        with open("output.csv", "wb") as file:
            file.write(response.content)
        print("The CSV file was saved successfully as 'output.csv'")
    else:
        return {
            "error": "Failed to retrieve donations",
            "status_code": response.status_code,
        }


def get_history_json(lastId=None):
    url = (
        baseUrl
        + "Action=GetHistoryJson&MosadId="
        + MosadId
        + "&ApiPassword="
        + ApiPassword
        + "&LastId="
        + lastId
    )
    response = requests.get(url)
    # print(response.status_code)
    # print(response.status_code)
    if response.status_code == 200:
        file_name = "outputt.json"
        results = response.json()
        return results
        # print(len(results))
        # with open(file_name, "r", encoding="utf-8") as file:
        #     data = json.load(file)
        # data.extend(results)
        # with open(file_name, "w", encoding="utf-8") as file:
        #     json.dump(data, file, ensure_ascii=False, indent=4)
    else:
        return {
            "error": "Failed to retrieve donations",
            "status_code": response.status_code,
        }


def get_history_csv():
    url = (
        baseUrl
        + "Action=GetHistoryCSV&MosadNumber="
        + MosadId
        + "&ApiPassword="
        + ApiPassword
        + "From=22/11/2016"
    )
    response = requests.get(url)
    # print(response.status_code)
    if response.status_code == 200:
        with open("history.csv", "wb") as file:
            file.write(response.content)
        print("The CSV file was saved successfully as 'output.csv'")
    else:
        return {
            "error": "Failed to retrieve donations",
            "status_code": response.status_code,
        }


def map_json_into_table():
    with open("outputt.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    for row in data:
        if row["TransactionType"] in ["רגיל", "תשלומים"]:
            donation = {
                "Zeout": row.get("Zeout", None),
                "ClientName": row.get("ClientName", None),
                "Adresse": row.get("Adresse"),
                "Phone": row.get("Phone"),
                "Mail": row.get("Mail"),
                "Amount": row.get("Amount"),
                "Currency": row.get("Currency"),
                "TransactionTime": row.get("TransactionTime"),
                "LastNum": row.get("LastNum"),
                "TransactionType": row.get("TransactionType"),
                "Groupe": row.get("Groupe"),
                "Comments": row.get("Comments"),
                "Tashloumim": row.get("Tashloumim"),
                "FirstTashloum": row.get("FirstTashloum"),
                "NextTashloum": row.get("NextTashloum"),
                "TransactionId": row.get("TransactionId"),
                "KevaId": row.get("KevaId"),
            }


def add_donors_to_db():
    df = pd.read_csv(
        "output2.csv", encoding="utf-16", delimiter="\t", skiprows=range(1, 11)
    )
    columns_mapping = {
        "מספר זהות": "id",
        "שם משפחה": "last name",
        "שם פרטי": "first name",
        "כתובת": "address",
        "עיר": "city",
        "טלפון 1": "phone 1",
        "טלפון 2": "phone 2",
        "טלפון 3": "phone 3",
        "אימייל": "email",
        "הערות": "notes",
        "תואר": "title",
        "פרטי": "personal",
        "משפחה": "family",
        "איחול": "greeting",
        "שדה 5": "field 5",
        "שדה 6": "field 6",
        "שדה 7": "field 7",
        "שדה 8": "field 8",
        "סך נדרים": "total commitments",
        "מספר אישי בעסקים": "business personal number",
        "רשום בעמדות": "registered at stations",
    }

    # שינוי שם הטורים באמצעות המיפוי
    # print(df.columns)
    df.rename(columns=columns_mapping, inplace=True)
    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = (
                df[column]
                .str.replace('="', "", regex=False)
                .str.replace('"', "", regex=False)
            )
    # print(df["city"])
    columns_to_string = [
        "last name",
        "first name",
        "address",
        "city",
        "phone 1",
        "phone 2",
        "phone 3",
        "email",
        "notes",
        "title",
        "personal",
        "family",
        "greeting",
        "field 5",
        "field 6",
        "field 7",
        "field 8",
        "business personal number",
        "registered at stations",
    ]
    df[columns_to_string] = df[columns_to_string].astype(str)

    df["total commitments"] = pd.to_numeric(
        df["total commitments"], errors="coerce"
    ).fillna(0.0)
    for index, row in df.iterrows():
        donor = {
            "zeout": row["id"],
            "name": f"{row.get('first name', '')} {row.get('last name', '')}".strip(),
            "address": row.get("address"),
            "city": row.get("city"),
            "phone": row.get("phone 1"),
            "husband_phone": row.get("phone 2"),
            "wife_phone": row.get("phone 3"),
            "mail": row.get("email"),
            "bank": None,
            "brunch": None,
            "account_num": None,
            "source_of_details": "נדרים",
        }
        donor_service.create_new_donor(donor)
        # print("the obj add in success", donor)


def keva_json():
    # data = get_keva_json()
    # with open(file_name, "w", encoding="utf-8") as file:
    #     json.dump(data, file, ensure_ascii=False, indent=4)
    file_name = "output.json"
    with open(file_name, "r", encoding="utf-8") as file:
        loaded_data = json.load(file)
    for row in loaded_data:
        tz = row.get("Zeout", "")
        donor = donor_service.get_donors_by_tz(tz)
        balance_of_charges = row.get("Itra", "")

        if balance_of_charges == "":
            balance_of_charges = None
        else:
            balance_of_charges = int(balance_of_charges)

        created_date = datetime.strptime(
            row.get("CreationDate", ""), "%d/%m/%Y %H:%M:%S"
        )
        next_charge = datetime.strptime(row.get("NextDate", ""), "%d/%m/%Y %H:%M:%S")
        if donor:
            keva_donation = {
                "donors_id": donor[0].id,
                "status": row.get("Enabled", "0") == "1",
                "monthly_amount": float(row.get("Amount", 0)),
                "currency": row.get("Currency", ""),
                "category": row.get("Groupe", ""),
                "notes": "",
                "balance_of_charges": balance_of_charges,
                "were_carried_out": int(row.get("Success", 0)),
                "next_charge": next_charge.strftime("%d/%m/%Y"),
                "error": row.get("ErrorText", ""),
                "validity": row.get("Tokef", ""),
                "last_4_digits": row.get("LastNum", ""),
                "creationDate": created_date.strftime("%d/%m/%Y"),
            }

            donor_service.add_keva_donation(keva_donation)


def keva():
    df = pd.read_csv("output.csv", encoding="utf-16", delimiter="\t")
    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = (
                df[column]
                .str.replace('="', "", regex=False)
                .str.replace('"', "", regex=False)
            )
    columns_mapping = {
        "מספר הוראה": "instruction number",
        "סטטוס": "status",
        "שם": "name",
        "ת.ז": "zeout",
        "כתובת": "address",
        "עיר": "city",
        "טלפון": "phone",
        "מייל": "email",
        "סכום חודשי": "monthly amount",
        "קטגוריה": "category",
        "הערות": "notes",
        "יתרת חיובים": "outstanding balance",
        "בוצעו": "executed",
        "חיוב הבא": "next charge",
        "שגיאה": "error",
        "תוקף": "expiration",
        "4 ספרות אחרונות": "last 4 digits",
        "הוקם בעמדה": "created at position",
        "תאריך הקמה": "creation date",
        "מספר אישי": "personal number",
        "צפי לתשלום 12 חוד'": "expected payment (12 months)",
        "צפי לתשלום 36 חוד'": "expected payment (36 months)",
    }
    df.rename(columns=columns_mapping, inplace=True)
    print(df.columns)

    print(df.head())


def get_donations():
    file_name = "outputt.json"
    with open(file_name, "r", encoding="utf-8") as file:
        loaded_data = json.load(file)
    donations_data = [
        transaction
        for transaction in loaded_data
        if transaction["TransactionType"] != 'הו"ק'
    ]
    new_file_name = "filtered_donations.json"
    with open(new_file_name, "w", encoding="utf-8") as new_file:
        json.dump(donations_data, new_file, ensure_ascii=False, indent=4)

    print(f"Data has been written to {new_file_name}")


def add_donations_to_db():
    # anonymous=False
    # anonymous=False
    file_name = "filtered_donations.json"
    with open(file_name, "r", encoding="utf-8") as file:
        loaded_data = json.load(file)
        for donation in loaded_data:
            if donation.get("Zeout") == "" or donation.get("first_name") == "":
                pass
            else:
                donor = donor_service.get_donors_by_tz(donation.get("Zeout"))
                currency = "שקל" if donation.get("Currency") == "1" else "דולר"
                if donor == []:

                    new_donor = {
                        "zeout": donation.get("Zeout"),
                        "name": f"{donation.get('LastName', '')} {donation.get('FirstName', '')}".strip(),
                        "address": donation.get("Adresse"),
                        "city": "",
                        "phone": donation.get("Phone"),
                        "husband_phone": donation.get("Phone2"),
                        "wife_phone": "",
                        "mail": donation.get("Mail"),
                        "bank": None,
                        "brunch": None,
                        "account_num": None,
                        "source_of_details": "נדרים",
                    }

                    donor_service.create_new_donor(new_donor)
                    donor = donor_service.get_donors_by_tz(new_donor["zeout"])
                    
            donation_data = {
                "donors_id": donor[0].id,
                "amount": float(donation.get("Amount", 0)),
                "currency": currency,
                "transactionTime": (
                    datetime.strptime(
                        donation.get("TransactionTime", ""), "%d/%m/%Y %H:%M:%S"
                    ).strftime("%d/%m/%Y")
                    if donation.get("TransactionTime")
                    else None
                ),
                "lastNum": donation.get("LastNum", ""),
                "transactionType": donation.get("TransactionType", ""),
                "groupe": donation.get("Groupe", ""),
                "tashloumim": int(donation.get("Tashloumim", 0)),
                "firstTashloum": (
                    float(donation.get("FirstTashloum", 0))
                    if donation.get("FirstTashloum")
                    else None
                ),
                "nextTashloum": (
                    float(donation.get("NextTashloum", 0))
                    if donation.get("NextTashloum")
                    else None
                ),
                # "transactionId": donation.get("TransactionId", ""),
                "source": "נדרים",
            }
            donor_service.add_donation(donation_data)


# def add_anonymous_donations():
#     donation_data = {
#         "donors_id": 0,
#         "amount":0,
#         "currency": int(donation.get("Currency", 0)),
#         "transactionTime": datetime.strptime(donation.get("TransactionTime", ""), "%d/%m/%Y %H:%M:%S") if donation.get("TransactionTime") else None,
#         "lastNum": donation.get("LastNum", ""),
#         "transactionType": donation.get("TransactionType", ""),
#         "groupe": donation.get("Groupe", ""),
#         "comments": "תרומות אנונימיות",
#         "tashloumim": 0,
#         "firstTashloum": None,
#         "nextTashloum": None,
#         "transactionId": None,
#             }

#     print(df.head())


# get_donations_csv()
# get_keva_json()
# get_keva_id_json('1116674 ')
# get_keva_csv()
# get_history_json()
# get_history_csv()
# add_donors_to_db()
# keva_json()
# get_history_json()
# get_donations()
add_donations_to_db()
