
# Will search your PDF file for the pages with the specified word in it
# Make sure to get rid of "" when putting in the path
import PyPDF2
x = "  sdf"
#You will need to use pip PyPDF2 to use this program 
def search_string_in_pdf(pdf_path, search_string):
    """Searches for a specific string in a PDF file and prints the page numbers where it's found."""
    try:
        with open(pdf_path, 'rb') as pdf_file_obj:
            pdf_reader = PyPDF2.PdfReader(pdf_file_obj)
            found = False
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text = page.extract_text()
                if search_string in text:
                    print(f"String '{search_string}' found on page {page_num + 1}")
                    found = True
            if not found:
                print(f"String '{search_string}' not found in the PDF.")
    except FileNotFoundError:
        print(f"Error: File not found at '{pdf_path}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
pdf_file_path =  str(input( r"Enter your PDF file path way: "))
while x != "":
    string_to_search = str(input("Enter what you want to find in this PDF: "))
    search_string_in_pdf(pdf_file_path, string_to_search)
    x = input("Press space to stop, anything else to continue: ")


