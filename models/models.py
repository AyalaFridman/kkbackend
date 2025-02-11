from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from db.database import Base


class BaseSupport(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    amount = Column(Float, nullable=False)
    date = Column(String, nullable=False)
    notes = Column(String, nullable=True)


class Support(BaseSupport):
    __tablename__ = "supports"
    needy_id = Column(Integer, ForeignKey("needy.id"))
    allocations_id = Column(Integer, ForeignKey("allocations.id"))


class SpecialSupport(BaseSupport):
    __tablename__ = "special_supports"
    needy_id = Column(Integer, ForeignKey("needy.id"))
    service_provider_id = Column(Integer, ForeignKey("service_providers.id"))

    service_provider = relationship(
        "ServiceProvider", back_populates="special_supports"
    )


class ServiceProvider(Base):
    __tablename__ = "service_providers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=True)
    city = Column(String, nullable=False)
    street = Column(String, nullable=False)
    building_number = Column(String, nullable=True)
    apartment_number = Column(Integer, nullable=True)
    type_of_service = Column(String, nullable=False)
    account_owner_name = Column(String, nullable=False)
    account_number = Column(String, nullable=False)
    bank_number = Column(String, nullable=False)
    branch_number = Column(String, nullable=False)
    provider_type = Column(String, nullable=False)  # "needy" או "cashbox"

    special_supports = relationship(
        "SpecialSupport", back_populates="service_provider", cascade="all, delete"
    )
    # cashbox_id = Column(Integer, ForeignKey("cashbox.id"), nullable=True)
    cashbox = relationship("CashBox", back_populates="service_providers")
    
    # תיקון שם המחלקה ושם ה-back_populates
    payments = relationship("Payment", back_populates="service_provider")


class CashBox(Base):
    __tablename__ = "cashbox"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    balance = Column(Integer, default=0)
    service_provider_id = Column(Integer, ForeignKey("service_providers.id"))

    service_providers = relationship("ServiceProvider", back_populates="cashbox")


class Allocation(Base):
    __tablename__ = "allocations"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))
    fund_id = Column(Integer, ForeignKey("funds.id"))
    allocation_type = Column(String, nullable=True)
    allocation_method = Column(String, nullable=True)
    amount_or_quantity = Column(Float, default=0.0)
    distributed = Column(Float, default=0.0)

    fund = relationship("Fund", back_populates="allocations")
    project = relationship(
        "Project", back_populates="allocations", passive_deletes=True
    )
    supports = relationship("Support", backref="allocation", cascade="all, delete")


class Fund(Base):
    __tablename__ = "funds"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    contact_name = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    mail = Column(String, nullable=True)
    type = Column(String, nullable=False)
    allocations = relationship(
        "Allocation", back_populates="fund", cascade="all, delete"
    )


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)

    allocations = relationship(
        "Allocation", back_populates="project", cascade="all, delete"
    )


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    needy_id = Column(Integer, ForeignKey("needy.id"))
    expense_type = Column(String, nullable=True)
    description = Column(String, nullable=True)
    amount = Column(Float, default=0.0)


class Income(Base):
    __tablename__ = "income"

    id = Column(Integer, primary_key=True, index=True)
    needy_id = Column(Integer, ForeignKey("needy.id"))
    income_type = Column(String, nullable=True)
    description = Column(String, nullable=True)
    amount = Column(Float, default=0.0)


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    payment_method = Column(String, nullable=False)
    service_provider_id = Column(Integer, ForeignKey("service_providers.id"))

    service_provider = relationship("ServiceProvider", back_populates="payments")


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    needy_id = Column(Integer, ForeignKey("needy.id"))
    account_owner_name = Column(String, nullable=False)
    account_number = Column(String, nullable=False)
    bank_number = Column(String, nullable=False)
    branch_number = Column(String, nullable=False)


# class Address(Base):
#     __tablename__ = "addresses"

#     id = Column(Integer, primary_key=True, index=True)
#     city = Column(String, nullable=False)
#     street = Column(String, nullable=False)
#     building_number = Column(String, nullable=True)


class Child(Base):
    __tablename__ = "children"

    id = Column(Integer, primary_key=True, index=True)
    needy_id = Column(Integer, ForeignKey("needy.id"))
    child_id = Column(String, nullable=False)
    name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=False)
    place_of_study = Column(String, nullable=False)
    tuition_amount = Column(Integer, nullable=False)
    additional_expenses = Column(Integer, nullable=False)


class Needy(Base):
    __tablename__ = "needy"

    id = Column(Integer, primary_key=True, index=True)
    last_name = Column(String, nullable=False)
    husband_name = Column(String, nullable=True)
    id_husband = Column(String, nullable=True)
    husband_date_of_birth = Column(Date, nullable=True)
    wife_name = Column(String, nullable=True)
    id_wife = Column(String, nullable=True)
    wife_date_of_birth = Column(Date, nullable=True)
    marital_status = Column(String, nullable=True)
    num_of_children = Column(Integer, default=0)
    num_of_minor_children = Column(Integer, default=0)
    num_of_unmarried_children = Column(Integer, default=0)
    level_of_need = Column(Integer, nullable=True)
    city = Column(String, nullable=False)
    street = Column(String, nullable=False)
    building_number = Column(String, nullable=True)
    apartment_number = Column(Integer, nullable=True)
    phone = Column(String, nullable=True)
    husband_phone = Column(String, nullable=True)
    wife_phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    total_debt = Column(Float, default=0.0)
    status = Column(Boolean, default=True, nullable=False)
    one_time_support=Column(Integer, nullable=True)
    reason_for_expense = Column(String, nullable=True)
    gerim=Column(Boolean, nullable=False)
    # קשרים
    children = relationship("Child", backref="parent_needy", cascade="all, delete")
    expenses = relationship("Expense", backref="needy", cascade="all, delete")
    income = relationship("Income", backref="needy", cascade="all, delete")
    # transfers = relationship(
    #     "Transfer",
    #     primaryjoin="and_(Transfer.beneficiary_id == Needy.id, Transfer.beneficiary_type == 'needy')",
    #     foreign_keys="[Transfer.beneficiary_id]",
    #     backref="needy",
    #     viewonly=True,
    # )
    supports = relationship("Support", backref="needy", cascade="all, delete")
    special_supports = relationship("SpecialSupport", backref="needy", cascade="all, delete")
    account= relationship("Account",backref="needy",cascade="all, delete",uselist=False)

class DonorsBase(Base):
    __tablename__ = "donors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    zeout = Column(String)
    name = Column(String)
    city = Column(String)
    address = Column(String)
    phone = Column(String)
    husband_phone = Column(String)
    wife_phone = Column(String)
    mail = Column(String)
    bank = Column(String)
    brunch = Column(String)
    account_num = Column(String)
    source_of_details = Column(String)

    # קשרים
    donations_keva = relationship("DonationsKeva", back_populates="donor")
    donations = relationship("Donation", back_populates="donor")


class DonationsKeva(Base):
    __tablename__ = "donations_keva"

    id = Column(Integer, primary_key=True, autoincrement=True)
    donors_id = Column(Integer, ForeignKey("donors.id"), nullable=False)
    status = Column(Boolean, nullable=False)
    monthly_amount = Column(Float, nullable=True)
    currency = Column(String, nullable=True)
    category = Column(String, nullable=True)
    notes = Column(String, nullable=True)
    balance_of_charges = Column(Integer, nullable=True)
    were_carried_out = Column(Integer, nullable=True)
    next_charge = Column(String, nullable=True)
    error = Column(String, nullable=True)
    validity = Column(String, nullable=True)
    last_4_digits = Column(String, nullable=True)
    creationDate = Column(String, nullable=False)

    # קשרים
    donor = relationship("DonorsBase", back_populates="donations_keva")


class Donation(Base):
    __tablename__ = "donation"

    id = Column(Integer, primary_key=True, autoincrement=True)
    donors_id = Column(Integer, ForeignKey("donors.id"), nullable=False)
    amount = Column(Float, nullable=False)
    currency = Column(String, nullable=True)
    transactionTime = Column(String, nullable=True)
    lastNum = Column(String, nullable=True)
    transactionType = Column(String, nullable=True)
    groupe = Column(String, nullable=True)
    tashloumim = Column(Integer, nullable=True)
    firstTashloum = Column(Float, nullable=True)
    nextTashloum = Column(Float, nullable=True)
    source = Column(String, nullable=True)

    donor = relationship("DonorsBase", back_populates="donations")



class Settings(Base):
    __tablename__ = "settings"

    key = Column(String, primary_key=True)
    value = Column(String)
