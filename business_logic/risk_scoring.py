# business_logic/risk_scoring.py

def get_risk_score_and_category(churn_probability: float):
    
    # 1. Aturan konversi probability -> score (0-100)
    # Kita kalikan 100 dan bulatkan agar mudah dibaca di dashboard
    risk_score = round(churn_probability * 100, 2)
    
    # 2. Aturan kategori: High / Medium / Low
    # Sesuai instruksi BusinessLogic.pdf
    if risk_score >= 70:
        risk_category = "High"
    elif 40 <= risk_score < 70:
        risk_category = "Medium"
    else:
        risk_category = "Low"
        
    # Output harus seragam untuk kebutuhan API
    return {
        "risk_score": risk_score,
        "risk_category": risk_category
    }