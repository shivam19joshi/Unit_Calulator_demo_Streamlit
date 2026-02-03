import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Car Horsepower Analysis", layout="wide")

st.title(" Car Model Analysis")
st.write("Select a car brand to visualize model-wise horsepower")

# Load data
df = pd.read_csv("CARS.csv")

# Brand selection
brand = st.selectbox(
    "Select Car Brand",
    sorted(df["Make"].unique())
)

# Filter data
car = df[df["Make"] == brand]

# Optional: model multiselect
models = st.multiselect(
    "Select Models (optional)",
    car["Model"].unique(),
    default=car["Model"].unique()
)

car = car[car["Model"].isin(models)]

# Plot
if not car.empty:
    fig, ax = plt.subplots(figsize=(12, 6))
    sb.barplot(
        x=car["Model"],
        y=car["Horsepower"],
        palette="copper",
        ax=ax
    )
    ax.set_xlabel("Car Model")
    ax.set_ylabel("Horsepower")
    ax.set_title(f"Horsepower by Model – {brand}")
    plt.xticks(rotation=90)

    st.pyplot(fig)
else:
    st.warning("No data available for the selected filters.")
