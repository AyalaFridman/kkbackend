from fastapi import FastAPI, File, UploadFile, APIRouter
from fastapi.responses import JSONResponse
import pdfplumber
import io
import re
import pandas as pd
from io import BytesIO
from services import donor_service


router = APIRouter()


def extract_text_from_keyword(text, start_keyword, end_keyword):

    pattern = re.compile(
        f"{re.escape(start_keyword)}(.*?){re.escape(end_keyword)}", re.DOTALL
    )
    matches = pattern.findall(text)
    return matches


def add_data_to_db(new_data):
    donor_service.add_keva_donation(new_data)


def create_new_donor(new_donor):

    donor_id = (
        new_donor["column_7"][: new_donor["column_7"].find(":")]
        + new_donor["column_7"][new_donor["column_7"].rfind(":") :]
    )
    bank_details = new_donor["column_7"].split(":")
    donor = {
        "zeout": donor_id,
        "name": new_donor["column_6"],
        "city": "",
        "address": "",
        "phone": "",
        "husband_phone": "",
        "wife_phone": "",
        "mail": "",
        "bank": bank_details[0],
        "brunch": bank_details[1],
        "account_num": bank_details[2],
        "source_of_details": "בנק",
    }
    donor["name"] = donor["name"].replace("ð", "נ")
    donor["name"] = donor["name"][::-1]
    donor_service.create_new_donor(donor)


def create_new_donor_from_excel(new_donor):

    print("in created")

    donor_id = str(new_donor["Unnamed: 4"]) + ":" + str(new_donor["Unnamed: 6"])

    donor = {
        "zeout": donor_id,
        "name": new_donor["Unnamed: 3"],
        "city": "",
        "address": "",
        "phone": "",
        "husband_phone": "",
        "wife_phone": "",
        "mail": "",
        "bank": new_donor["Unnamed: 4"],
        "brunch": new_donor["Unnamed: 5"],
        "account_num": new_donor["Unnamed: 6"],
        "source_of_details": "בנק",
    }
    donor_service.create_new_donor(donor)
    return donor_id


@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        file_data = await file.read()

        with pdfplumber.open(io.BytesIO(file_data)) as pdf:
            for page in pdf.pages:
                all_text = page.extract_text()
                text = extract_text_from_keyword(all_text, "תויאקðב", ":רובע")
                dates = []
                for line in text:
                    date_pattern = r"\b\d{1,2}-\d{1,2}-\d{4}\b"

                    match = re.search(date_pattern, line)
                    dates.append(match.group().replace("-", "/"))

                tables = page.extract_tables()
                index = 0
                for table in tables:
                    row_data = {
                        f"column_{i+1}": cell for i, cell in enumerate(table[0])
                    }
                    if (
                        row_data["column_1"] == "ורתוð"
                        or row_data["column_1"] == "שדוחב םוי"
                    ):
                        continue

                    for row in table:
                        row_data = {f"column_{i+1}": cell for i, cell in enumerate(row)}
                        if row_data["column_1"] == "בויחל הרעה":
                            continue

                        if row_data["column_6"]:
                            donor_id = (
                                row_data["column_7"][: row_data["column_7"].find(":")]
                                + row_data["column_7"][
                                    row_data["column_7"].rfind(":") :
                                ]
                            )
                            donor = donor_service.get_donors_by_account(donor_id)
                            if donor == []:
                                create_new_donor(row_data)
                            donor = donor_service.get_donors_by_account(donor_id)
                            donor_keva = donor_service.get_donor_keva_by_id(donor[0].id)
                            print(donor_keva)
                            if donor_keva == []:
                                json_data = {
                                    "donors_id": donor[0].id,
                                    "status": True,
                                    "monthly_amount": row_data["column_3"],
                                    "currency": "שקל",
                                    "category": "עניי עירך",
                                    "notes": "",
                                    "balance_of_charges": None,
                                    "were_carried_out": 1,
                                    "next_charge": dates[index],
                                    "error": "",
                                    "validity": "",
                                    "last_4_digits": "",
                                    "creationDate": dates[index],
                                }

                                json_data["monthly_amount"] = float(
                                    json_data["monthly_amount"]
                                    .replace("₪", "")
                                    .replace(",", "")
                                )

                                add_data_to_db(json_data)

                            else:
                                donor_service.update_keva_donation(
                                    donor_keva[0].id,
                                    updates={
                                        "were_carried_out": (
                                            donor_keva[0].were_carried_out + 1
                                        )
                                    },
                                )
                    index += 1

        return {"text": "succsesful"}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@router.post("/upload-excel")
async def upload_excel(file: UploadFile = File(...)):

    contents = await file.read()
    df = pd.read_excel(BytesIO(contents), engine="xlrd")

    data = df.to_dict(orient="records")

    for line in data:

        if line["Unnamed: 1"] == "תאריך רישום":
            continue
        donor_id = str(line["Unnamed: 4"]) + ":" + str(line["Unnamed: 6"])
        donor = donor_service.get_donors_by_account(donor_id)
        if donor == []:
            create_new_donor_from_excel(line)
        donor = donor_service.get_donors_by_account(donor_id)
        json_data = {
            "donors_id": donor[0].id,
            "amount": line["Unnamed: 7"],
            "currency": "שקל",
            "transactionTime": line["Unnamed: 2"].strftime("%d/%m/%Y"),
            "lastNum": "",
            "transactionType": "רגיל",
            "groupe": "",
            "tashloumim": 1,
            "firstTashloum": line["Unnamed: 7"],
            "nextTashloum": 0,
            "source": "בנק",
        }
        donor_service.add_donation(json_data)
