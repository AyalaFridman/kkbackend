from models.models import Donation, DonorsBase, DonationsKeva
from models.donor_schema import DonorSchema, DonorSchemaGet
from models.address_schema import AddressSchema
from models.donation_get_schema import DonationSchema, DonationSchemaGet
from models.donation_schema import DonationSchema
from models.donation_keve_get_schema import DonationsKevaSchemaGet
from db_config import object_manager
from typing import List
from datetime import datetime

def get_all_donors() -> List[DonorSchema]:
    print("dal before: ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    donors = object_manager.get_objects(
        base_table=DonorsBase,
        schema_class=DonorSchemaGet,
        # relationships=[Fund.allocations],  # טעינה מקדימה של הקשר 'allocations'
        filters=None,  # ניתן להוסיף פילטרים לפי הצורך
    )
    print("dal after: ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    return donors

def get_donors_by_id(id):
    filters = [DonorsBase.id == id]
    relationships=[DonorsBase.donations,DonorsBase.donations_keva]
    return object_manager.get_objects(
        base_table=DonorsBase, schema_class=DonorSchemaGet, filters=filters,relationships=relationships
    )

def get_donors_by_name(last_name: str, first_name: str = None):
    filters = [DonorsBase.last_name == last_name]
    if first_name:
        filters.append(DonorsBase.first_name == first_name)
    return object_manager.get_objects(
        base_table=DonorsBase, schema_class=DonorSchemaGet, filters=filters
    )
def get_donor_by_tz(tz:str)->DonorSchemaGet:
    filters = [DonorsBase.zeout == tz]
    return object_manager.get_objects(
        base_table=DonorsBase, schema_class=DonorSchemaGet, filters=filters
        )
    

def get_donors_keva():

    return object_manager.get_objects(
        base_table=DonationsKeva,
        schema_class=DonationsKevaSchemaGet,
        relationships=[DonationsKeva.donor],
        filters=None,
    )

def get_donor_by_account(account):
    
    donor =  object_manager.get_objects(
        base_table=DonorsBase,
        schema_class=DonorSchemaGet,
        filters=[DonorsBase.zeout == account]
    )
    return donor

def get_reg_donation():

    return object_manager.get_objects(
        base_table=Donation,
        schema_class=DonationSchemaGet,
        relationships=[Donation.donor],
        filters=None,
    )

def get_donor_keva_by_id(donor_id: int):
    
    filters = [DonationsKeva.donors_id == donor_id]
    res= object_manager.get_objects(
        base_table=DonationsKeva,
        schema_class=DonationsKevaSchemaGet,
        relationships=[DonationsKeva.donor],
        filters=filters,
    )
    return res
def get_activite_keva_donation():
    return object_manager.get_objects(
        base_table=DonationsKeva, 
        schema_class=DonationsKevaSchemaGet,
        relationships=[DonationsKeva.donor],
        filters=[DonationsKeva.status == True]
    )
    
def update_keva_donation(keva_id, updates):
    
    filters = [DonationsKeva.id == keva_id]
    # update = updates.dict(exclude_unset=True)
    donors = object_manager.update_objects(
        DonationsKeva, DonationSchema, filters=filters, updates=updates
    )
    return donors
# def get_bank_donation():

#     return object_manager.get_objects(
#         base_table=BankDonations,
#         schema_class=BankDonationSchema,
#         filters=None,
#     )
    
# def get_donation_keva() ->List[KevaDonationSchema]:
#     return object_manager.get_objects(
#         base_table=Donations_Keva, 
#         schema_class=KevaDonationSchema, 
#         filters = None
#     )

def create_new_donor(donor_data: DonorSchema) -> DonorSchema:
    print(donor_data)
    if type(donor_data)!=dict:
        donor_dict = donor_data.dict()
        new_donor = DonorsBase(**donor_dict)
    else:
        new_donor=DonorsBase(**donor_data) 
    return object_manager.add_object(new_donor)


# def add_donor_with_address(new_donor: dict):
#     donor = object_manager.get_objects(
#         DonorsBase,
#         schema_class=DonorSchema,
#         filters=[DonorsBase.zeout == new_donor["zeout"]],
#     )
#     if donor:
#         print(f"התורם עם מספר הזיהוי {new_donor['zeout']} כבר קיים במאגר.")
#         return donor
#     else:
#         print("the donor don't exist")

#     # # חיפוש אם הכתובת קיימת
#     address_data = new_donor["address"]
#     address_dict = address_data.split(" ")
#     address = object_manager.get_objects(
#         Address, schema_class=AddressSchema, filters=[Address.city == address_dict[-1]]
#     )

#     if address:
#         # print(f"הכתובת קיימת. הכתובת תוקצה לתורם.", new_donor['address'])
#         pass
#         # new_donor['address_id'] = address.id
#     else:
#         # print(f"לא נמצאה הכתובת, נוסיף אותה למאגר.",new_donor['address'])
#         pass
#         # address = object_manager.create_object(Address, address_data)
#         # donor_data['address_id'] = address.id

#     # יצירת התורם
#     donor_data = DonorSchema(
#         zeout=new_donor["zeout"],
#         last_name=new_donor["last_name"],
#         first_name=new_donor["first_name"],
#         address=None,
#         phone=new_donor["phone"],
#         husband_phone=new_donor["husband_phone"],
#         wife_phone=new_donor["wife_phone"],
#         mail=new_donor["mail"],
#         amount=new_donor["amount"],
#     )
#     donor = object_manager.create_object(DonorsBase, donor_data)
#     return donor


def add_keva(donor_keva_data):

    donor = object_manager.get_objects(
        DonorsBase,
        DonorSchemaGet,
        filters=[DonorsBase.zeout == donor_keva_data["donors_id"]],
    )

    # creationDate = datetime.strptime(
    #     donor_keva_data["creationDate"], "%d/%m/%Y %H:%M:%S"
    # ).date()
    if donor:
        balance_of_charges = (
            None
            if donor_keva_data["balance_of_charges"] == ""
            else donor_keva_data["balance_of_charges"]
        )

        new_donor_keva = {
            "donors_id": donor[0].id,
            "status": donor_keva_data["status"],
            "monthly_amount": donor_keva_data["monthly_amount"],
            "currency": donor_keva_data["currency"],
            "category": donor_keva_data["category"],
            "notes": donor_keva_data["notes"],
            "balance_of_charges": balance_of_charges,
            "were_carried_out": donor_keva_data["were_carried_out"],
            "next_charge": None,
            "error": donor_keva_data["error"],
            "validity": donor_keva_data["validity"],
            "last_4_digits": donor_keva_data["last_4_digits"],
            "creationDate": donor_keva_data["creationDate"],
        }
        # print(new_donor_keva)
        add_donor = DonationsKeva(**new_donor_keva)
        res = object_manager.add_object(add_donor)
        # print("success")
        return res
    else:
        print("the donor don't exist", donor_keva_data)

def add_keva_donation(new_keva_data):
    add_keva = DonationsKeva(**new_keva_data)
    return  object_manager.add_object(add_keva)
    
        
def add_donation(donation_data):
    # בדיקה אם התורם קיים בבסיס הנתונים
    donor = object_manager.get_objects(
        DonorsBase,
        DonorSchemaGet,
        filters=[DonorsBase.id == donation_data["donors_id"]],
    )

    if donor or donation_data["donors_id"]=="":
        donors_id = 0 if donation_data["donors_id"] == "" else (donor[0].id if donor else None)
        # יצירת נתוני התרומה
        new_donation_data = {
            "donors_id":donors_id,
            "amount": donation_data["amount"],
            "currency": donation_data.get("currency"),
            "transactionTime": donation_data.get("transactionTime"),
            "lastNum": donation_data.get("lastNum"),
            "transactionType": donation_data.get("transactionType"),
            "groupe": donation_data.get("groupe"),
            # "comments": donation_data.get("comments"),
            "tashloumim": donation_data.get("tashloumim"),
            "firstTashloum": donation_data.get("firstTashloum"),
            "nextTashloum": donation_data.get("nextTashloum"),
            "source":donation_data.get("source")
            # "transactionId": donation_data.get("transactionId"),
        }

        # יצירת אובייקט התרומה
        new_donation = Donation(**new_donation_data)

        # הוספת התרומה לבסיס הנתונים
        res = object_manager.add_object(new_donation)

        return res
    else:
        print("The donor does not exist", donation_data)
        return None

def add_new_donation(new_donation):
    
    dobation = Donation(**new_donation) 
    print(dobation)  
    object_manager.add_object(dobation)
# def add_bank_donation(new_data: BankDonationPostSchema) -> BankDonationPostSchema:
#     bank_donation_dict = new_data.dict()
#     new_bank_donation = BankDonations(**bank_donation_dict)
#     return object_manager.add_object(new_bank_donation)

# def add_keva_donation(new_data) -> KevaDonationPostSchema:
#     # donation_dict = new_data.dict()
#     new_donation = Donations_Keva(**new_data)
#     return object_manager.add_object(new_donation)
