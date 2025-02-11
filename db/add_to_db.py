import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import random
from models.models import *
from db_config import object_manager


# # יצירת טבלאות עבור כל אובייקט במסד הנתונים


object_manager.db_manager.create_tables(Base)

# # streets = [
# #     "שדרות נשיאי ישראל",
# #     "רחוב הזית",
# #     "רחוב הארזים",
# #     "רחוב השקד",
# #     "רחוב הפרחים",
# #     "שדרות יצחק רבין",
# #     "רחוב הדקל",
# #     "רחוב האלה",
# #     "שדרות הגפן",
# #     "רחוב הנרקיסים",
# #     "רחוב החורש",
# #     "רחוב התמר",
# # ]

# # # יצירת נתונים

# # for street in streets:
# #     for building_number in range(1, 51):
# #         new_address = Address(
# #             city="כרמיאל",
# #             street=street,
# #             building_number=building_number
# #         )

# #         object_manager.add_object(new_address)

# new_needies = [
#     Needy(
#         last_name="לוי",
#         husband_name="יצחק",
#         id_husband="123456789",
#         wife_name="רבקה",
#         id_wife="987456321",
#         marital_status="Married",  # ['Married', 'Single', 'Divorced', 'Widowed']
#         num_of_children=5,
#         num_of_minor_children=5,
#         num_of_unmarried_children=5,
#         level_of_need=4,
#         city="כרמיאל",
#         street="רחוב הזית",
#         building_number=12,
#         apartment_number=8,
#         phone="04-78963254",
#         husband_phone="0504100000",
#         wife_phone="0527100000",
#         email=None,
#         total_debt=15000,
#         status=True
#     ),
#     Needy(
#         last_name="כהן",
#         husband_name="דוד",
#         id_husband="123456789",
#         wife_name="",
#         id_wife="",
#         marital_status="Divorced",  # ['Married', 'Single', 'Divorced', 'Widowed']
#         num_of_children=10,
#         num_of_minor_children=7,
#         num_of_unmarried_children=2,
#         level_of_need=5,
#         city="כרמיאל",
#         street="רחוב הזית",
#         building_number=20,
#         apartment_number=10,
#         phone="04-78963254",
#         husband_phone="0504100000",
#         wife_phone="",
#         email=None,
#         total_debt=15000,
#         status=True
        
#     ),
#     Needy(
#         last_name="שפירא",
#         husband_name="מיכאל",
#         id_husband="123456789",
#         wife_name="נחמה",
#         id_wife="582369741",
#         marital_status="Married",  # ['Married', 'Single', 'Divorced', 'Widowed']
#         num_of_children=12,
#         num_of_minor_children=8,
#         num_of_unmarried_children=2,
#         level_of_need=5,
#         city="כרמיאל",
#         street="רחוב הזית",
#         building_number=30,
#         apartment_number=15,
#         phone="04-78963254",
#         husband_phone="0504100000",
#         wife_phone="0527100000",
#         email=None,
#         total_debt=15000,
#         status=True
# new_needies = [
#     Needy(
#         last_name="לוי",
#         husband_name="יצחק",
#         id_husband="123456789",
#         wife_name="רבקה",
#         id_wife="987456321",
#         marital_status="Married",  # ['Married', 'Single', 'Divorced', 'Widowed']
#         num_of_children=5,
#         num_of_minor_children=5,
#         num_of_unmarried_children=5,
#         level_of_need=4,
#         city="כרמיאל",
#         street="רחוב הזית",
#         building_number=12,
#         apartment_number=8,
#         phone="04-78963254",
#         husband_phone="0504100000",
#         wife_phone="0527100000",
#         email=None,
#         total_debt=15000,
#         status=True,
#         one_time_support=500,
#         reason_for_expense="רפואית- ניתוח לילד",
#         gerim=False,
#     ),
#     Needy(
#         last_name="כהן",
#         husband_name="דוד",
#         id_husband="123456789",
#         wife_name="",
#         id_wife="",
#         marital_status="Divorced",  # ['Married', 'Single', 'Divorced', 'Widowed']
#         num_of_children=10,
#         num_of_minor_children=7,
#         num_of_unmarried_children=2,
#         level_of_need=5,
#         city="כרמיאל",
#         street="רחוב הזית",
#         building_number=20,
#         apartment_number=10,
#         phone="04-78963254",
#         husband_phone="0504100000",
#         wife_phone="",
#         email=None,
#         total_debt=15000,
#         status=True,
#         gerim=True    
#     ),
#     Needy(
#         last_name="שפירא",
#         husband_name="מיכאל",
#         id_husband="123456789",
#         wife_name="נחמה",
#         id_wife="582369741",
#         marital_status="Married",  # ['Married', 'Single', 'Divorced', 'Widowed']
#         num_of_children=12,
#         num_of_minor_children=8,
#         num_of_unmarried_children=2,
#         level_of_need=5,
#         city="כרמיאל",
#         street="רחוב הזית",
#         building_number=30,
#         apartment_number=15,
#         phone="04-78963254",
#         husband_phone="0504100000",
#         wife_phone="0527100000",
#         email=None,
#         total_debt=15000,
#         status=True,
#         one_time_support=200,
#         reason_for_expense="נישואי בת",
#         gerim=False
        
#     ),
# ]


# object_manager.add_objects(new_needies)
# print("נתמכים נוספו בהצלחה.")


# new_projects = [
#     Project(name="בין הזמנים", description=""),
#     Project(name="פסח תשפה", description=""),
#     Project(name="שוטף", description=""),
# ]
# object_manager.add_objects(new_projects)
# print("פרויקטים נוספו בהצלחה.")


# new_funds = [
#     Fund(name="טובה וברכה", description="",contact_name="שמעון",phone="0556702879",mail="ad05697@gmail.com", type = "עזרה לקופה"),
#     Fund(name="יד מיכל", description="",contact_name="לוי",phone="0527693586",mail="", type = "עזרה לקופה"),
#     Fund(name="קופת כרמיאל", description="",contact_name="משה",phone="0533978563",mail="karmiel@gmail.com", type = "עזרה לקופה"),
#     Fund(name="בעזרי", description="עזרה לכלות",contact_name="משה",phone="0533978563",mail="karmiel@gmail.com", type = "עזרה למשפחות"),
#     Fund(name="חד הורי", description="עזרה למשפחות חד הוריות",contact_name="משה",phone="0533978563",mail="karmiel@gmail.com", type = "עזרה למשפחות"),

# ]
# object_manager.add_objects(new_funds)
# print("קרנות נוספו בהצלחה.")


# new_allocations = [
#     Allocation(
#         project_id=1,
#         fund_id=1,
#         allocation_type="כסף",
#         allocation_method="מזומן",
#         amount_or_quantity=5000,
#     ),
#     Allocation(
#         project_id=2,
#         fund_id=2,
#         allocation_type="מצרכים",
#         allocation_method="מעילים",
#         amount_or_quantity=100,
#     ),
#     Allocation(
#         project_id=1,
#         fund_id=3,
#         allocation_type="מצרכים",
#         allocation_method="עופות",
#         amount_or_quantity=200,
#     ),
# ]

# object_manager.add_objects(new_allocations)
# print("חלוקות נוספו בהצלחה.")



# new_supports = [
#     Support(
#         allocations_id=1,
#         needy_id=1,
#         date="30/01/2024",
#         amount=500,
#         notes="",
#     ),
#     Support(
#         allocations_id=2,
#         needy_id=1,
#         date="30/01/2024",
#         amount=3,
#         notes="",
#     ),
# ]

# object_manager.add_objects(new_supports)
# print("תמיכות נוספו בהצלחה.")

# service_providers = [
#     ServiceProvider(
#         name = "שרה",
#         phone = "0520596387",
#         email = "",
#         type_of_service = "מטפלת רגשית",
#         city="כרמיאל",
#         street="רחוב הארזים",
#         building_number=5,
#         apartment_number=2,
#         account_owner_name = "שרה",
#         account_number = "785412",
#         bank_number = "52",
#         branch_number = "180",
#         provider_type = "needy",
        
#     )
#     ,
# ]

# object_manager.add_objects(service_providers)
# print("נותני שירות נוספו בהצלחה")

# new_special_supports = [
#     SpecialSupport(
#         needy_id= 1,
#         service_provider_id = 1,
#         amount = 500,
#         date = "01/02/2024",
#         notes = "טיפול רגשי לילד"
#     ),
#     SpecialSupport(
#         needy_id= 2,
#         service_provider_id = 1,
#         amount = 1200,
#         date = "15/05/2024",
#         notes = "סומכת"
#     )
# ]

# object_manager.add_objects(new_special_supports)
# print("תמיכות מיוחדות נוספו בהצלחה.")

# cashBox = CashBox(
#     name = "פרסום ",
#     balance = 500,
#     service_provider_id = 1
# )
# object_manager.add_object(cashBox)

# new_incomes = [
#     Income(
#         needy_id=1,
#         income_type="עיסוק הבעל",
#         description="כולל",
#         amount=1000,
#     ),
#     Income(
#         needy_id=1,
#         income_type="הכנסות וקצבאות נוספות",
#         description="קצבת ילדים",
#         amount=500,
#     ),
#     Income(
#         needy_id=1,
#         income_type="הכנסות וקצבאות נוספות",
#         description="קצבת נכות",
#         amount=1000,
#     ),
#     Income(
#         needy_id=1,
#         income_type="הכנסות וקצבאות נוספות",
#         description="מלגת מבחנים",
#         amount=280,
#     ),
#     Income(
#         needy_id=2,
#         income_type="עיסוק הבעל",
#         description="כולל",
#         amount=1500,
#     ),
#     Income(
#         needy_id=3,
#         income_type="הכנסות וקצבאות נוספות",
#         description="קצבת ילדים",
#         amount=700,
#     ),
#     Income(
#         needy_id=1,
#         income_type="עיסוק האישה",
#         description="גננת",
#         amount=4500,
#     ),
#     Income(
#         needy_id=3,
#         income_type="עיסוק האישה",
#         description="מורה",
#         amount=5500,
#     ),
# ]
# # הוספת האובייקטים למסד הנתונים
# object_manager.add_objects(new_incomes)
# print("הכנסות נוספו בהצלחה.")

# new_accounts = [
#     Account(
#         needy_id=1,
#         account_owner_name="יצחק לוי",
#         account_number="123456",
#         bank_number="10",
#         branch_number="001",
#     ),
#     Account(
#         needy_id=2,
#         account_owner_name="דוד כהן",
#         account_number="654321",
#         bank_number="52",
#         branch_number="182",
#     ),
#     Account(
#         needy_id=3,
#         account_owner_name="מיכאל שפירא",
#         account_number="789123",
#         bank_number="52",
#         branch_number="180",
#     ),
# ]
# # הוספת אובייקטים של חשבונות למסד הנתונים
# object_manager.add_objects(new_accounts)
# print("חשבונות נוספו בהצלחה.")


# new_children = [
#     Child(needy_id=1, child_id="123456001", name="רינה ", birth_date="21/05/2010",place_of_study="משכנות תמר-בית ספר",tuition_amount=700,additional_expenses=100),
#     Child(needy_id=1, child_id="123456002", name="שרה ", birth_date="10/01/2020",place_of_study="גני עץ הדעת",tuition_amount=400,additional_expenses=0),
#     Child(needy_id=2, child_id="123456003", name="לאה ", birth_date="05/06/2023",place_of_study="משכנות תמר-בית ספר",tuition_amount=1000,additional_expenses=300),
# ]
# object_manager.add_objects(new_children)
# print("ילדים נוספו בהצלחה.")

# setting = Settings(key = "lastTransactionId", value= "46663925")
# object_manager.add_object(setting)