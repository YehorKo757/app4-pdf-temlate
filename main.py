from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

data = pd.read_csv("topics.csv")

for index, row in data.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L",
             ln=1, border=0)

    for y in range(21,298,10):
        pdf.line(x1=10, y1=y, x2=200, y2=y)

    # Set the footer for master page
    pdf.ln(267)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R",
             ln=1, border=0)

    for i in range(0,row["Pages"]-1):
        pdf.add_page()

        for y in range(21, 298, 10):
            pdf.line(x1=10, y1=y, x2=200, y2=y)
        # Set the footer for other pages
        pdf.ln(279)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R",
                 ln=1, border=0)


pdf.output("output.pdf")
