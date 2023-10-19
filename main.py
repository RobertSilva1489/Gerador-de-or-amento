from fpdf import FPDF
pdf = FPDF()

projeto = input('Informe a descricao do projeto: ')
horas = input('Informe trabalhadas por dia de horas: ')
valor = input('Informe o valor hora trabalhada: ')
prazo = input('Informe o prazo(em dias): ')


total = int(horas) * float(valor) * int(prazo)
pdf.add_page()
pdf.set_font("Arial","",18)

pdf.image("template.png", x=0, y=0)

pdf.text(115,145,projeto)
pdf.text(115,160,horas + " horas")
pdf.text(115,175,valor + " reais")
pdf.text(115,190,prazo + " dias")
pdf.text(115,205,str(total)+" reais")

pdf.output("Orçamento.pdf")
print("Gerado com sucesso!")



