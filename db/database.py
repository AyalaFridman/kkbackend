import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# קריאה למתני סביבה, ב-Railway המשתנה יהיה DATABASE_URL
DATABASE_URL = "postgresql://postgres:HwJMBnyVDjTDjoNVmdyfBUPqPMODMLCw@postgres.railway.internal:5432/railway"

if not DATABASE_URL:
    raise ValueError("DATABASE_URL must be set in the environment variables")

# יצירת אובייקט engine
engine = create_engine(DATABASE_URL)

# יצירת sessionlocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# יצירת Base כדי להשתמש בה כדי להגדיר את הטבלאות
Base = declarative_base()

# יצירת הטבלאות אם לא קיימות
Base.metadata.create_all(bind=engine)
