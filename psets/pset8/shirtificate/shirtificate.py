from fpdf import FPDF

name = input("Name: ")

pdf = FPDF()
pdf.add_page(orientation="portrait", format="A4")
pdf.set_font("helvetica", size=32)
pdf.cell(h = 40, text="CS50 Shirtificate", center=True)
pdf.image("shirtificate.png", x=10, y=50, w=190, h=200, keep_aspect_ratio=True)
pdf.set_text_color(255, 255, 255)
pdf.cell(h= 220, text=f"{name} took CS50", center=True)
pdf.output("shirtificate.pdf")
