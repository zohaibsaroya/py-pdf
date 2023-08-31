from fpdf import FPDF
a=FPDF('l','mm','letter')
a.add_page()
a.set_font('times','I',20)
a.set_text_color(100,70,50)
a.cell(90,20,'Hi Zohaib',ln=True)

a.set_font('helvetica','B',10)
a.cell(3,4,'How Are You')
a.output('pdf form')