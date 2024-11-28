# Milvus OpenAI Integration

This project integrates Milvus, a vector database, with OpenAI's API to perform semantic search and retrieve relevant information from a collection of text documents. The application loads text data, creates embeddings using OpenAI, stores them in Milvus, and allows for efficient search and retrieval.

## Features

- Load and process text data from markdown files.
- Create embeddings using OpenAI's API.
- Store and manage embeddings in Milvus.
- Perform semantic search to retrieve relevant text snippets.
- Generate responses using OpenAI's chat model.

## Prerequisites

- Python 3.7 or higher
- Docker (for running Milvus)
- OpenAI API key
- Milvus server running locally or accessible remotely

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/sobebarali/rag-with-milvus.git
   cd rag-with-milvus
   ```

2. **Install dependencies:**

   Create and activate a virtual environment, then install the required packages:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**

   Create a `.env` file in the root directory and add the following variables:

   ```plaintext
   OPENAI_API_KEY=your_openai_api_key
   MILVUS_URI=http://localhost:19530
   COLLECTION_NAME=test_collection
   MILVUS_USER=test_user
   MILVUS_PASSWORD=test_password
   MILVUS_TOKEN=test_token
   ```

4. **Run Milvus:**

   Ensure Milvus is running. You can use Docker to start a Milvus instance:

   ```bash
   docker run -d --name milvus -p 19530:19530 milvusdb/milvus:latest
   ```

## Usage

1. **Run the main script:**

   Execute the main script to load data, create embeddings, and perform a search:

   ```bash
   python src/main.py
   ```

2. **Modify and extend:**

   - Update the text data in the `data/milvus_docs/en/faq/` directory as needed.
   - Adjust the search query in `src/main.py` to test different questions.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Milvus](https://milvus.io/) for providing a powerful vector database.
- [OpenAI](https://openai.com/) for their advanced AI models and APIs.
