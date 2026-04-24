COST = 57.23

def calculate_total(qty, gold_customer):
    qty = abs(qty)

    if qty == 0:
        return 0, "No quantity discount"

    if gold_customer:
        if qty < 25:
            total = (COST * qty) * 0.965
            message = "Gold discount of 3.5% applied. No quantity discount"
        elif qty < 100:
            total = (COST * qty) * 0.915
            message = "Gold discount of 3.5% applied, quantity discount of 5%"
        else:
            total = (COST * qty) * 0.865
            message = "Gold discount of 3.5% applied, quantity discount of 10%"
    else:
        total = COST * qty
        message = "No quantity discount applied"

    return round(total, 2), message