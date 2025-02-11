from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# החלף את DATABASE_URL בהתאם לחיבור שלך ל-PostgreSQL
DATABASE_URL = 'postgresql://postgres:postgresql@localhost:5432/db_test1'
# אם זה בתוך דוקר, השתמש בזה
# DATABASE_URL = 'postgresql://postgres:postgresql@db:5432/db_test1'

# יצירת אובייקט engine
engine = create_engine(DATABASE_URL)

# יצירת sessionlocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# יצירת Base כדי להשתמש בה כדי להגדיר את הטבלאות
Base = declarative_base()

Base.metadata.create_all(bind=engine)
