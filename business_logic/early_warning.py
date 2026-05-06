def get_early_warning(data, churn_prob):
    # Rule: Inactivity > 20 hari DAN churn probabilitas > 0.5 (Poin 7)
    inactivity = data.get("inactivity_days", 0)
    ticket_count = data.get("ticket_per_month", 0)
    
    if inactivity > 20 and (churn_prob > 0.5 or ticket_count > 5):
        return "⚠️ SEGERA HUBUNGI: Indikasi Churn Terdeteksi"
    return "Normal"