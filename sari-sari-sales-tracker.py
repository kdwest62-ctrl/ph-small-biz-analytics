import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

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
        option = input("Option: ")
        if option == "1":
            print(df.to_string())
        elif option == "2":
            print("a. Daily Sales\nb. Product Sales")
            category = input("Category: ")
            if category == "a":
                print("i. Line Chart\nii. Pie Chart")
                chart = input("Chart: ")
                if chart == "i":
                    quantity_dict = df.groupby('date')['quantity_sold'].sum().to_dict()
                    x = [num for num in range(1, len(quantity_dict.keys()) + 1)]
                    y = [v for v in quantity_dict.values()]
                    plt.plot(x, y)
                    plt.show()
                elif chart == "ii":
                    pass
                else:
                    print("Chart not available")
            elif category == "b":
                print("i. Full Rankings\nii. Top-3\niii. Bottom 3")
                rankings = input("Rankings: ")
                if rankings == "i":
                    data = {"product": [k for k in sorted_data.keys()],
                            "quantity_sold": [v for v in sorted_data.values()]}
                    result = pd.DataFrame(data)
                    print(result.to_string())
                elif rankings == "ii":
                    top_3 = dict(list(sorted_data.items())[:3])
                    data = {"product": [k for k in top_3.keys()],
                            "quantity_sold": [v for v in top_3.values()]}
                    result = pd.DataFrame(data)
                    print(result.to_string())
                elif rankings == "iii":
                    bottom_3 = dict(list(sorted_data.items())[-3:])
                    data = {"product": [k for k in bottom_3.keys()],
                            "quantity_sold": [v for v in bottom_3.values()]}
                    result = pd.DataFrame(data)
                    print(result.to_string())
                else:
                    print("Rankings not available")
            elif category == "c":
                pass
            else:
                print("Category not available")
        elif option == "3":
            print("a. Product\nb. Daily Revenue\nc. Rankings")
            category = input("Category: ")
            if category == "a":
                pass
            elif category == "b":
                print("i. Line Chart\nii. Pie Chart")
                chart = input("Chart: ")
                if chart == "i":
                    pass
                elif chart == "ii":
                    pass
                else:
                    print("Chart not available")
            elif category == "c":
                print("i. Full Rankings\nii. Top-3\niii. Bottom 3")
                rankings = input("Rankings: ")
                if rankings == "i":
                    pass
                elif rankings == "ii":
                    pass
                elif rankings == "iii":
                    pass
                else:
                    print("Rankings not available")
            else:
                print("Category not available")
        elif option == "4":
            pass
        elif option == "5":
            pass
        elif option == "6":
            print("Program closed")
            break
        else:
            print("Option not available")
else:
    print("Path does not exist")
