import pandas as pd
from pathlib import Path

path = Path(input("CSV path: "))
if path.exists():
    df = pd.read_csv(path)
    column_data = df['product'].tolist()
    products = []
    for entry in column_data:
        if entry not in products:
            products.append(entry)
    quantity_sold = []
    for item in products:
        if column_data.count(item) > 1:
            product = df[df['product'] == item]
            quantity_sold.append(sum(product['quantity_sold'].tolist()))
        elif column_data.count(item) == 1:
            quantity_sold.append(df[df['product'] == item]['quantity_sold'].values[0])
    reference = dict(zip(products, quantity_sold))
    sorted_data = dict(sorted(reference.items(), key=lambda i: i[1], reverse=True))
    print("1. CSV\n2. Sales\n3. Revenue\n4. Exit")
    while True:
        option = input("Select option (number): ")
        if option == "1":
            print(df.to_string())
        elif option == "2":
            print("a. Full Rankings | b. Top-3 | c. Bottom-3")
            category = input("Choose category (letter): ")
            if category == "a":
                data = {"product": [k for k in sorted_data.keys()],
                        "quantity_sold": [v for v in sorted_data.values()]}
                result = pd.DataFrame(data)
                print(result.to_string())
            elif category == "b":
                top_3 = dict(list(sorted_data.items())[:3])
                data = {"product": [k for k in top_3.keys()],
                        "quantity_sold": [v for v in top_3.values()]}
                result = pd.DataFrame(data)
                print(result.to_string())
            elif category == "c":
                pass
            else:
                print("Option not available")
        elif option == "3":
            pass
        elif option == "4":
            print("Program closed")
            break
        else:
            print("Option not available")
else:
    print("Path does not exist")
