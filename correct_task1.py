def calculate_average_order_value(orders):
    total = 0
    count = 0

    for order in orders:
        if isinstance(order["amount"], (int, float)):
            total += order["amount"]
            count += 1

    
    if count == 0:
        return 0

    return total / count

