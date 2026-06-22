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
            def create_df(col_name, col_data):
                data = {'product': [i for i in products], col_name: [i for i in col_data]}
                return pd.DataFrame(data)

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
            print('1. Quantity Sold\n2. Sales\n3. Profit\n4. Inventory\n5. Exit')
            while True:
                rankings = input('Select rankings: ')
                if rankings == '1':
                    print(create_df('quantity_sold', ref1.values()))
                elif rankings == '2':
                    print(create_df('sales', ref3.values()))
                elif rankings == '3':
                    exp = []
                    print('Input total expenses for each product')
                    for p in products:
                        expense = int(input(f'{p}: '))
                        exp.append(expense)
                    expenses = np.array(exp)
                    profits = np.subtract(sales, expenses)
                    print(create_df('profit', profits))
                elif rankings == '4':
                    orders = []
                    for p in products:
                        order = int(input(f'{p} sold {ref1[p]} | items ordered: '))
                        if order >= ref1[p]:
                            orders.append(order)
                        else:
                            print('Items ordered cannot be less than quantity sold')
                            print(f'Items ordered for {p}: 0')
                            orders.append(0)
                    orders = np.array(orders)
                    quantity_sold = np.array(quantity_sold)
                    stocks = np.subtract(orders, quantity_sold)
                elif rankings == '5':
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
