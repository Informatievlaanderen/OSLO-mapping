import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    # Open the PDF
    doc = fitz.open(pdf_path)
    text = ''

    # Extract text from each page
    for page in doc:
        text += page.get_text()

    doc.close()
    return text

# Example usage
pdf_file_path = 'OSLO-SensorenEnBemonstering.pdf'
extracted_text = extract_text_from_pdf(pdf_file_path)
print(extracted_text)