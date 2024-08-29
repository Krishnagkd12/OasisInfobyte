def calculate_bmi(weight, height):
    """Calculate BMI given weight in kilograms and height in meters."""
    bmi = weight / (height ** 2)
    return bmi

def bmi_category(bmi):
    """Determine the BMI category based on the calculated BMI."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    try:
        # Get user input for weight (in kg) and height (in meters)
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (m): "))

        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Determine BMI category
        category = bmi_category(bmi)

        # Print the results
        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")

if __name__ == "__main__":
   main()