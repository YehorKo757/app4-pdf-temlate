import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("Invoices\\*.xlsx")

for filepath in filepaths:

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")

    pdf.set_font(family="times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1)

    pdf.set_font(family="times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date {date}", ln=1)
    pdf.ln(5)

    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    columns = [item.replace("_", " ").title() for item in df.columns]
    pdf.set_font(family="Times", size=10, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=str(columns[0]), ln=0, border=1)
    pdf.cell(w=65, h=8, txt=str(columns[1]), ln=0, border=1)
    pdf.cell(w=35, h=8, txt=str(columns[2]), ln=0, border=1)
    pdf.cell(w=30, h=8, txt=str(columns[3]), ln=0, border=1)
    pdf.cell(w=30, h=8, txt=str(columns[4]), ln=1, border=1)

    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["product_id"]), ln=0, border=1)
        pdf.cell(w=65, h=8, txt=str(row["product_name"]), ln=0, border=1)
        pdf.cell(w=35, h=8, txt=str(row["amount_purchased"]), ln=0, border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), ln=0, border=1)
        pdf.cell(w=30, h=8, txt=str(row["total_price"]), ln=1, border=1)

    total_sum = df["total_price"].sum()
    pdf.set_font(family="Times", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt="", ln=0, border=1)
    pdf.cell(w=65, h=8, txt="", ln=0, border=1)
    pdf.cell(w=35, h=8, txt="", ln=0, border=1)
    pdf.cell(w=30, h=8, txt="", ln=0, border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum), ln=1, border=1)

    # Add total sum sentence
    pdf.set_font(family="Times", size=12, style="B")
    pdf.cell(w=30, h=8, txt=f"The total price is {total_sum}", ln=1, border=0)

    # Add company name and logo
    pdf.set_font(family="Times", size=12, style="B")
    pdf.cell(w=30, h=8, txt=f"Company name", ln=0, border=0)
    pdf.image("pythonhow.png", w=10)


    pdf.output(f"PDFs\\{filename}.pdf")
