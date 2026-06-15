import pandas as pd
from pathlib import Path

path = Path(input("CSV path: "))
if path.exists():
    df = pd.read_csv(path)
    while True:
        print("Menu")
        print("1. Data\n2. Rankings\n3. Exit")
        option = input("Select option: ")
        if option == "1":
            print(df.to_string())
            print("-" * 8)
        elif option == "2":
            print("a. Sales\nb. Revenue\nc. Profit\nd. Inventory")
            rankings = input("Select rankings: ")
            if rankings == "a":
                sales = df.groupby("product")["quantity_sold"].sum().sort_values(ascending=False)
                print(sales)
                print("-" * 8)
            elif rankings == "b":
                pass
            elif rankings == "c":
                pass
            elif rankings == "d":
                pass
            else:
                print("Rankings not available")
        elif option == "3":
            print("Program closed")
            break
        else:
            print("Option not available")
else:
    print("Path does not exist")
