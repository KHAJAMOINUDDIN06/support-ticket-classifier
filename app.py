import streamlit as st

from src.intent_classifier import classify_intent


# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Customer Support Ticket Classifier",
    page_icon="🎫",
    layout="centered"
)


# -----------------------------
# Header
# -----------------------------
st.title("🎫 Customer Support Ticket Classifier")

st.write(
    "An intelligent support-ticket intent classifier that "
    "categorizes customer messages into common support areas."
)

st.divider()


# -----------------------------
# Example tickets
# -----------------------------
st.subheader("💡 Try an Example")

examples = {
    "🔐 Account": "I forgot my password and cannot log into my account.",
    "💳 Payment": "I was charged twice for my purchase.",
    "💰 Refund": "I would like a refund for the product I purchased.",
    "📦 Delivery": "My package has not arrived yet and I need tracking information.",
    "📶 Network": "My laptop cannot connect to WiFi.",
    "🔋 Battery": "My device battery is not charging.",
    "💻 Software": "The application keeps crashing when I open it.",
    "🔧 Installation": "I need help installing the product."
}

selected_example = st.selectbox(
    "Choose an example ticket:",
    ["None"] + list(examples.keys())
)


# -----------------------------
# Input
# -----------------------------
st.subheader("📝 Customer Support Message")

default_text = ""

if selected_example != "None":
    default_text = examples[selected_example]

ticket_text = st.text_area(
    "Enter the customer's message:",
    value=default_text,
    placeholder="Example: My laptop cannot connect to WiFi...",
    height=160
)


# -----------------------------
# Classification
# -----------------------------
if st.button("🔍 Classify Ticket", type="primary"):

    if not ticket_text.strip():

        st.warning("Please enter a customer support message.")

    else:

        intent = classify_intent(ticket_text)

        st.success(
            f"### Predicted Category\n{intent}"
        )

        st.divider()

        st.subheader("📌 Classification Details")

        st.write(
            "The message was classified using transparent "
            "keyword-based intent detection."
        )

        st.write(
            "**Customer message:**"
        )

        st.info(ticket_text)


# -----------------------------
# Supported categories
# -----------------------------
st.divider()

st.subheader("📂 Supported Categories")

categories = [
    "Account Access",
    "Billing / Payment",
    "Refund / Cancellation",
    "Delivery",
    "Network / Connectivity",
    "Battery / Hardware",
    "Software / Display",
    "Installation / General Support"
]

for category in categories:
    st.write(f"• {category}")


# -----------------------------
# Dataset note
# -----------------------------
st.divider()

st.caption(
    "Note: The original dataset contains noisy/inconsistent labels. "
    "The final classifier therefore uses transparent intent rules "
    "rather than reporting misleading ML accuracy from leaked labels."
)