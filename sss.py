from fpdf import FPDF
a=FPDF('p','mm','letter')
a.add_page()
a.set_font('times','B',10)
for i in range(1,41):
 a.cell(0,10,f'This is line {i} :A',ln=True)
a.output('ssp.py')
