def get_recommendation(risk_category: str):
    """
    Determines action items based on risk categories.
    """
    if risk_category == "High":
        return "Intensive Intervention: Initiate direct call and offer exclusive retention discounts."
    elif risk_category == "Medium":
        return "Soft Follow-up: Send a feedback survey and educational product newsletters."
    elif risk_category == "Low":
        return "Loyalty Program: Maintain service quality and offer periodic rewards."
    else:
        return "Standard Monitoring"