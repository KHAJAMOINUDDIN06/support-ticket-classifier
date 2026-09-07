import streamlit as st

from src.intent_classifier import classify_intent


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Customer Support AI",
    page_icon="🎫",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# HERO SECTION
# ============================================================

st.title("🎫 Customer Support AI")

st.subheader(
    "Intelligent Customer-Support Ticket Classification"
)

st.write(
    "Analyze customer messages and classify them into "
    "relevant support categories using NLP concepts "
    "and transparent intent detection."
)

st.write(
    "🐍 Python   •   🧠 NLP   •   📐 TF-IDF   •   "
    "⚡ Streamlit   •   🔍 Intent Classification"
)


# ============================================================
# PROJECT STATISTICS
# ============================================================

st.divider()

stat1, stat2, stat3, stat4 = st.columns(4)

with stat1:
    st.metric(
        label="Supported Intents",
        value="8"
    )

with stat2:
    st.metric(
        label="Text Processing",
        value="NLP"
    )

with stat3:
    st.metric(
        label="Classification",
        value="AI / ML"
    )

with stat4:
    st.metric(
        label="Deployment",
        value="Streamlit"
    )


# ============================================================
# CLASSIFICATION SECTION
# ============================================================

st.divider()

st.header("🔍 Classify a Support Ticket")

st.write(
    "Enter a customer message below and let the application "
    "identify the most relevant support category."
)


# ============================================================
# EXAMPLE TICKETS
# ============================================================

examples = {
    "🔐 Account Access":
        "I forgot my password and cannot log into my account.",

    "💳 Billing / Payment":
        "I was charged twice for my purchase.",

    "💰 Refund / Cancellation":
        "I would like a refund for the product I purchased.",

    "📦 Delivery":
        "My package has not arrived yet and I need tracking information.",

    "📶 Network / Connectivity":
        "My laptop cannot connect to WiFi.",

    "🔋 Battery / Hardware":
        "My device battery is not charging.",

    "💻 Software / Display":
        "The application keeps crashing when I open it.",

    "🔧 Installation / General":
        "I need help installing the product."
}


selected_example = st.selectbox(
    "💡 Try a sample ticket",
    ["None"] + list(examples.keys())
)


# ============================================================
# CUSTOMER MESSAGE
# ============================================================

if selected_example != "None":
    default_text = examples[selected_example]
else:
    default_text = ""


ticket_text = st.text_area(
    "📝 Customer Message",
    value=default_text,
    placeholder="Example: My laptop cannot connect to WiFi...",
    height=170
)


# ============================================================
# CLASSIFY BUTTON
# ============================================================

classify_button = st.button(
    "🚀 Classify Ticket",
    type="primary",
    use_container_width=True
)


# ============================================================
# PREDICTION RESULT
# ============================================================

if classify_button:

    if not ticket_text.strip():

        st.warning(
            "Please enter a customer support message "
            "before classifying."
        )

    else:

        intent = classify_intent(ticket_text)

        st.divider()

        st.header("🎯 Classification Result")

        st.success(
            f"Predicted Category: **{intent}**"
        )

        st.write(
            "The message was classified using transparent "
            "keyword-based intent detection."
        )

        with st.expander("📝 View Customer Message"):

            st.write(ticket_text)


# ============================================================
# SUPPORTED CATEGORIES
# ============================================================

st.divider()

st.header("📂 Supported Categories")

st.write(
    "The classifier supports eight common customer-support intents."
)


# First row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("🔐 **Account Access**")
    st.caption("Login, password and account access issues.")

with col2:
    st.info("💳 **Billing / Payment**")
    st.caption("Payments, charges and billing issues.")

with col3:
    st.info("💰 **Refund / Cancellation**")
    st.caption("Refunds, returns and cancellations.")

with col4:
    st.info("📦 **Delivery**")
    st.caption("Shipping, tracking and delivery issues.")


# Second row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("📶 **Network / Connectivity**")
    st.caption("WiFi, internet and connection problems.")

with col2:
    st.info("🔋 **Battery / Hardware**")
    st.caption("Battery, charging and hardware problems.")

with col3:
    st.info("💻 **Software / Display**")
    st.caption("Software, applications and display issues.")

with col4:
    st.info("🔧 **Installation / General Support**")
    st.caption("Installation and general support requests.")


# ============================================================
# HOW IT WORKS
# ============================================================

st.divider()

st.header("⚙️ How It Works")

st.write(
    "The application follows a simple three-step workflow."
)


step1, step2, step3 = st.columns(3)

with step1:

    st.subheader("1️⃣ Input")

    st.write(
        "Enter a customer support message or select "
        "one of the example tickets."
    )


with step2:

    st.subheader("2️⃣ Analyze")

    st.write(
        "The message is cleaned and checked against "
        "transparent intent-detection rules."
    )


with step3:

    st.subheader("3️⃣ Predict")

    st.write(
        "The application returns the most relevant "
        "customer-support category."
    )


# ============================================================
# ML APPROACH
# ============================================================

st.divider()

st.header("🧠 Machine Learning Approach")

st.write(
    "During development, several NLP-based machine-learning "
    "experiments were performed using TF-IDF and Scikit-learn."
)

ml1, ml2 = st.columns(2)

with ml1:

    st.info(
        "**Exploration**\n\n"
        "• Data cleaning\n"
        "• Exploratory Data Analysis\n"
        "• TF-IDF text features\n"
        "• Logistic Regression\n"
        "• Naive Bayes"
    )


with ml2:

    st.warning(
        "**Data Quality Finding**\n\n"
        "The dataset contained noisy/inconsistent labels "
        "and a target-leakage issue was identified during "
        "experimentation."
    )


st.write(
    "Because of these data-quality limitations, the final "
    "application uses transparent rule-based intent "
    "classification rather than reporting misleading ML accuracy."
)


# ============================================================
# TECHNOLOGIES
# ============================================================

st.divider()

st.header("🛠️ Technologies")

tech1, tech2, tech3, tech4 = st.columns(4)

with tech1:

    st.write("🐍 **Python**")
    st.write("📊 **Pandas**")
    st.write("🔢 **NumPy**")


with tech2:

    st.write("🧠 **NLP**")
    st.write("📐 **TF-IDF**")
    st.write("🤖 **Scikit-learn**")


with tech3:

    st.write("⚡ **Streamlit**")
    st.write("📦 **Git**")
    st.write("🐙 **GitHub**")


with tech4:

    st.write("🧹 **Data Cleaning**")
    st.write("🔎 **EDA**")
    st.write("⚠️ **Leakage Detection**")


# ============================================================
# PROJECT LINKS
# ============================================================

st.divider()

st.header("🔗 Project")

link1, link2 = st.columns(2)

with link1:

    st.link_button(
        "🐙 View GitHub Repository",
        "https://github.com/KHAJAMOINUDDIN06/support-ticket-classifier",
        use_container_width=True
    )


with link2:

    st.link_button(
        "🌐 Open Live Demo",
        "https://customer-support-ticket-classifier-khaja.streamlit.app",
        use_container_width=True
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🎫 Customer Support AI"
)

st.caption(
    "AI/ML Portfolio Project • Python • NLP • Streamlit"
)