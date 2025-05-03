
import streamlit as st
from fpdf import FPDF

# Sample ingredients list
ingredients = [
    {"name": "Sugar", "amount": "100g", "pantry": True},
    {"name": "Flour", "amount": "200g", "pantry": True},
    {"name": "Chicken Thighs", "amount": "2kg", "pantry": False},
    {"name": "Olive Oil", "amount": "1L", "pantry": True},
    {"name": "Garlic", "amount": "50g", "pantry": False},
]

st.title("Catering Shopping List Preview")
st.markdown("Check off pantry items you already have:")

# Track checked pantry items
checked = []
for ingredient in ingredients:
    label = f"{ingredient['amount']} {ingredient['name']}"
    if st.checkbox(label, key=ingredient['name']):
        checked.append(ingredient['name'])

# Filter ingredients for the PDF
filtered_ingredients = [
    ing for ing in ingredients
    if not (ing['pantry'] and ing['name'] in checked)
]

st.markdown("---")
st.header("Final Shopping List")
for ing in filtered_ingredients:
    st.write(f"- {ing['amount']} {ing['name']}")

# PDF export function
def create_pdf(ingredients):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Shopping List", ln=True, align="C")
    pdf.ln(10)
    for ing in ingredients:
        line = f"- {ing['amount']} {ing['name']}"
        pdf.cell(200, 10, txt=line, ln=True)
    pdf.output("shopping_list.pdf")

if st.button("Export to PDF"):
    create_pdf(filtered_ingredients)
    with open("shopping_list.pdf", "rb") as file:
        btn = st.download_button(
            label="Download PDF",
            data=file,
            file_name="shopping_list.pdf",
            mime="application/pdf"
        )
