# from models.model import allocation
# import requests
from DAL import donor_repo
from typing import List
from models.donor_schema import DonorSchema

def get_all_donors() -> List[DonorSchema]:

    result = donor_repo.get_all_donors()
    return result


def get_donors_by_id(id):
    return donor_repo.get_donors_by_id(id)


def get_donors_by_name(last_name: str, first_name: str = None):
    return donor_repo.get_donors_by_name(last_name, first_name)


def get_donors_by_tz(tz: str):
    return donor_repo.get_donor_by_tz(tz)


def get_donors_by_account(account: str):
    return donor_repo.get_donor_by_account(account)


def get_donor_keva_by_id(id: int):
    return donor_repo.get_donor_keva_by_id(id)


def get_donors_keva():
    return donor_repo.get_donors_keva()


def get_reg_donation():
    return donor_repo.get_reg_donation()


# def get_bank_donations() -> List[BankDonationSchema]:
#     return donor_repo.get_bank_donation()

# def get_donation_keva() -> List[KevaDonationSchema]:
#     return donor_repo.get_donation_keva()


def create_new_donor(new_donor: dict):
    donor = get_donors_by_tz(new_donor.zeout)
    if donor:
        return "יש כבר תורם עם מספר ת.ז זהה"
    return donor_repo.create_new_donor(new_donor)

def create_recepit(recepit: dict):
    api_key ="f1c85d16fc1acd369a93f0489f4615d93371632d97a9b0a197de6d4dc0da51bf"
    api_email = "k1800800530@gmail.com"
    developer_email = "ayalafridman2870@gmail.com"
    urlRecepit = 'https://demo.ezcount.co.il/api/createDoc'
    paymentObj = [
    {
        "payment_type": recepit.payment[0].payment_type,
        "payment_sum": recepit.payment[0].payment_sum,
        "comment":recepit.payment[0].comment
    } 
    # for payment in recepit.payment if payment is not None
    ]
    # for i, payment in enumerate(recepit.payment):
    #     print(payment.checks_number)
    #     if payment.payment_type == 4:
    #         paymentObj[i]["checks_number"] = payment.checks_number
    #         paymentObj[i]["bt_bank_branch"] = payment.bt_bank_branch
    #         paymentObj[i]["bt_bank_account"] = payment.bt_bank_account

    payload = {
      "api_key": api_key,
      "developer_email":developer_email,
      "type": 400,
      "description": recepit.description,
      "customer_name": recepit.customer_name,
      "customer_email": recepit.customer_email,
      "customer_address": recepit.customer_address,
      "payment": paymentObj,
      "price_total": recepit.price_total,
      "comment": recepit.comment,
      "send_copy":recepit.send_copy,
      "email_text":"hello world!!"
    }
    donor_id=get_donors_by_tz(recepit.customer_zeout)
    print(donor_id[0].zeout)
    donation={
        "donors_id":donor_id[0].zeout,
        "source":"בנק",
        "amount": recepit.price_total,
        "currency": "שקל",
        "transactionTime":"",
        "lastNum":0,
        "transactionType":"רגיל",
        "groupe": "ענייי עירך",
        "tashloumim": 1,
        "firstTashloum":0,
        "nextTashloum": 0
    }
    print(donation)
    return add_donation(donation)
    # headers = {'content-type': 'application/json'}

    # response = requests.post(urlRecepit, json=payload)
    # response_data = response.json()
    # if response_data['success']:
    #     print (response_data["pdf_link"] + "\n")
    #     return response_data
    # else:
    #     print (response.json())


# return donor_repo.add_donor_with_address(new_donor)
def update_keva_donation(keva_id, updates):
    return donor_repo.update_keva_donation(keva_id, updates)


def add_keva_donation(new_donor):
    return donor_repo.add_keva_donation(new_donor)


def add_keva(new_keva):
    return donor_repo.add_keva(new_keva)


def add_donation(new_donation):
    print("in add",new_donation)
    return donor_repo.add_new_donation(new_donation)


def get_donor_keva(last_name: str, first_name: str = None):
    donor: DonorSchema = get_donors_by_name(last_name, first_name)
    return donor_repo.get_donor_keva_by_id(donor[0].id)


# def add_bank_donation(new_donation:BankDonationPostSchema) -> BankDonationPostSchema:
#     return donor_repo.add_bank_donation(new_donation)

# def add_keva_donation(new_donation: KevaDonationPostSchema) -> KevaDonationPostSchema:
#     return donor_repo.add_keva_donation(new_donation)
# def update_allocation(id: int, update: AllocationSchema)-> AllocationSchema:

#     return allocation_repo.update_allocation(id, update)

# def delete_allocation(id: int):

#     return allocation_repo.delete_allocation(id)



def update_monthly_keva_donations(keva_donations: list[dict]):
    
    # current_month = datetime.today().strftime("%Y-%m-01")  

    for donation in keva_donations:
        donor_id = donation["donor_id"]
        monthly_amount = donation["monthly_amount"]


        existing_donations = donor_repo.get_donor_keva_by_id(donation["donor_id"])

        if existing_donations:
            matching_donation = next(
                (
                    d
                    for d in existing_donations
                    if d.monthly_amount == monthly_amount
                ),
                None,
            )

            if matching_donation:
                donor_repo.update_keva_donation(matching_donation.id, updates={
                                        "were_carried_out": (
                                            matching_donation.were_carried_out + 1
                                        )
                                    })
            else:
                donor_repo.update_keva_donation(
                    matching_donation.id,
                    updates={"status": False},
                )

                donor_repo.add_keva_donation(donation)

        else:
            
            donor_repo.add_keva_donation(donation)

    mark_missing_donations_as_inactive(keva_donations)

def mark_missing_donations_as_inactive(new_donations):
    
    prev_month_donations = donor_repo.get_activite_keva_donation()

    for donation in prev_month_donations:
        if not any(d["donor_id"] == donation.donors_id for d in new_donations):
            donor_repo.update_keva_donation(
                    donation.id,
                    updates={"status": False},
                )
