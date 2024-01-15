def calculate_bmi(weight, height):
    """
    Calculate BMI and classify into categories.

    :param weight: Weight in kilograms
    :param height: Height in meters
    :return: BMI value and corresponding category
    """
    bmi = weight / (height ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    return bmi, category


def main():
    print("BMI Calculator")
    print("---------------")
    
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
    except ValueError:
        print("Invalid input. Please enter numerical values for weight and height.")
        return
    
    if weight <= 0 or height <= 0:
        print("Invalid input. Weight and height must be positive values.")
        return
    
    bmi, category = calculate_bmi(weight, height)
    
    print("\nBMI Result:")
    print("------------")
    print(f"Weight: {weight} kg")
    print(f"Height: {height} m")
    print(f"BMI: {bmi:.2f}")
    print("Category: " + category)


if __name__ == "__main__":
    main()
