from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.image("shirtificate.png",10,30,5)
pdf.cell(40, 10, " cs50 ")
pdf.output("tuto2.pdf")