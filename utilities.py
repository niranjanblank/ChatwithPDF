from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def extract_data_from_pdfs(docs):
    """
    Extracts text from the pdf and return in a string
    """
    text_list = []
    for doc in docs:
        reader = PdfReader(doc)

        # iterating through pages and getting text
        for page in reader.pages:
            text_list.append(page.extract_text())

    return " ".join(text_list)


def create_text_chunks(data):
    """
    Chunks the string data and returns the chunks
    """
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n"],
        chunk_size=1000,
        chunk_overlap=200
    )
    text_chunks = text_splitter.split_text(data)
    return text_chunks
