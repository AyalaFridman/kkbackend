from datetime import datetime
from fastapi import APIRouter, HTTPException, Depends, Body
from pydantic import BaseModel
from typing import List
from models.recepit_schema import RecepitSchema
from services import donor_service
from models.donor_schema import DonorSchema


router = APIRouter()


@router.get("/get-all-donors")
def get_all():
    print("controller: ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    results = donor_service.get_all_donors()
    print("controller after: ", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    return results


@router.get("/get-donors-keva")
def get_donors_keva():

    results = donor_service.get_donors_keva()
    return results

@router.get("/get-reg-donation")
def get_reg_donation():

    results = donor_service.get_reg_donation()
    return results

@router.get("/get-donor-by-id/{id}")
def get_donors_by_id(id):
    results = donor_service.get_donors_by_id(id)
    return results
@router.get("/get-donor-by-tz")
def get_donors_by_tz(tz):
    results = donor_service.get_donors_by_tz(tz)
    return results
@router.get("/get-donors-by-name")
def get_donors_by_name(last_name: str, first_name: str = None):

    results = donor_service.get_donors_by_name(last_name, first_name)
    return results

@router.get("/get-donor-keva")
def get_donors_keva(last_name: str, first_name: str = None):

    results = donor_service.get_donor_keva(last_name, first_name)
    return results


@router.get("/get-donor-keva-by-id/{id}")
async def get_donors_keva_by_id(id: int):

    results = donor_service.get_donor_keva_by_id(id)
    if results is None:
        raise HTTPException(status_code=404, detail="")
    return results

    
@router.post("/add-donor")
async def add_donor(new_donor: DonorSchema = Body(...)):
    donor = donor_service.create_new_donor(new_donor)
    if donor is None:
        raise HTTPException(status_code=404, detail="")
    if donor == "יש כבר תורם עם מספר ת.ז זהה":
        raise HTTPException(status_code=400, detail=donor)
    return donor
@router.post("/create-recepit")
async def create_recepit(recepit:RecepitSchema= Body(...)):
    print("hello")
    donor = donor_service.create_recepit(recepit)
    if donor is None:
        raise HTTPException(status_code=404, detail="")
    return donor
# @router.post("/add-bank-donation")
# async def add_bank_donation(new_bank_donation: BankDonationPostSchema = Body(...)):

#     bank_donation = donor_service.add_bank_donation(new_bank_donation)
#     if bank_donation is None:
#         raise HTTPException(status_code=404, detail="")
#     return bank_donation

# @router.post("/add-bank-keva-donation")
# async def add_bank_keva_donation(new_donation: KevaDonationPostSchema = Body(...)):

#     donation = donor_service.add_keva_donation(new_donation)
#     if donation is None:
#         raise HTTPException(status_code=404, detail="")
#     return donation
