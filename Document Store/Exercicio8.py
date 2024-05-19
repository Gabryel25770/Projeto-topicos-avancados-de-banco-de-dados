'''' Projeto Banco de dados:

Thiago Ayres Kimura - RA: 22.221.045-2
Giovanna Borges Tamagnini - RA: 22.221.016-3
Gabryel Lourenço Maciel de Morais - RA: 22.221.021-3 '''

from pymongo import MongoClient

def count_sections_in_classrooms():
    # Conexão com o MongoDB
    mongo_client = MongoClient('localhost', 27017)
    mongo_db = mongo_client['ProjetoDB']

    # Inicializando o dicionário para armazenar o número de seções por sala
    classrooms = {}
    
    # Buscando todas as salas e inicializando a contagem de seções como 0
    classroom_collection = mongo_db['classroom']
    classroom_results = classroom_collection.find()
    for classroom in classroom_results:
        classrooms[classroom['room_number']] = 0

    # Contando o número de seções em cada sala
    section_collection = mongo_db['section']
    for room_number in classrooms.keys():
        section_filter = {"room_number": room_number}
        section_results = section_collection.find(section_filter)
        for section in section_results:
            classrooms[room_number] += 1

    # Imprimindo o número de seções por sala
    for room_number, section_count in classrooms.items():
        print(f"{room_number}: {section_count}")

# Chamando a função para contar e imprimir o número de seções por sala
count_sections_in_classrooms()
