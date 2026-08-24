def calculate_emi(p, r, y):
    """ 
    p = Principal loan amount
    r = Annual interest rate
    y = Loan duration in years
    """
    monthly_rate = r / (12 * 100)
    months = y * 12

    emi = (p * monthly_rate * (1 + monthly_rate) ** months) / \
          ((1 + monthly_rate) ** months - 1)

    return emi