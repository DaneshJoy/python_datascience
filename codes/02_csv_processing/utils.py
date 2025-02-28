

def calculate_bmi(h, w):
    h /= 100

    # Calculate BMI
    bmi = w / h**2
    bmi = round(bmi, 2)
    return bmi