import fitz

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

data_output = []

# Print results
for data in extracted_data:
    data_output.append({
        "page": data['page'], 
        "text": data['text'], 
        "bbox": data['bbox']
    })
    if str(data['text']).startswith("0") or str(data['text']).startswith("1"):
        continue
    if not any(char.isalpha() for char in data['text']):
        continue
    word_list = ["enumeration", "dataType", "::", "OSLO-Generiek", "disjoint", "(", ")"]
    if any(word in data['text'] for word in word_list):
        continue
    char_list = ['^', ':', '+']
    if data['text'][0] in char_list:
        data['text'] = data['text'][1:]
    else:
        print(f"Page: {data['page']}, Text: {data['text']}, BBox: {data['bbox']}")

# Optionally, save the extracted text and locations to a file
with open('extracted_text_and_locations.txt', 'w', encoding='utf-8') as f:
    for data in extracted_data:
        f.write(f"Page: {data['page']}, Text: {data['text']}, BBox: {data['bbox']}\n")


def add_legend_to_pdf(pdf_path, data):
    doc = fitz.open(pdf_path)
    link_dict = {}

    for entry in data:
        page_number = entry['page'] - 1
        text = entry['text']
        bbox = fitz.Rect(entry['bbox'])  # Ensure bbox is a fitz.Rect object

        # Create a link target for each text
        link_dict[(page_number, text)] = doc[page_number].insert_link({
            'kind': 1,  # GoToR link kind
            'from': bbox,  # link rectangle
            'page': page_number,  # target page number
            'zoom': 0  # keep current zoom
        })

    # Adding a new page for the legend
    legend_page = doc.new_page(-1)

    # Formatting the legend
    legend_text = "Legends:\n\n"
    for i, (key, value) in enumerate(link_dict.items()):
        page_num, text = key
        legend_text += f"{i+1}. Page: {page_num+1}, Text: {text}, Link: {value}\n"

    legend_page.insert_text((50, 50), legend_text, fontsize=12)

    # Save the modified PDF
    doc.save("modified_pdf_with_legend.pdf")
    doc.close()



add_legend_to_pdf(pdf_file_path, data_output)
