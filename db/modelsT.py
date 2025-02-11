from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base
from add_to_db import object_manager
# from db_config import object_manager

# class DonorsBase(Base):
#     __tablename__ = "donors"  
# class DonorsBase(Base):
#     __tablename__ = "donors"  

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     zeout = Column(String, nullable=False)  
#     last_name = Column(String, nullable=False)
#     first_name = Column(String, nullable=False)
#     address = Column(String, nullable=True)
#     phone = Column(String, nullable=True)
#     husband_phone = Column(String, nullable=True)
#     wife_phone = Column(String, nullable=True)
#     mail = Column(String, nullable=True)
#     amount = Column(Float, nullable=True)
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     zeout = Column(String, nullable=False)  
#     last_name = Column(String, nullable=False)
#     first_name = Column(String, nullable=False)
#     address = Column(String, nullable=True)
#     phone = Column(String, nullable=True)
#     husband_phone = Column(String, nullable=True)
#     wife_phone = Column(String, nullable=True)
#     mail = Column(String, nullable=True)
#     amount = Column(Float, nullable=True)

#     # קשרים
#     donations_keva = relationship("DonorsKevaCC", back_populates="donor_keva")
#     donations = relationship("Donation", back_populates="donor")


# class DonorsKevaCC(Base):
#     __tablename__ = "donors_keva_cc" 

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     donors_id = Column(Integer, ForeignKey("donors.id"), nullable=False)
#     status = Column(Boolean, nullable=False)
#     monthly_amount = Column(Float, nullable=True)
#     currency = Column(String, nullable=True)
#     category = Column(String, nullable=True)
#     notes = Column(String, nullable=True)
#     balance_of_charges = Column(Integer, nullable=True)
#     were_carried_out = Column(Integer, nullable=True)
#     next_charge = Column(Date, nullable=True)
#     error = Column(String, nullable=True)
#     validity = Column(String, nullable=True)
#     last_4_digits = Column(String, nullable=True)
#     established_in_the_position = Column(String, nullable=True)
#     creationDate = Column(Date, nullable=False)
#     personal_number = Column(String, nullable=True)
#     expected__to_be_paid_12_units = Column(Float, nullable=True)
#     expected__to_be_paid_36_units = Column(Float, nullable=True)

#     # קשרים
#     donor = relationship("DonorsBase", back_populates="donations_keva")
    
# class donation(Base):
#     __tablename__ = "donation"
    
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     donors_id = Column(Integer, ForeignKey("donors.id"), nullable=False)
#     amount = Column(Float, nullable = False)
#     currency = Column(Integer, nullable = True)
#     transactionTime = Column(Date, nullable=True)
#     lastNum = Column(String, nullable = True)
#     transactionType = Column(String, nullable = True)
#     groupe= Column(String, nullable = True)
#     comments= Column(String, nullable = True)
#     tashloumim = Column(Integer, nullable = True)
#     firstTashloum= Column(Float, nullable = True)
#     nextTashloum = Column(Float, nullable = True)
#     transactionId= Column(String, nullable = True)
#     # kevaId= Column(Integer, nullable = True)
    
#     donor = relationship("DonorsBase", back_populates="donations")

class BaseSupport(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    date = Column(Date, nullable=False)
    notes = Column(String, nullable=True)

# class Support(BaseSupport):
#     __tablename__ = "supports"
#     needy_id = Column(Integer, ForeignKey("needy.id"))
#     allocations_id = Column(Integer, ForeignKey("allocations.id"))

class SpecialSupport(BaseSupport):
    __tablename__ = "special_supports"
    needy_id = Column(Integer, ForeignKey("needy.id"))
    service_provider_id = Column(Integer, ForeignKey("service_providers.id"))
# class ServiceProvider(Base):
#     __tablename__ = "service_providers"
    
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=True)
#     phone =Column(String, nullable=False)
#     email = Column(String, nullable=False)
#     address_id = Column(Integer, ForeignKey("addresses.id"))
#     account_owner_name = Column(String, nullable=False)
#     account_number = Column(String, nullable=False)
#     bank_number = Column(String, nullable=False)
#     branch_number = Column(String, nullable=False)
#     provider_type = Column(String, nullable=False)  # "needy" או "cashbox"
    
#     address = relationship("Address", backref="needy", cascade="all, delete")
#     special_supports_id = Column(Integer, ForeignKey("special_supports.id"), nullable=True)
#     needy = relationship("special_supports", back_populates="service_providers")
#     cashbox_id = Column(Integer, ForeignKey("cashbox.id"), nullable=True)
#     cashbox = relationship("CashBox", back_populates="service_providers")
    
# class CashBox(Base):
#     __tablename__ = "cashbox"
    
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False) 
#     balance = Column(Integer, default=0)  
    
#     service_providers = relationship("ServiceProvider", back_populates="cashbox")

object_manager.db_manager.create_tables(Base)
