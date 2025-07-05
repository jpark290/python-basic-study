# Quiz) Calculate the standard weight based on height and gender

# Definition:
# * Standard weight: Appropriate weight based on a person's height.
# * Formula by gender:
#   - Male: height(m) × height(m) × 22
#   - Female: height(m) × height(m) × 21

# Requirements:
# 1. Calculation must be done inside a function
#    * Function name: std_weight
#    * Parameters: height (in cm), gender (string)
# 2. Result must be rounded to 2 decimal places

def std_weight(gender, height):
    height_m = height / 100  # Convert height from cm to meters
    if gender == "male":
        return round(height_m * height_m * 22, 2)
    else:
        return round(height_m * height_m * 21, 2)

# Example usage
height = 175
gender = "male"
weight = std_weight(gender, height)

print(f"A standard weight for a {gender} with height {height}cm is {weight}kg.")
# Output: A standard weight for a male with height 175cm is 67.38kg.
