import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
menu = ["1. Data",
        "2. Data Aggregation",
        "3. Average Usage per Day Type",
        "4. Forecast Ingredient Needs",
        "5. Actual vs Predicted Usage",
        "6. Data Simulation"
        "7. Exit"]
for item in menu:
    print(item)
while True:
    option = input("Select option: ")
    if option == "1":
        print(df.to_string())
    elif option == "2":
        pass
    elif option == "3":
        pass
    elif option == "4":
        pass
    elif option == "5":
        pass
    elif option == "6":
        pass
    elif option == "7":
        print("Program closed")
        break
    else:
        print("Invalid input")
