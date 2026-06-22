from pathlib import Path
import pandas as pd
import numpy as np

path = Path(input('CSV path: '))
if path.exists():
    if path.suffix == '.csv':
        check_csv = pd.read_csv(path, nrows=0)
        required_columns = ['date', 'product', 'quantity_sold', 'price']
        all_exist = set(required_columns).issubset(check_csv.columns)
        if all_exist:
            df = pd.read_csv(path)
            print(df.to_string())
            start_index = int(input('Start date (number): '))
            end_index = int(input('End date (number): '))
            end_index += 1
            new_df = df.iloc[start_index:end_index].copy()
            products = []
            column_data = new_df['product'].tolist()
            for entry in column_data:
                if entry not in products:
                    products.append(entry)
            quantity_sold = []
            prices = []
            for product in products:
                if column_data.count(product) > 1:
                    prod = new_df[new_df['product'] == product]
                    sales = prod['quantity_sold'].tolist()
                    price = prod['price'].tolist()
                    quantity_sold.append(sum(sales))
                    prices.append(price[0])
                elif column_data.count(product) == 1:
                    sales = new_df[new_df['product'] == product]['quantity_sold'].values[0]
                    price = new_df[new_df['product'] == product]['price'].values[0]
                    quantity_sold.append(sales)
                    prices.append(price)
            arr1 = np.array(quantity_sold)
            arr2 = np.array(prices)
            sales = np.multiply(arr1, arr2)
            ref1 = dict(zip(products, quantity_sold))
            ref2 = dict(zip(products, prices))
            ref3 = dict(zip(products, sales))
            print('Menu')
            print('1. CSV\n2. Quantity Sold\n3. Sales\n4. Profit\n5. Inventory\n6. Exit')
            while True:
                choice = input('Select option: ')
                if choice == '1':
                    print(new_df.to_string())
                elif choice == '2':
                    reference = dict(zip(products, quantity_sold))
                    print(reference)
                elif choice == '3':
                    pass
                elif choice == '4':
                    pass
                elif choice == '5':
                    pass
                elif choice == '6':
                    print('Program closed')
                    break
                else:
                    print('Invalid choice')
        else:
            print('One or more columns are missing')
    else:
        print('File not CSV')
else:
    print('Path does not exist')
