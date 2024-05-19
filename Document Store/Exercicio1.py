'''' Projeto Banco de dados:

Thiago Ayres Kimura - RA: 22.221.045-2
Giovanna Borges Tamagnini - RA: 22.221.016-3
Gabryel Lourenço Maciel de Morais - RA: 22.221.021-3 '''

from pymongo import MongoClient

def find_and_print_courses_by_department(department_name):
    # Conexão com o MongoDB
    mongo_client = MongoClient('localhost', 27017)
    mongo_db = mongo_client['ProjetoDB']
    collection = mongo_db['course']

    # Definindo o filtro de busca
    filter_query = {"dept_name": department_name}

    # Realizando a consulta
    search_results = collection.find(filter_query)

    # Iterando sobre os resultados da consulta e imprimindo os títulos dos cursos
    for result in search_results:
        print(result['title'])

# Nome do departamento a ser pesquisado
department_name_to_search = "History"

# Chamando a função para encontrar e imprimir cursos pelo departamento
find_and_print_courses_by_department(department_name_to_search)
