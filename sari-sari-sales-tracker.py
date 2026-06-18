import pandas as pd
from pathlib import Path
import numpy as np

try:
    path = Path(input('CSV path: '))
    if path.exists():
        check = pd.read_csv(path, nrows=0)
        required_columns = ['date', 'product', 'quantity_sold', 'price']
        all_exist = set(required_columns).issubset(check.columns)
        if all_exist:
            df = pd.read_csv(path)
            column_data = df['product'].tolist()
            products = []
            for entry in column_data:
                if entry not in products:
                    products.append(entry)
            quantity_sold = []
            prices = []
            for product in products:
                if column_data.count(product) > 1:
                    prod = df[df['product'] == product]
                    sales = prod['quantity_sold'].tolist()
                    price = prod['price'].tolist()
                    quantity_sold.append(sum(sales))
                    prices.append(price[0])
                elif column_data.count(product) == 1:
                    sales = df[df['product'] == product]['quantity_sold'].values[0]
                    price = df[df['product'] == product]['price'].values[0]
                    quantity_sold.append(sales)
                    prices.append(price)
            arr1 = np.array(quantity_sold)
            arr2 = np.array(prices)
            sales = np.multiply(arr1, arr2)
            ref1 = dict(zip(products, quantity_sold))
            ref2 = dict(zip(products, prices))
            ref3 = dict(zip(products, sales))
            print('Menu')
            print('1. Data\n2. Quantity Sold\n3. Sales\n4. Profit\n5. Inventory\n6. Exit')
            while True:
                option = input('Select option: ')
                if option == '1':
                    print(df.to_string())
                    print('-' * 8)
                elif option == '2':
                    sorted_data = dict(sorted(ref1.items(), key=lambda item: item[1], reverse=True))
                    data = {'product': [i for i in sorted_data.keys()],
                            'quantity_sold': [i for i in sorted_data.values()]}
                    result = pd.DataFrame(data)
                    print(result.to_string())
                    print('-' * 8)
                elif option == '3':
                    data = {'product': [i for i in products],
                            'quantity_sold': [i for i in quantity_sold],
                            'price': [i for i in prices],
                            'sales': [i for i in sales]}
                    result = pd.DataFrame(data)
                    res = result.groupby(['product', 'quantity_sold', 'price'])['sales'].sum().sort_values(ascending=False)
                    print(res.to_string())
                    print('-' * 8)
                elif option == '4':
                    exp = []
                    for p in products:
                        expense = int(input(f'Total expenses for {p}: '))
                        exp.append(expense)
                    expenses = np.array(exp)
                    profits = np.subtract(sales, expenses)
                    data = {'product': [i for i in products],
                            'quantity_sold': [i for i in quantity_sold],
                            'price': [i for i in prices],
                            'sales': [i for i in sales],
                            'expenses': [i for i in expenses],
                            'profit': [i for i in profits]}
                    profit = pd.DataFrame(data)
                    res = profit.groupby(['product', 'quantity_sold', 'price', 'sales', 'expenses'])['profit'].sum().sort_values(ascending=False)
                    print(res.to_string())
                    print('-' * 8)
                elif option == '5':
                    reference = dict(zip(products, quantity_sold))
                    orders = []
                    for p in products:
                        order = int(input(f'{p} sold {reference[p]} | items ordered: '))
                        if order >= reference[p]:
                            orders.append(order)
                        else:
                            print('Items ordered cannot be less than quantity sold')
                            print(f'Items ordered for {p}: 0')
                            orders.append(0)
                    orders = np.array(orders)
                    quantity_sold = np.array(quantity_sold)
                    stocks = np.subtract(orders, quantity_sold)
                    data = {'product': [i for i in products],
                            'orders': [i for i in orders],
                            'quantity_sold': [i for i in quantity_sold],
                            'stocks': [i for i in stocks]}
                    inventory = pd.DataFrame(data)
                    res = inventory.groupby('product')['stocks'].sum().sort_values(ascending=False)
                    print(res.to_string())
                    print('-' * 8)
                elif option == '6':
                    print('Program closed')
                    break
                else:
                    print('Option not available')
        else:
            print('One or more columns are missing')
    else:
        print('Path does not exist')
except ValueError:
    print('Invalid input')
