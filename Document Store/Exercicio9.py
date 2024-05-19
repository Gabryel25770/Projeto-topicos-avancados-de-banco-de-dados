'''' Projeto Banco de dados:

Thiago Ayres Kimura - RA: 22.221.045-2
Giovanna Borges Tamagnini - RA: 22.221.016-3
Gabryel Lourenço Maciel de Morais - RA: 22.221.021-3 '''

from pymongo import MongoClient

def find_courses_with_specific_prerequisite(prereq_id):
    # Conexão com o MongoDB
    mongo_client = MongoClient('localhost', 27017)
    mongo_db = mongo_client['ProjetoDB']

    # Buscando os cursos que têm o pré-requisito específico
    prereq_collection = mongo_db['prereq']
    prereq_filter = {"prereq_id": prereq_id}
    prereq_results = prereq_collection.find(prereq_filter)

    course_ids = [result['course_id'] for result in prereq_results]

    # Buscando e imprimindo os títulos dos cursos correspondentes
    course_collection = mongo_db['course']
    for course_id in course_ids:
        course_filter = {"course_id": course_id}
        course_results = course_collection.find(course_filter)
        for course in course_results:
            print(course['title'])

# ID do curso específico a ser pesquisado como pré-requisito
specific_prereq_id = "CS-101"

# Chamando a função para encontrar e imprimir os títulos dos cursos
find_courses_with_specific_prerequisite(specific_prereq_id)
