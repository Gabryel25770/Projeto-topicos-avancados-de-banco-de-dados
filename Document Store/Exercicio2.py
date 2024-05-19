'''' Projeto Banco de dados:

Thiago Ayres Kimura - RA: 22.221.045-2
Giovanna Borges Tamagnini - RA: 22.221.016-3
Gabryel Lourenço Maciel de Morais - RA: 22.221.021-3 '''

from pymongo import MongoClient

def find_courses_by_semester_and_department(semester, department):
    # Conexão com o MongoDB
    mongo_client = MongoClient('localhost', 27017)
    mongo_db = mongo_client['ProjetoDB']

    # Buscando os IDs dos cursos ensinados no semestre especificado
    teaches_collection = mongo_db['teaches']
    teaches_filter = {"semester": semester}
    teaches_results = teaches_collection.find(teaches_filter)
    
    course_ids = [result['course_id'] for result in teaches_results]

    # Buscando os títulos dos cursos que pertencem ao departamento especificado
    course_collection = mongo_db['course']
    course_titles = []
    for course_id in course_ids:
        course_filter = {"course_id": course_id, "dept_name": department}
        course_results = course_collection.find(course_filter)
        for course in course_results:
            course_titles.append(course['title'])

    return course_titles

# Semestre e departamento a serem pesquisados
semester_to_search = 'Summer'
department_to_search = 'History'

# Chamando a função para encontrar e imprimir os títulos dos cursos
print(find_courses_by_semester_and_department(semester_to_search, department_to_search))
