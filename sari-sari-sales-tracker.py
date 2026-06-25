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
            def get_dates(csv, user_choice):
                if user_choice == 'a':
                    return csv
                elif user_choice == 'b':
                    print(csv.to_string())
                    start_index = int(input('Start date (number): '))
                    end_index = int(input('End date (number): '))
                    end_index += 1
                    result = csv.iloc[start_index:end_index].copy()
                    return result
                else:
                    raise ValueError('Program must use either full or filtered CSV')
            def create_df(col_name, prod_data, col_data):
                data = {'product': [i for i in prod_data], col_name: [i for i in col_data]}
                return pd.DataFrame(data)
            def bar_chart(c, v, col_name):
                categories = [i for i in c]
                values = [i for i in v]
                plt.bar(categories, values, color='skyblue')
                plt.xlabel('Product')
                plt.ylabel(col_name)
                plt.show()
            def sort_dict(sample_dict):
                result_dict = dict(sorted(sample_dict.items(), key=lambda item: item[1], reverse=True))
                return result_dict
            df = pd.read_csv(path)
            csv_choice = input('Use (a) full CSV or (b) select dates of CSV: ')
            new_df = get_dates(df, csv_choice)
            print(new_df)
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
                    print('1. Groupby() | 2. Exit')
                    while True:
                        option = input('Select option: ')
                        if option == '1':
                            group = input("Group products by 'date', 'quantity_sold', or 'price': ")
                            if group in ['date', 'quantity_sold', 'price']:
                                if group == 'date':
                                    output = new_df.groupby('product')[group].sum()
                                    print(output)
                                elif group == 'quantity_sold':
                                    output = new_df.groupby('product')[group].sum()
                                    print(output)
                                elif group == 'price':
                                    output = new_df.groupby('product')[group].sum()
                                    print(output)
                            else:
                                print('Invalid input')
                        elif option == '2':
                            break
                        else:
                            print('Invalid input')
                elif option == '2':
                    print('1. Quantity Sold | 2. Sales | 3. Profit | 4. Inventory')
                    while True:
                        rankings = input('Select rankings ("e" to exit): ')
                        if rankings == '1':
                            print('a. Table | b. Bar Chart')
                            while True:
                                option = input('Select option ("e" to exit): ')
                                if option == 'a':
                                    sorted_data = sort_dict(ref1)
                                    print(create_df('quantity_sold', sorted_data.keys(), sorted_data.values()))
                                elif option == 'b':
                                    sorted_data = sort_dict(ref1)
                                    bar_chart(sorted_data.keys(), sorted_data.values(), 'Quantity Sold')
                                elif option == 'e':
                                    break
                                else:
                                    print('Invalid input')
                        elif rankings == '2':
                            print('a. Table | b. Bar Chart')
                            while True:
                                option = input('Select option ("e" to exit): ')
                                if option == 'a':
                                    sorted_data = sort_dict(ref3)
                                    print(create_df('sales', sorted_data.keys(), sorted_data.values()))
                                elif option == 'b':
                                    sorted_data = sort_dict(ref3)
                                    bar_chart(sorted_data.keys(), sorted_data.values(), 'Sales')
                                elif option == 'e':
                                    break
                                else:
                                    print('Invalid input')
                        elif rankings == '3':
                            exp = []
                            print('Input total expenses for each product')
                            for p in products:
                                expense = int(input(f'{p}: '))
                                exp.append(expense)
                            expenses = np.array(exp)
                            profits = np.subtract(sales, expenses)
                            ref4 = dict(zip(products, profits))
                            print('a. Table | b. Bar Chart')
                            while True:
                                option = input('Select option ("e" to exit): ')
                                if option == 'a':
                                    sorted_data = sort_dict(ref4)
                                    print(create_df('profit', sorted_data.keys(), sorted_data.values()))
                                elif option == 'b':
                                    sorted_data = sort_dict(ref4)
                                    bar_chart(sorted_data.keys(), sorted_data.values(), 'Profit')
                                elif option == 'e':
                                    break
                                else:
                                    print('Invalid input')
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
                            ref5 = dict(zip(products, stocks))
                            print('a. Table | b. Bar Chart')
                            while True:
                                option = input('Select option ("e" to exit): ')
                                if option == 'a':
                                    sorted_data = sort_dict(ref5)
                                    print(create_df('stocks', sorted_data.keys(), sorted_data.values()))
                                elif option == 'b':
                                    sorted_data = sort_dict(ref5)
                                    bar_chart(sorted_data.keys(), sorted_data.values(), 'Stocks')
                                elif option == 'e':
                                    break
                                else:
                                    print('Invalid input')
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
