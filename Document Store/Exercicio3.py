'''' Projeto Banco de dados:

Thiago Ayres Kimura - RA: 22.221.045-2
Giovanna Borges Tamagnini - RA: 22.221.016-3
Gabryel Lourenço Maciel de Morais - RA: 22.221.021-3 '''

from pymongo import MongoClient

def find_students_by_department(department):
    # Conexão com o MongoDB
    mongo_client = MongoClient('localhost', 27017)
    mongo_db = mongo_client['ProjetoDB']

    # Buscando os alunos que pertencem ao departamento especificado
    student_collection = mongo_db['student']
    filter_query = {"dept_name": department}
    results = student_collection.find(filter_query)

    # Imprimindo os nomes dos alunos
    for result in results:
        print(result['name'])

# Departamento a ser pesquisado
department_to_search = "History"

# Chamando a função para encontrar e imprimir os nomes dos alunos
find_students_by_department(department_to_search)
