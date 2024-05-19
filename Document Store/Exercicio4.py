'''' Projeto Banco de dados:

Thiago Ayres Kimura - RA: 22.221.045-2
Giovanna Borges Tamagnini - RA: 22.221.016-3
Gabryel Lourenço Maciel de Morais - RA: 22.221.021-3 '''

from pymongo import MongoClient

def calculate_average_salary_by_department(department):
    # Conexão com o MongoDB
    mongo_client = MongoClient('localhost', 27017)
    mongo_db = mongo_client['ProjetoDB']

    # Realizando a agregação para calcular a média do salário por departamento
    instructor_collection = mongo_db['instructor']
    aggregation_pipeline = [
        {'$match': {'dept_name': department}},
        {'$group': {'_id': None, 'average_salary': {'$avg': '$salary'}}}
    ]
    result = instructor_collection.aggregate(aggregation_pipeline)

    # Extraindo e imprimindo o resultado
    for doc in result:
        print("Média:", doc['average_salary'])

# Departamento para calcular a média do salário
department_to_search = "History"

# Chamando a função para calcular e imprimir a média do salário do departamento especificado
calculate_average_salary_by_department(department_to_search)
