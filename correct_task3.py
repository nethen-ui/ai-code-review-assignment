def average_valid_measurements(values):
    total = 0
    count = 0

    for v in values:
        if v is not None and isinstance(v, (int, float)):
            total += float(v)
            count += 1

            
    if count == 0:
        return 0

    return total / count

