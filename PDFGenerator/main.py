from fpdf import FPDF
import pandas as pd

df= pd.read_csv("topics.csv")

pdf= FPDF(orientation='P',unit='mm',format='A4')
pdf.set_auto_page_break(auto=False,margin=0)

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font('Times', 'B', size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align='L', ln=1, border=0)
    pdf.line(10,22,200,22)

    pdf.ln(260)
    for i in range(0,240,10):
        pdf.line(10, i+35, 200, i+35)




    pdf.set_font('Times', 'I', size=8)
    pdf.cell(w=0, h=10, txt=row["Topic"], align='R', ln=1, border=0)

    for i in range(row['Pages']-1):
        pdf.add_page()

        pdf.ln(260)
        for i in range(0, 240, 10):
            pdf.line(10, i + 35, 200, i + 35)

        pdf.set_font('Times', 'I', size=8)
        pdf.cell(w=0, h=10, txt=row["Topic"], align='R', ln=1, border=0)



pdf.output('output.pdf')