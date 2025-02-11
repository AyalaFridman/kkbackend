from copy import copy
from sqlalchemy import create_engine
from contextlib import contextmanager
from typing import Dict, List, Any, Type, TypeVar,Optional
from sqlalchemy.orm import joinedload,sessionmaker
from pydantic import BaseModel
from sqlalchemy.sql import and_
from models.models import *
from models.schema import *


class DBManager:
    def __init__(self, db_config):
        self.engine = create_engine(
            f"postgresql://{db_config['user']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['dbname']}",
            pool_pre_ping=True,
        )
        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

    @contextmanager
    def get_session(self):
        session = self.SessionLocal()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def create_tables(self, base):
        base.metadata.create_all(self.engine, checkfirst=True)


class ObjectManager:
    def __init__(self, db_manager: DBManager):
        """אתחול ObjectManager עם DBManager"""
        self.db_manager = db_manager

    def create_management_table(self, model_class):
        """יצירת טבלה מתוך מחלקת SQLAlchemy"""
        model_class.__table__.create(self.db_manager.engine, checkfirst=True)

    def create_object(self, model_class, data, session=None):
        # פתיחת session רק אם הוא לא סופק מבחוץ
        if session is None:
            with self.db_manager.get_session() as session:
                obj = self.create_object(model_class, data, session)
                session.commit()  # וודא שמירת האובייקט
                session.refresh(obj)  # רענון האובייקט
                return obj
        # יצירת אובייקט חדש
        obj = model_class()
        session.add(obj)

        if isinstance(data, dict):
            data_dict = data
        else:
            data_dict = data.dict()

        # עדכון השדות באובייקט הראשי
        for key, value in data_dict.items():
            if isinstance(value, list):
                # טיפול ברשימות (קשרים מקושרים)
                related_objects = getattr(obj, key, None)
                if related_objects is not None:
                    related_model = model_class.__mapper__.relationships[
                        key
                    ].mapper.class_
                    setattr(
                        obj,
                        key,
                        [
                            self.create_object(
                                related_model, item, session
                            )  # העברת session
                            for item in value
                        ],
                    )
            elif hasattr(obj, key):
                setattr(obj, key, value)
        session.flush()
        return obj

    def add_object(self, obj_instance) -> dict:
        try:
            with self.db_manager.get_session() as session:
                session.add(obj_instance)
                session.commit()  # שמירה בפועל של הנתונים
            print("VVVV")
            return {"success": True, "message": "Object added successfully"}
        except Exception as e:
            return {"success": False, "message": str(e)}


    def create_needy(self, data: dict):
        print(data.last_name)
        # print(data["last_name"])
        # יצירת אובייקט נצרך
        needy_data = {
            "last_name": data.last_name,
            "husband_name": data.husband_name,
            "id_husband": data.id_husband,
            "husband_date_of_birth": data.husband_date_of_birth,
            "wife_name": data.wife_name,
            "id_wife": data.id_wife,
            "wife_date_of_birth": data.wife_date_of_birth,
            "marital_status": data.marital_status,
            "city":data.city,
            "street":data.street,
            "building_number":data.building_number,
            "apartment_number":data.apartment_number,
            "num_of_children": data.num_of_children,
            "num_of_minor_children": data.num_of_minor_children,
            "num_of_unmarried_children": data.num_of_unmarried_children,
            "level_of_need": data.level_of_need,
            "apartment_number": data.apartment_number,
            "phone": data.phone,
            "husband_phone": data.husband_phone,
            "wife_phone": data.wife_phone,
            "email": data.email,
            "total_debt": data.total_debt,
            "status":data.status,
            "one_time_support":data.one_time_support,
            "reason_for_expense":data.reason_for_expense,
            "gerim":data.gerim
        }

        # # יצירת אובייקט Needy
        # data_dict=data.dict()
        print(type(needy_data))
        needy = Needy(**needy_data)
        # # הוספת ילדים
        for child in data.children:
            needy.children.append(
                Child(
                    name=child.name,
                    child_id=child.child_id,
                    birth_date=child.birth_date,
                    place_of_study=child.place_of_study,
                    tuition_amount=child.tuition_amount,
                    additional_expenses=child.additional_expenses
                )
            )
        print(needy)
        needy.account=Account(
            account_owner_name=data.account.account_owner_name,
            account_number=data.account.account_number,
            bank_number=data.account.bank_number,
            branch_number=data.account.branch_number
        )
        print(needy.account)
        # # הוספת הכנסות
        for income in data.income:
            needy.income.append(
                Income(
                    income_type=income.income_type,
                    description=income.description,
                    amount=income.amount,
                )
            )
        print(needy)
            

        # # הוספת הוצאות
        # for expense in data.get("expenses", []):
        #     needy.expenses.append(
        #         Expense(
        #             expense_type=expense.get("expense_type"),
        #             description=expense.get("description"),
        #             amount=expense.get("amount"),
        #         )
        #     )
        with self.db_manager.get_session() as session:
            session.add(needy)
            session.commit()
        return needy

    def add_objects(self, obj_instances):
        """הוספת רשימת אובייקטים לטבלה"""
        with self.db_manager.get_session() as session:
            session.add_all(obj_instances)

    def get_objects_whithout_rel(self, model_class, filters=None):
        """שליפת רשומות עם אופציה לפילטרים"""
        with self.db_manager.get_session() as session:
            query = session.query(model_class)
            if filters:
                query = query.filter_by(**filters)
            res = query.all()
            res_copy = [copy(needy) for needy in res]
            for needy in res_copy:
                print(needy)
            return res_copy

    T = TypeVar("T", bound=BaseModel)

    def get_objects(
        self,
        base_table: Any,
        schema_class: Type[T],
        relationships: Optional[List[Any]] = None,
        filters: Optional[Dict[str, Any]] = None,
    ) -> List[T]:
        with self.db_manager.get_session() as session:

            query = session.query(base_table)

            if relationships:
                for relationship in relationships:
                    query = query.options(joinedload(relationship))
            
            if filters:
                query = query.filter(and_(*filters))
                
            results = query.all()
            
            return [schema_class.from_orm(obj) for obj in results]
        

    def update_objects(self, model_class, schema_class, filters, updates, rel=None):
        with self.db_manager.get_session() as session:
            query = session.query(model_class).filter(*filters)
            for obj in query:
                for key, value in updates.items():
                    if hasattr(obj, key):
                        if isinstance(getattr(obj, key), (list, dict)):
                            continue
                        setattr(obj, key, value)  # עדכון השדה במודל
                session.add(obj)  # הוסף את האובייקט לסשן של SQLAlchemy
            # session.flush()
            session.commit()  # עדכון במסד הנתונים

        return updates  # החזר את המילון המעודכן


    def delete_objects(self, model_class, filters):
        """מחיקת רשומות לפי פילטרים"""
        with self.db_manager.get_session() as session:
            query = session.query(model_class).filter(*filters)
            print(query)

            for obj in query:
                session.delete(obj)
