'''' Projeto Banco de dados:

Thiago Ayres Kimura - RA: 22.221.045-2
Giovanna Borges Tamagnini - RA: 22.221.016-3
Gabryel Lourenço Maciel de Morais - RA: 22.221.021-3 '''

from pymongo import MongoClient

def count_advisees_per_professor():
    # Conexão com o MongoDB
    mongo_client = MongoClient('localhost', 27017)
    mongo_db = mongo_client['ProjetoDB']

    # Inicializando o dicionário para armazenar o número de aconselhados por professor
    professors = {}

    # Buscando todos os professores e inicializando a contagem de aconselhados como 0
    instructor_collection = mongo_db['instructor']
    instructor_results = instructor_collection.find()
    for instructor in instructor_results:
        professors[instructor['ID']] = 0

    # Contando o número de aconselhados para cada professor
    advisor_collection = mongo_db['advisor']
    for professor_id in professors.keys():
        advisor_filter = {"i_ID": professor_id}
        advisor_results = advisor_collection.find(advisor_filter)
        for _ in advisor_results:
            professors[professor_id] += 1

    # Imprimindo o número de aconselhados por professor
    for professor_id, advisee_count in professors.items():
        instructor_results = instructor_collection.find({'ID': professor_id})
        for instructor in instructor_results:
            print(f"{instructor['name']}: {advisee_count}")

# Chamando a função para contar e imprimir o número de aconselhados por professor
count_advisees_per_professor()
