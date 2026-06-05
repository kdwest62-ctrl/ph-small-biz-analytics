import pandas as pd
from pathlib import Path

path = Path(input("CSV path: "))
if path.exists():
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
else:
    print("Path does not exist")
