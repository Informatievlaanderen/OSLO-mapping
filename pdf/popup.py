import fitz

def add_popup_annotation(pdf_path, output_path):
    doc = fitz.open(pdf_path)

    for page in doc:
        # Example of adding an annotation
        # Change the bbox values to the desired location on the page
        rect = fitz.Rect(20.16010093688965, 87.3530044555664, 40.95225524902344, 89.4498291015625)
        annot = page.add_text_annot(rect, "Dit is de inhoud van de pop-up", icon="Note")

        # Set the title of the popup
        annot.set_info(title="Titel")

    doc.save(output_path)
    doc.close()

pdf_file_path = 'OSLO-SensorenEnBemonstering.pdf'
output_path = 'popups.pdf'
add_popup_annotation(pdf_file_path, output_path)