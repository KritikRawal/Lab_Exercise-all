"""find BMI using body mass and height"""

print("Enter the body mass (in kg): ")
mass = float(input())
print("Enter the height (in metres): ")
height = float(input())
bmi = mass / (height ** 2)
print('the bmi is',bmi)
print()