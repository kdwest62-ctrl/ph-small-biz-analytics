import pandas as pd
from pathlib import Path
import numpy as np

path = Path(input('CSV path: '))
if path.exists():
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
    print('Menu')
    print('1. Data\n2. Quantity Sold\n3. Sales\n4. Profit\n5. Inventory\n6. Exit')
    while True:
        option = input('Select option: ')
        if option == '1':
            print(df.to_string())
            print('-' * 8)
        elif option == '2':
            data = {'product': [i for i in products],
                    'quantity_sold': [i for i in quantity_sold]}
            result = pd.DataFrame(data)
            res = result.groupby('product')['quantity_sold'].sum().sort_values(ascending=False)
            print(res.to_string())
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
            pass
        elif option == '5':
            pass
        elif option == '6':
            print('Program closed')
            break
        else:
            print('Option not available')
else:
    print('Path does not exist')
