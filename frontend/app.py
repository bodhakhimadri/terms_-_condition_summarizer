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

# ---------- FORM (ENTER KEY WILL WORK NOW) ----------
with st.form("summarize_form"):
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

    submit = st.form_submit_button("Summarize")  # ENTER key triggers this

# ---------- PROCESS ----------
if submit:
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

            # ---------- SUMMARY ----------
            st.subheader("📌 Summary")
            st.write(data.get("summary", "No summary generated."))

            # ---------- KEY POINTS ----------
            st.subheader("🔑 Key Points")
            key_points = data.get("key_points", [])
            if key_points:
                for point in key_points:
                    st.markdown(f"- {point}")
            else:
                st.write("No key points found.")

            # ---------- RISK NOTES ----------
            st.subheader("⚠️ Risk Notes")
            risk_notes = data.get("risk_notes", [])
            if risk_notes:
                for risk in risk_notes:
                    st.markdown(f"- {risk}")
            else:
                st.write("No major risks identified.")

        else:
            st.error("Failed to connect to backend API.")
