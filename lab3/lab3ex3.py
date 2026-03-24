def normalizare(data):
    min_val = min(data)
    max_val = max(data)
    if max_val - min_val == 0:
        return [0] * len(data)  # Evită împărțirea la zero
    return [(x - min_val) / (max_val - min_val) for x in data]
    
    
data=[1, 2, 3, 4, 8]
print(normalizare(data))