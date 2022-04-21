import tabula
# Read a PDF File
df = tabula.read_pdf("File.pdf", pages='all')[0]
tabula.convert_into("File.pdf", "file6.csv",
                    output_format="csv", pages='all')
