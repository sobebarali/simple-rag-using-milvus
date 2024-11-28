import json
from glob import glob
from embedding import emb_text
from milvus_operations import create_collection, search_collection
from openai_operations import get_chat_response
from config import COLLECTION_NAME


def load_text_lines():
    text_lines = []
    for file_path in glob("data/milvus_docs/en/faq/*.md", recursive=True):
        with open(file_path, "r") as file:
            file_text = file.read()
        text_lines += file_text.split("# ")
    return text_lines

def main():
    text_lines = load_text_lines()
    test_embedding = emb_text("This is a test")
    embedding_dim = len(test_embedding)
    print(embedding_dim)
    print(test_embedding[:10])

    create_collection(embedding_dim)

    # Uncomment to insert data
    # data = [{"id": i, "vector": emb_text(line), "text": line} for i, line in enumerate(tqdm(text_lines, desc="Creating embeddings"))]
    # milvus_client.insert(collection_name=COLLECTION_NAME, data=data)

    question = "How is data stored in milvus?"
    search_res = search_collection(emb_text(question))

    retrieved_lines_with_distances = [
        (res["entity"]["text"], res["distance"]) for res in search_res[0]
    ]
    print(json.dumps(retrieved_lines_with_distances, indent=4))

    context = "\n".join(
        [line_with_distance[0] for line_with_distance in retrieved_lines_with_distances]
    )

    SYSTEM_PROMPT = """
    Human: You are an AI assistant. You are able to find answers to the questions from the contextual passage snippets provided.
    """
    USER_PROMPT = f"""
    Use the following pieces of information enclosed in <context> tags to provide an answer to the question enclosed in <question> tags.
    <context>
    {context}
    </context>
    <question>
    {question}
    </question>
    """

    response = get_chat_response(SYSTEM_PROMPT, USER_PROMPT)
    print(response)

if __name__ == "__main__":
    main()