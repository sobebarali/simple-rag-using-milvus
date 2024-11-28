from pymilvus import MilvusClient
from config import MILVUS_URI, COLLECTION_NAME, MILVUS_USER, MILVUS_PASSWORD, MILVUS_TOKEN

#Initialize Milvus client
milvus_client = MilvusClient(uri=MILVUS_URI, user=MILVUS_USER, password=MILVUS_PASSWORD, token=MILVUS_TOKEN)

def create_collection(embedding_dim):
    if milvus_client.has_collection(COLLECTION_NAME):
        milvus_client.drop_collection(COLLECTION_NAME)
    
    milvus_client.create_collection(
        collection_name=COLLECTION_NAME,
        dimension=embedding_dim,
        metric_type="IP",
        consistency_level="Strong",
    )

def search_collection(query_embedding, limit=3):
    return milvus_client.search(
        collection_name=COLLECTION_NAME,
        data=[query_embedding],
        limit=limit,
        search_params={"metric_type": "IP", "params": {}},
        output_fields=["text"],
    )