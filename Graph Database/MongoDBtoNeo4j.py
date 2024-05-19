from pymongo import MongoClient
from neo4j import GraphDatabase

# Configurar conexões com MongoDB e Neo4j
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["ProjetoDB"]
neo4j_driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "kimura0608"))

# Função para criar nós no Neo4j
def create_nodes(tx, collection_name, documents):
    for doc in documents:
        props = {k: v for k, v in doc.items() if k != "_id"}
        props_string = ", ".join([f"{k}: ${k}" for k in props])
        query = f"CREATE (n:{collection_name} {{{props_string}}})"
        tx.run(query, **props)

# Função para migrar uma coleção do MongoDB para Neo4j
def migrate_collection(collection_name):
    collection = mongo_db[collection_name]
    documents = list(collection.find())
    with neo4j_driver.session() as session:
        session.execute_write(create_nodes, collection_name, documents)

# Função principal para migrar todas as coleções
def migrate_all_collections():
    collections = mongo_db.list_collection_names()
    for collection_name in collections:
        migrate_collection(collection_name)
        print(f"Coleção '{collection_name}' migrada com sucesso.")

# Executar a migração
if __name__ == "__main__":
    migrate_all_collections()
    print("Migração concluída com sucesso.")
