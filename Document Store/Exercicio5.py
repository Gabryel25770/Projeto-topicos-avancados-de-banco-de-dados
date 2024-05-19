'''' Projeto Banco de dados:

Thiago Ayres Kimura - RA: 22.221.045-2
Giovanna Borges Tamagnini - RA: 22.221.016-3
Gabryel Lourenço Maciel de Morais - RA: 22.221.021-3 '''

from pymongo import MongoClient

def find_total_credits_by_student_name(student_name):
    # Conexão com o MongoDB
    mongo_client = MongoClient('localhost', 27017)
    mongo_db = mongo_client['ProjetoDB']

    # Buscando o aluno pelo nome especificado
    student_collection = mongo_db['student']
    filter_query = {"name": student_name}
    results = student_collection.find(filter_query)

    # Imprimindo o total de créditos do aluno
    for result in results:
        print(result['tot_cred'])

# Nome do aluno a ser pesquisado
student_name_to_search = "Snow"

# Chamando a função para encontrar e imprimir o total de créditos do aluno
find_total_credits_by_student_name(student_name_to_search)
