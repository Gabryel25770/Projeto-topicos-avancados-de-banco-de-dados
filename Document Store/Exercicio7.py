'''' Projeto Banco de dados:

Thiago Ayres Kimura - RA: 22.221.045-2
Giovanna Borges Tamagnini - RA: 22.221.016-3
Gabryel Lourenço Maciel de Morais - RA: 22.221.021-3 '''

from pymongo import MongoClient

def find_students_advised_by_professor(professor_name):
    # Conexão com o MongoDB
    mongo_client = MongoClient('localhost', 27017)
    mongo_db = mongo_client['ProjetoDB']

    # Buscando o ID do professor pelo nome
    instructor_collection = mongo_db['instructor']
    instructor_filter = {"name": professor_name}
    instructor_results = instructor_collection.find(instructor_filter)

    professor_ids = [str(result['ID']) for result in instructor_results]

    # Buscando os IDs dos alunos que são aconselhados pelo professor
    advisor_collection = mongo_db['advisor']
    student_ids = []
    for professor_id in professor_ids:
        advisor_filter = {"i_ID": professor_id}
        advisor_results = advisor_collection.find(advisor_filter)
        student_ids.extend([result['s_ID'] for result in advisor_results])

    # Buscando e imprimindo os nomes dos alunos
    student_collection = mongo_db['student']
    for student_id in student_ids:
        student_filter = {"ID": student_id}
        student_results = student_collection.find(student_filter)
        for student in student_results:
            print(student['name'])

# Nome do professor a ser pesquisado
professor_name_to_search = "Katz"

# Chamando a função para encontrar e imprimir os nomes dos alunos aconselhados pelo professor
find_students_advised_by_professor(professor_name_to_search)
