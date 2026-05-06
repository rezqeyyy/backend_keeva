import shap
import pandas as pd
import numpy as np

explainer = None
feature_order = []

def init_explainer(model, feat_order):
    global explainer, feature_order
    feature_order = feat_order
    
    # KernelExplainer cocok untuk semua model termasuk StackingClassifier
    # Butuh background data — kita pakai data dummy (zeros)
    background = pd.DataFrame(
        np.zeros((50, len(feat_order))), 
        columns=feat_order
    )
    
    explainer = shap.KernelExplainer(
        lambda x: model.predict_proba(pd.DataFrame(x, columns=feat_order))[:, 1],
        background
    )

def get_shap_explanation(df_input, feat_order):
    shap_values = explainer.shap_values(df_input, nsamples=100)
    
    vals = shap_values[0] if len(shap_values.shape) > 1 else shap_values
    
    factors = sorted(
        [{"feature": feat_order[i], "shap_value": round(float(vals[i]), 4)} 
         for i in range(len(feat_order))],
        key=lambda x: abs(x["shap_value"]), reverse=True
    )
    return factors[:5]