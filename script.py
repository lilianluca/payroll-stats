import os
import fitz
import pytesseract
from dotenv import load_dotenv
from pdf2image import convert_from_bytes

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
load_dotenv()

PDF_PASSWD = os.getenv("PDF_PASSWD")
FILE_PATH = "Vyplatni_paska_Luca_Lilian_082024.pdf"

# Open and authenticate the PDF
pdf = fitz.open(FILE_PATH)
if pdf.is_encrypted:  # Use is_encrypted instead of isEncrypted
    if not pdf.authenticate(PDF_PASSWD):
        print("Failed to decrypt the PDF. Check the password.")
        exit()


pdf_bytes = pdf.write()  # Get bytes of the decrypted PDF
pages = convert_from_bytes(pdf_bytes)
text = ""
for page in pages:
    text += pytesseract.image_to_string(page, lang="ces")

print(text)



