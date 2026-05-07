from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib

from business_logic.risk_scoring import get_risk_score_and_category
from business_logic.revenue_at_risk import calculate_revenue_at_risk
from business_logic.recommendation_engine import get_recommendation
from business_logic.explanation_rules import get_churn_reasons
from business_logic.early_warning import get_early_warning
from chatbot.chat_handler import handle_chat
from explainability.shap_explainer import init_explainer, get_shap_explanation

app = FastAPI()

# Enable CORS for Frontend connectivity
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "https://keeva-ai.vercel.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load Model with Dictionary Extraction
model_data = joblib.load("model/Model.pkl")
if isinstance(model_data, dict):
    model = next((v for v in model_data.values() if hasattr(v, "predict_proba")), list(model_data.values())[0])
else:
    model = model_data

# Load Metadata
metadata = joblib.load("preprocessing/preprocessing_pipeline.pkl")
FEATURE_ORDER = metadata.get('feature_cols', []) if isinstance(metadata, dict) else []

@app.post("/predict")
def predict_churn(customer_data: dict):
    cust_id = customer_data.get("customer_id", "Unknown-ID")
    
    # Preprocessing
    df_input = pd.DataFrame([customer_data])
    for col in FEATURE_ORDER:
        if col not in df_input.columns:
            df_input[col] = 0
    df_input = df_input[FEATURE_ORDER]
    
    # Model Inference
    churn_prob = model.predict_proba(df_input)[0][1]
    risk_info = get_risk_score_and_category(churn_prob)
    
    # Revenue Calculation
    revenue_val = customer_data.get("average_payment_value", customer_data.get("monthly_revenue", 0))
    rev_at_risk = calculate_revenue_at_risk(revenue_val, churn_prob)
    
    # Logic Modules
    warning_status = get_early_warning(customer_data, churn_prob)
    reasons = get_churn_reasons(customer_data)
    recommendation = get_recommendation(risk_info["risk_category"])
    
    # Priority Level Logic
    if rev_at_risk > 500000 or risk_info["risk_category"] == "High":
        priority = "High"
    elif rev_at_risk > 200000 or risk_info["risk_category"] == "Medium":
        priority = "Normal"
    else:
        priority = "Low"
    
    return {
        "customer_id": cust_id,
        "churn_probability": round(float(churn_prob), 4),
        "risk_score": round(float(risk_info["risk_score"]), 2),
        "risk_category": risk_info["risk_category"],
        "revenue_at_risk": round(float(rev_at_risk), 2),
        "priority_level": priority,
        "early_warning": warning_status,
        "recommendation": recommendation,
        "reasons": reasons
    }
    
# Inisialisasi SHAP setelah load model
init_explainer(model, FEATURE_ORDER)

@app.post("/chat")
def chat(payload: dict):
    customer_id = payload.get("customer_id")
    message = payload.get("message")
    churn_data = payload.get("churn_data")  # kirim hasil /predict dari frontend
    reply = handle_chat(customer_id, message, churn_data)
    return {"reply": reply}

@app.post("/explain")
def explain(customer_data: dict):
    df_input = pd.DataFrame([customer_data])
    for col in FEATURE_ORDER:
        if col not in df_input.columns:
            df_input[col] = 0
    df_input = df_input[FEATURE_ORDER]
    factors = get_shap_explanation(df_input, FEATURE_ORDER)
    return {"top_factors": factors}