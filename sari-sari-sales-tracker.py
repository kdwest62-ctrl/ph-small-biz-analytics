from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = Path(input('CSV path: '))
if path.exists():
    if path.suffix == '.csv':
        check_csv = pd.read_csv(path, nrows=0)
        required_columns = ['date', 'product', 'quantity_sold', 'price']
        all_exist = set(required_columns).issubset(check_csv.columns)
        if all_exist:
            def func_name(d, c):
                if c == 'full':
                    return d
                elif c == 'filter':
                    print(d.to_string())
                    start_index = int(input('Start date (number): '))
                    end_index = int(input('End date (number): '))
                    end_index += 1
                    result = df.iloc[start_index:end_index].copy()
                    return result
                else:
                    raise ValueError('Program must use either full of filtered CSV')
            def create_df(col_name, col_data):
                data = {'product': [i for i in products], col_name: [i for i in col_data]}
                return pd.DataFrame(data)
            def bar_char(c, v, col_name, plot_title):
                categories = [i for i in c]
                values = [i for i in v]
                plt.bar(categories, values, color='skyblue')
                plt.xlabel('Product')
                plt.ylabel(col_name)
                plt.title(plot_title)
                plt.show()
            df = pd.read_csv(path)
            csv_choice = input('Use full CSV or filter dates (full/filter): ')
            new_df = func_name(df, csv_choice)
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
            print('1. CSV Analysis | 2. Product Rankings | 3. Exit Program')
            while True:
                option = input('Select option: ')
                if option == '1':
                    pass
                elif option == '2':
                    print('1. Quantity Sold | 2. Sales | 3. Profit | 4. Inventory')
                    while True:
                        rankings = input('Select rankings ("e" to exit): ')
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
                            print(create_df('stocks', stocks))
                        elif rankings == 'e':
                            break
                        else:
                            input('Invalid input')
                elif option == '3':
                    print('Program closed')
                    break
                else:
                    print('Invalid input')
        else:
            print('One or more columns are missing')
    else:
        print('File not CSV')
else:
    print('Path does not exist')
