# Simple Interest Calculator

P = float(input("Enter the Principal amount: "))
R = float(input("Enter the Rate of interest (%): "))
T = float(input("Enter the Time (years): "))

SI = (P * R * T) / 100
print(f"Simple Interest = {SI}")
