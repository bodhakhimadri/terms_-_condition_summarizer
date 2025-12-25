import streamlit as st
import requests

# -------------------------------
# Configuration
# -------------------------------
API_URL = "http://127.0.0.1:8000/summarize"

st.set_page_config(
    page_title="T&C Summarizer",
    layout="centered"
)

# -------------------------------
# UI Header
# -------------------------------
st.title("📄 Terms & Conditions Summarizer")
st.write(
    "Paste **Terms & Conditions text** or provide a **URL**, and get a simplified summary using LLM."
)

# -------------------------------
# Input Section
# -------------------------------
input_type = st.radio(
    "Choose Input Type:",
    ["Text", "URL"]
)

text_input = None
url_input = None

if input_type == "Text":
    text_input = st.text_area(
        "Paste Terms & Conditions text here:",
        height=250
    )
else:
    url_input = st.text_input(
        "Enter Terms & Conditions URL:"
    )

summary_type = st.selectbox(
    "Select Summary Type:",
    ["simple", "simplified", "risk"]
)

# -------------------------------
# Submit Button
# -------------------------------
if st.button("🔍 Generate Summary"):
    if not text_input and not url_input:
        st.warning("Please provide text or a URL.")
    else:
        payload = {
            "text": text_input,
            "url": url_input,
            "summary_type": summary_type
        }

        try:
            with st.spinner("Summarizing..."):
                response = requests.post(API_URL, json=payload, timeout=60)

            if response.status_code == 200:
                data = response.json()

                st.success("Summary Generated Successfully!")

                # -------------------------------
                # Output Section
                # -------------------------------
                st.subheader("📝 Summary")
                st.write(data.get("summary", ""))

                if data.get("key_points"):
                    st.subheader("📌 Key Points")
                    for point in data["key_points"]:
                        st.write(f"- {point}")

                if data.get("risk_notes"):
                    st.subheader("⚠️ Risk Notes")
                    for risk in data["risk_notes"]:
                        st.write(f"- {risk}")

            else:
                st.error(f"API Error: {response.text}")

        except Exception as e:
            st.error(f"Connection error: {e}")
