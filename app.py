import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Personalized Billing Assistance",
    page_icon="⚡",
    layout="wide"
)

st.title("Personalized Billing Assistance")
st.subheader("Your AI-powered Electricity Bill Assistant")

st.write(
    "Understand your electricity bills, "
    "monitor consumption and make smarter energy decisions."
)

st.divider()

bill_data={
    "Month":["July","August","September","October"],
    "Units":[180,220,195,260],
    "Bill Amount":[850,1050,930,1250]
}

df=pd.DataFrame(bill_data)

col1,col2,col3=st.columns(3)

with col1:
    st.metric("Latest Consumption","260 Units")

with col2:
     st.metric("Latest Bill", "₹1,250")

with col3:
    st.metric("Previous Consumption", "195 Units")

st.divider()

st.subheader("Monthly Electricity Consumption")

fig=px.line(
    df,
    x="Month",
    y="Units",
    markers=True,
    title="Monthly Consumption Trend"
)

st.plotly_chart(fig,use_container_width=True)

st.subheader("Electricity Bill History")

st.dataframe(df, use_container_width=True)

st.divider()

st.subheader("Upload Your Electricity Bill")
uploaded_file=st.file_uploader(
    "Upload a bill image or PDF",
    type=["png","jpg","jpeg","pdf"]

)

if uploaded_file is not None:
    st.success("Bill uploaded successfully!")

    st.write("File name:",uploaded_file.name)
    st.write("File size:",uploaded_file.size,"bytes")

    st.info(
        "OCR extraction will be implemented in the future to extract data from the uploaded bill."
    )

st.divider()

st.caption(
    "Developed by Rajashekar @2026. All rights reserved."
)