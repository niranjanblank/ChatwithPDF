from pypdf import PdfReader

def extract_data_from_pdfs(docs):
    """
    Extracts text fron the pdf and return in a string
    """
    text_list = []
    for doc in docs:
        reader = PdfReader(doc)

        # iterating through pages and getting text
        for page in reader.pages:
            text_list.append(page.extract_text())

    return " ".join(text_list)