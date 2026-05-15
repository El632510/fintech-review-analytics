import pandas as pd

def identify_theme(review):

    review = str(review).lower()

    # Account access issues
    if any(word in review for word in [
        "login",
        "log in",
        "password",
        "otp",
        "account locked",
        "verification"
    ]):
        return "Account Access Issues"

    # Transaction performance
    elif any(word in review for word in [
        "transfer",
        "transaction",
        "payment",
        "slow",
        "delay",
        "failed"
    ]):
        return "Transaction Performance"

    # UI & design
    elif any(word in review for word in [
        "interface",
        "design",
        "ui",
        "easy to use",
        "layout"
    ]):
        return "UI & Design"

    # Customer support
    elif any(word in review for word in [
        "support",
        "service",
        "help",
        "response",
        "customer care"
    ]):
        return "Customer Support"

    # Feature requests
    elif any(word in review for word in [
        "feature",
        "update",
        "fingerprint",
        "dark mode",
        "add"
    ]):
        return "Feature Requests"

    else:
        return "Other"