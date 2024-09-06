import PyPDF2

def extract_text_from_pdf(pdf_path):
    # PDF-Datei öffnen
    with open(pdf_path, "rb") as file:
        # PDF-Reader-Objekt erstellen
        pdf_reader = PyPDF2.PdfReader(file)

        # Anzahl der Seiten ermitteln
        num_pages = len(pdf_reader.pages)
        print(f"Die PDF hat {num_pages} Seiten.\n")

        # Inhalt jeder Seite auslesen
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()
            print(f"--- Seite {page_num + 1} ---\n")
            print(text)

# Beispielaufruf mit Pfad zur PDF-Datei
pdf_path = "dein-pdf-dokument.pdf"
extract_text_from_pdf(pdf_path)
