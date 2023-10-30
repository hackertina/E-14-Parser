import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf, output_folder):
    # Create a folder to store the resulting PDFs
    os.makedirs(output_folder, exist_ok=True)

    # Open the input PDF file
    with open(input_pdf, 'rb') as pdf_file:
        pdf_reader = PdfReader(pdf_file)
        
        # Iterate through each page
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer = PdfWriter()
            pdf_writer.add_page(pdf_reader.pages[page_num])

            # Save the page as a separate PDF
            output_pdf = os.path.join(output_folder, f'page_{page_num+1}.pdf')
            with open(output_pdf, 'wb') as output_file:
                pdf_writer.write(output_file)

input_pdf = 'e14_project/data/example.pdf'
output_folder = 'e14_project/data/example'

split_pdf(input_pdf, output_folder)
