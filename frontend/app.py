import streamlit as st
import requests

BACKEND_URL = "http://localhost:8000/api/summarize"

st.set_page_config(
    page_title="Terms & Conditions Summarizer",
    page_icon="📄",
    layout="centered"
)

st.title("📄 Terms & Conditions Summarizer")
st.write("Paste Terms & Conditions text OR provide a website URL to get a simplified summary.")

input_type = st.radio(
    "Choose input type:",
    ("Paste Text", "Website URL")
)

text = None
url = None

if input_type == "Paste Text":
    text = st.text_area(
        "Paste Terms & Conditions text here:",
        height=250
    )
else:
    url = st.text_input(
        "Enter Terms & Conditions website URL:"
    )

if st.button("Summarize"):
    if not text and not url:
        st.error("Please provide text or a URL.")
    else:
        payload = {
            "text": text,
            "url": url,
            "summary_type": "simple"
        }

        with st.spinner("Summarizing..."):
            response = requests.post(BACKEND_URL, json=payload)

        if response.status_code == 200:
            data = response.json()

            st.subheader("📌 Summary")
            st.write(data["summary"])

            st.subheader("🔑 Key Points")
            for point in data["key_points"]:
                st.markdown(f"- {point}")

            st.subheader("⚠️ Risk Notes")
            if data["risk_notes"]:
                for risk in data["risk_notes"]:
                    st.markdown(f"- {risk}")
            else:
                st.write("No major risks identified.")
        else:
            st.error("Something went wrong. Please try again.")
