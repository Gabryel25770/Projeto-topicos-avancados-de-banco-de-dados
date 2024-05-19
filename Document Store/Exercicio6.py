'''' Projeto Banco de dados:

Thiago Ayres Kimura - RA: 22.221.045-2
Giovanna Borges Tamagnini - RA: 22.221.016-3
Gabryel Lourenço Maciel de Morais - RA: 22.221.021-3 '''

from pymongo import MongoClient

def find_courses_taught_by_professor_in_semester(professor_id, semester):
    # Conexão com o MongoDB
    mongo_client = MongoClient('localhost', 27017)
    mongo_db = mongo_client['ProjetoDB']

    # Buscando os cursos ensinados pelo professor no semestre especificado
    teaches_collection = mongo_db['teaches']
    filter_query = {"semester": semester, "ID": professor_id}
    results = teaches_collection.find(filter_query)

    # Imprimindo os IDs dos cursos
    for result in results:
        print(result['course_id'])

# ID do professor e semestre a serem pesquisados
professor_id_to_search = "76766"
semester_to_search = "Summer"

# Chamando a função para encontrar e imprimir os IDs dos cursos
find_courses_taught_by_professor_in_semester(professor_id_to_search, semester_to_search)
