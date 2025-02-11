import os

API_NEDORIM = os.getenv("API_NEDORIM")

if API_NEDORIM:
    print("API Keys נטענו בהצלחה!")
else:
    print("שגיאה: לא נמצאו משתני סביבה.")
