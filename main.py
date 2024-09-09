import PyPDF2

# a = PyPDF2.PdfReader('sample.pdf')
# print(a.documentInfo)
# print(a.getNumPages())
# print(a.getPage(2))
# import PyPDF2  # type: ignore

# Use PdfReader instead of PdfFileReader
a = PyPDF2.PdfReader('sample.pdf')

# Print document information
print(a.metadata)

# Print the number of pages
print(len(a.pages))

# Get and print the content of the third page (index 2)
page = a.pages[1]
print(page.extract_text())
