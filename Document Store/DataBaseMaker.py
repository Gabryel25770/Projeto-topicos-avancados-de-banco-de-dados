'''' Projeto Banco de dados:

Thiago Ayres Kimura - RA: 22.221.045-2
Giovanna Borges Tamagnini - RA: 22.221.016-3
Gabryel Lourenço Maciel de Morais - RA: 22.221.021-3 '''

import sqlite3
from pymongo import MongoClient

def migrate_data_from_sqlite_to_mongodb(sqlite_table, mongo_collection, mapping):
    # Conexão com o MongoDB
    mongo_client = MongoClient('localhost', 27017)
    mongo_db = mongo_client['ProjetoDB']
    mongo_coll = mongo_db[mongo_collection]

    # Conexão com o SQLite
    sqlite_conn = sqlite3.connect('C:\\Users\\Thiago\\Documents\\DBProjeto.db')
    sqlite_cursor = sqlite_conn.cursor()

    sqlite_cursor.execute(f"SELECT * FROM {sqlite_table}")
    data_rows = sqlite_cursor.fetchall()

    for row in data_rows:
        document = {}
        for field, index in mapping.items():
            document[field] = row[index]
        mongo_coll.insert_one(document)

# Mapeamento das tabelas e campos
table_field_mapping = {
    "time_slot": {"time_slot_id": 0, "day": 1, "start_hr": 2, "start_min": 3, "end_hr": 4, "end_min": 5},
    "advisor": {"s_ID": 0, "i_ID": 1},
    "classroom": {"building": 0, "room_number": 1, "capacity": 2},
    "course": {"course_id": 0, "title": 1, "dept_name": 2, "credits": 3},
    "department": {"dept_name": 0, "building": 1, "budget": 2},
    "instructor": {"ID": 0, "name": 1, "dept_name": 2, "salary": 3},
    "prereq": {"course_id": 0, "prereq_id": 1},
    "section": {"course_id": 0, "sec_id": 1, "semester": 2, "year": 3, "building": 4, "room_number": 5, "time_slot_id": 6},
    "student": {"ID": 0, "name": 1, "dept_name": 2, "tot_cred": 3},
    "takes": {"ID": 0, "course_id": 1, "sec_id": 2, "semester": 3, "year": 4, "grade": 5},
    "teaches": {"ID": 0, "course_id": 1, "sec_id": 2, "semester": 3, "year": 4}
}

# Migrando os dados para o MongoDB
for sqlite_table, field_mapping in table_field_mapping.items():
    migrate_data_from_sqlite_to_mongodb(sqlite_table, sqlite_table, field_mapping)
