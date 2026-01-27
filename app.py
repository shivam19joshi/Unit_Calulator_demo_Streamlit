import streamlit as st

# Title
st.title("📏 Units Calculator")

# Class for unit conversions
class Units:
    @staticmethod
    def feet_to_inch(ft):
        return ft * 12

    @staticmethod
    def inch_to_feet(inch):
        return inch / 12


# Dropdown to select conversion type
option = st.selectbox(
    "Select Conversion",
    ("Feet to Inch", "Inch to Feet")
)

# Input and calculation
if option == "Feet to Inch":
    ft = st.number_input("Enter value in Feet", min_value=0.0, step=0.1)
    if st.button("Convert"):
        inch = Units.feet_to_inch(ft)
        st.success(f"Inches: {inch}")

elif option == "Inch to Feet":
    inch = st.number_input("Enter value in Inches", min_value=0.0, step=0.1)
    if st.button("Convert"):
        feet = Units.inch_to_feet(inch)
        st.success(f"Feet: {feet}")
