import os
from pdf2image import convert_from_path
import cairosvg

def convert_pdf_to_svg(pdf_file, output_folder):
    # Convert PDF to list of images
    images = convert_from_path(pdf_file)

    for i, image in enumerate(images):
        # Save image as PNG
        image_path = os.path.join(output_folder, f"page_{i}.png")
        image.save(image_path, 'PNG')

        # Convert PNG to SVG
        svg_path = os.path.join(output_folder, f"page_{i}.svg")
        cairosvg.svg2png(url=image_path, write_to=svg_path)

if __name__ == "__main__":
    pdf_file = 'OSLO-SensorenEnBemonstering.pdf'  # Replace with your PDF file path
    output_folder = '.'  # Replace with your desired output folder
    convert_pdf_to_svg(pdf_file, output_folder)
