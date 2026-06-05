import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
print("1. CSV\n2. Sales\n3. Exit")
while True:
    option = input("Select option (number): ")
    if option == "1":
        print(df.to_string())
    elif option == "2":
        pass
    elif option == "3":
        print("Program closed")
        break
    else:
        print("Option not available")
