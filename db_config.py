from DAL.ObjectManager import ObjectManager, DBManager

db_config = {
    "dbname": "db_test1",
    "user": "postgres",
    "password": "postgresql",
    "host": "localhost",
    "port": "5432",
}

db_manager = DBManager(db_config)
object_manager = ObjectManager(db_manager)
