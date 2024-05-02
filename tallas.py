
def genTalla(medida):
    medida = int(medida)
    
    tallas = {
        12: [19, 50000],
        13: [20, 52000],
        14: [21, 57000],
        15: [22, 60000],
        16: [23, 90000],
        17: [24, 92000],
        18: [25, 95000],
        19: [26, 100000]
    }
    
    return tallas.get(medida)
