from fpdf import FPDF
pdf=FPDF('p','mm','letter')
pdf.add_page()
pdf.set_font('helvetica','U',18)
pdf.cell(40,10,'hello world',ln=True)
pdf.cell(70,12,'dddddddd')
pdf.output('zohaib.pdf')