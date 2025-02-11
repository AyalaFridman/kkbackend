from datetime import date


class KevaJson():
    Zeout:str #	מספר זהות
    ClientName :str #	שם לקוח
    Adresse :str #	כתובת מלאה
    City :str #	עיר
    Phone :str #	טלפון
    Mail :str #	מייל
    Amount :int #	סכום העסקה
    Currency :str #	מטבע (שקל 1 | דולר 2)
    Itra :int #	יתרת חיובים
    Success	:int #חיובים שבוצעו
    LastNum :str #	4 ספרות אחרונות
    CreationDate :date #תאריך חיוב ראשון
    NextDate :date #תאריך חיוב הבא
    ErrorText :str #פירוט שגיאת סירוב
    Groupe	:str #קטגוריה
    Comments:str #הערות
    MasofId	:str #מספר עמדה (לתרומות שהגיעו מבתי כנסת)
    Tokef:str #תוקף
    Enabled	:int #1 הוראה פעילה | 0 לא פעילה
    KevaId	:str #מזהה הוראת קבע בנדרים פלוס
    
class KevaId:
    KevaId:str #	מזהה הוראת קבע
    KevaStatus:int #	סטטוס הוראת קבע: 1 (פעילה) | 2 (מוקפאת) | 3 (נמחקה)
    KevaZeout:str #	מספר זהות
    KevaName:str #	שם לקוח
    KevaAdresse	:str #כתובת מלאה
    KevaCity:str #	עיר
    KevaPhone:str #	טלפון
    KevaMail:str #	מייל
    KevaGroupe:str #	קטגוריה
    KevaAvour	:str #הערה
    KevaAmount	:int #סכום חודשי לתשלום
    KevaCurrency	:int #מטבע (שקל 1 | דולר 2)
    KevaTashlumim:int #	יתרת חיובים
    KevaSuccess	:int #חיובים שבוצעו
    CreatedDate	:date #תאריך הקמה
    KevaAsToremCard:str #	האם יש לתורם כרטיס תורם
    KevaObservation:str #	הערות מערכת
    KevaNextDate	:date #תאריך חיוב הבא
    KevaFrequency:int #	תדירות גביה: 1 (חודשי) | 2 (שבועי) | 3 (יזכור)
    KevaLastNum:str #	4 ספרות אחרונות של הכרטיס אשראי
    KevaTokef:str #	תוקף כרטיס אשראי
    KevaCVV:str #	CVV (3 ספרות בגב הכרטיס)
    TotalHistoryAmount:int #	סכום שחוייב עד כה
    HistoryCount:int #	מספר פעמים שבוצע חיוב / ניסיון לחיוב
    
class History():
    Shovar:str #	מספר שובר בחברת האשראי
    Zeout:str #	מספר זהות
    ClientName:str #	שם לקוח
    Adresse:str #	כתובת מלאה
    Phone	:str #טלפון
    Mail	:str #מייל
    Amount	:int#סכום העסקה
    Currency:int #	מטבע (שקל 1 | דולר 2)
    TransactionTime	:date #תאריך ושעת ביצוע העסקה
    Confirmation :str #מספר אישור
    LastNum:str #	4 ספרות אחרונות
    TransactionType	:str #סוג עסקה (רגיל/תשלומים/הוראת קבע)
    Groupe:str #	קטגוריה
    Comments	:str #הערות
    Tashloumim:int #	מספר תשלומים (לחלק)
    FirstTashloum	:int #סכום תשלום ראשון (בעסקה בתשלומים בלבד)
    NextTashloum	:int #סכום שאר התשלומים
    CallId:str #	מזהה שיחה (לתרומות דרך נדרים פון)
    AsRecord	:int #אם התורם השאיר הקלטה = 1
    MasofId	:str #מספר עמדה (לתרומות שהגיעו מבתי כנסת)
    MasofName:str #	שם עמדה
    TransactionId:str #	מספר עסקה
    CompagnyCard:str #	מותג (לפי כללי שב"א)
    Solek	:str #סולק (לפי כללי שב"א)
    Tayar	:str #האם זה עסקה תייר (לא כדאי לסמוך על זה)
    KabalaId:str #	מספר קבלה
    KevaId	:str #מזהה הוראת קבע (לעסקאות הו"ק)