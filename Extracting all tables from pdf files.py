import pandas as pd
import tabula
tables = tabula.read_pdf(r"C:\Users\Cash\Documents\pruebas_python\proyectos\pdf\invoice.pdf", pages = "all")

df = pd.DataFrame(tables[0])

df