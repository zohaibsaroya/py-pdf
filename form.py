from fpdf import FPDF
a=FPDF('l','mm','letter')
a.add_page()
a.set_font('times','B',10)
for i in range(1,41):
 a.cell(0,10,f'This is line {i} :A',ln=True)
a.output(' form.py')
