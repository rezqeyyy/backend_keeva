def get_churn_reasons(data):
    reasons = []
    
    # 1. NPS Logic (Revised thresholds)
    if data.get("minimum_nps_score", 10) <= 4:
        reasons.append("Low customer satisfaction levels (Low Minimum NPS score)")
    
    if data.get("maximum_nps_score", 10) <= 6:
        reasons.append("Even the highest satisfaction scores remain below target levels")
        
    # 2. Inactivity (Revised threshold: > 20 days)
    if data.get("inactivity_days", 0) > 20:
        reasons.append("Customer has been inactive for more than 20 days")
        
    # 3. Payment Risk Score
    if data.get("payment_risk_score", 0) > 0.75:
        reasons.append("High risk detected in customer payment patterns")
        
    # 4. Technical Tickets
    if data.get("count_ticket_id_Technical", 0) > 5:
        reasons.append("Excessive technical issues reported by the customer")
        
    # 5. Composite Risk
    if data.get("composite_risk", 0) > 0.7:
        reasons.append("Accumulated behavioral indicators suggest high churn risk")

    # Fallback Reason
    if not reasons:
        reasons.append("Customer behavior is currently within normal parameters")
        
    return reasons[:3]