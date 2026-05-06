# business_logic/revenue_at_risk.py

def calculate_revenue_at_risk(monthly_revenue: float, churn_probability: float):
    """
    Menghitung potensi kerugian finansial (Revenue at Risk) 
    berdasarkan pendapatan bulanan dan probabilitas churn.
    """
    
    # Perkalian sederhana: Revenue x Probabilitas
    rev_at_risk = monthly_revenue * churn_probability
    
    # Kita bulatkan ke 2 angka di belakang koma (atau sesuai mata uang)
    return round(rev_at_risk, 2)