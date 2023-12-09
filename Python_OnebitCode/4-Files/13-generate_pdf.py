import fpdf
from num2words import num2words
from datetime import datetime
currentDate = datetime.now()

formato_personalizado = "%Y-%m-%d"
data_formatada = currentDate.strftime(formato_personalizado)
print(data_formatada[8:])

cliente = input("Informe o nome do cliente")

referente = input("Informe o tipo de consulta")
value_recibo = input("Informe o valor da consulta")
value = f"{value_recibo} reais"
value_extenso = num2words(float(value_recibo), lang="pt-br")
value_extenso_msg = f"{value_extenso} reais"
PDF = fpdf.FPDF()
# Layout do recibo
PDF.add_page()
PDF.set_font("Arial","", 16)
PDF.image("./data/rec.jpg", x=0, y=0)
PDF.text(75, 86, cliente)
PDF.text(75, 112, value_extenso_msg)
PDF.text(75, 137, referente)
PDF.text(160, 44, value)
PDF.set_text_color(255,255,255)
PDF.text(30, 193, f"{data_formatada[8:]}        {data_formatada[5:7]}        {data_formatada[0:4]}")
arquivo = f"{cliente}_{datetime.now()}.pdf"
PDF.output(f"data/{arquivo}")
