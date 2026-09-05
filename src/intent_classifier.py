import re


def clean_text(text):
    """Clean incoming customer support text."""
    text = str(text).lower()

    text = re.sub(r"\S+@\S+", " ", text)
    text = re.sub(r"http\S+|www\S+", " ", text)

    text = text.replace("{product_purchased}", " ")

    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    return text


def classify_intent(text):
    """
    Classify a customer support message using
    transparent keyword-based rules.
    """

    text = clean_text(text)

    # Account Access
    if any(word in text for word in [
        "password",
        "invalid credentials",
        "login",
        "log in",
        "sign in",
        "account access",
        "unable to access",
        "can't access",
        "cannot access"
    ]):
        return "Account Access"

    # Billing / Payment
    if any(word in text for word in [
        "payment",
        "billing",
        "charged",
        "invoice",
        "billing address",
        "billing zip",
        "credit card",
        "debit card"
    ]):
        return "Billing / Payment"

    # Refund / Cancellation
    if any(word in text for word in [
        "refund",
        "money back",
        "reimbursement",
        "cancel",
        "cancellation",
        "return the item",
        "return product"
    ]):
        return "Refund / Cancellation"

    # Delivery
    if any(word in text for word in [
        "delivery",
        "shipping",
        "shipment",
        "delivered",
        "arrived",
        "tracking",
        "package",
        "order status"
    ]):
        return "Delivery"

    # Network / Connectivity
    if any(word in text for word in [
        "network",
        "wifi",
        "wi fi",
        "internet",
        "connection",
        "connect",
        "connecting",
        "connected",
        "router",
        "bluetooth"
    ]):
        return "Network / Connectivity"

    # Battery / Hardware
    if any(word in text for word in [
        "battery",
        "charging",
        "charger",
        "battery life",
        "not charging",
        "hardware",
        "broken",
        "damaged",
        "physical damage",
        "not turning on",
        "strange noises"
    ]):
        return "Battery / Hardware"

    # Software / Display
    if any(word in text for word in [
        "software",
        "bug",
        "crash",
        "application",
        "app",
        "program",
        "firmware",
        "update",
        "error",
        "not responding",
        "freezes",
        "screen",
        "display",
        "brightness",
        "resolution",
        "pixels"
    ]):
        return "Software / Display"

    # Default
    return "Installation / General Support"


if __name__ == "__main__":
    test_messages = [
        "My password is not working and I cannot login.",
        "My laptop will not connect to WiFi.",
        "The battery is not charging.",
        "I want a refund for my purchase.",
        "My screen is completely black.",
        "The application keeps crashing.",
        "Where is my shipment?"
    ]

    print("Testing intent classifier:\n")

    for message in test_messages:
        result = classify_intent(message)
        print("Message:", message)
        print("Intent:", result)
        print("-" * 50)