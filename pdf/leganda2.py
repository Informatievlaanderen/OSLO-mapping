import fitz  # PyMuPDF

def extract_text_and_locations(pdf_path):
    doc = fitz.open(pdf_path)
    result = []

    for page_number in range(len(doc)):
        page = doc.load_page(page_number)
        text_dict = page.get_text("dict")
        blocks = text_dict["blocks"]

        for block in blocks:
            if block["type"] == 0:  # Block contains text
                for line in block["lines"]:
                    for span in line["spans"]:
                        text = span["text"]
                        bbox = span["bbox"]  # Bounding box of the text (x0, y0, x1, y1)
                        result.append({
                            "page": page_number + 1,
                            "text": text,
                            "bbox": bbox
                        })

    doc.close()
    return result

# Example usage
pdf_file_path = 'OSLO-SensorenEnBemonstering.pdf'
extracted_data = extract_text_and_locations(pdf_file_path)

# Print results
for data in extracted_data:
    print(f"Page: {data['page']}, Text: {data['text']}, BBox: {data['bbox']}")

# Optionally, save the extracted text and locations to a file
with open('extracted_text_and_locations.txt', 'w', encoding='utf-8') as f:
    for data in extracted_data:
        f.write(f"Page: {data['page']}, Text: {data['text']}, BBox: {data['bbox']}\n")
