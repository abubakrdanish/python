from fpdf import FPDF
import pandas as pd
pdf = FPDF(orientation="P", unit="mm",format="A4")
pdf.set_auto_page_break(auto=False,margin=0)
df = pd.read_csv("topics.csv")
for index, row in df.iterrows():

    pdf.add_page()

    pdf.set_font(family="Times",style="B",size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0,h=12,txt=row["Topic"], align="L",ln=1)
    pdf.line(10, 21,200, 21)
    y_position = 30
    for line_num in range(25):
        pdf.line(10, y_position, 200, y_position)
        y_position += 10
    pdf.ln(260)
    pdf.set_font(family="Times",style="I",size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
        pdf.line(10, 21, 200, 21)
        pdf.ln(260)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
        y_position = 30
        for line_num in range(25):
            pdf.line(10, y_position, 200, y_position)
            y_position += 10
pdf.output("output.pdf")