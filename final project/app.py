import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("HotelNames_filled.csv")
df.columns = ["Index", "HotelName", "HotelId", "Country"]
df = df.drop(columns=["Index"])
df["HotelName"] = df["HotelName"].str.strip()
df["Country"] = df["Country"].str.strip()

# Extract brands
brands = ["Oberoi", "Taj", "Mandarin", "St. Regis", "Soneva", "Viceroy", "Ritz", "Four Seasons"]
df["Brand"] = df["HotelName"].apply(
    lambda x: next((b for b in brands if b.lower() in x.lower()), "Other")
)
st.title("🏨 Global Luxury Hotels Dashboard")
st.write("Explore luxury hotels across countries and brands.")

# Filters
country_filter = st.selectbox("Select Country", ["All"] + sorted(df["Country"].unique()))
brand_filter = st.selectbox("Select Brand", ["All"] + sorted(df["Brand"].unique()))

filtered_df = df.copy()

if country_filter != "All":
    filtered_df = filtered_df[filtered_df["Country"] == country_filter]

if brand_filter != "All":
    filtered_df = filtered_df[filtered_df["Brand"] == brand_filter]

st.subheader("Filtered Hotels")
st.dataframe(filtered_df)
# Country distribution
st.subheader("Hotels per Country")
country_counts = df["Country"].value_counts()

fig, ax = plt.subplots(figsize=(12, 5))
sns.barplot(x=country_counts.index,
            y=country_counts.values,
            palette=sns.color_palette("viridis", len(country_counts)))
plt.xticks(rotation=90)
plt.title("Number of Luxury Hotels per Country")
st.pyplot(fig)

# Brand distribution
st.subheader("Brand Distribution")
brand_counts = df["Brand"].value_counts()

fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(x=brand_counts.index,
            y=brand_counts.values,
            palette=sns.color_palette("magma", len(brand_counts)))
plt.xticks(rotation=45)
plt.title("Hotel Brand Distribution")
st.pyplot(fig2)
st.subheader("📊 Key Insights")
st.write("""
- India and Mexico have many luxury hotels in this dataset.
- Maldives dominates ultra-luxury island resorts.
- Strong brand clusters: Oberoi (India), Soneva (Maldives), Ritz-Carlton Reserve (Mexico).
- Naming patterns show categories like Palace, Lodge, Boutique, Reserve.
""")
