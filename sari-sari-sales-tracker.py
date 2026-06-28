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
                    start_index = int(input('Start date (number): '))
                    end_index = int(input('End date (number): '))
                    end_index += 1
                    result = csv.iloc[start_index:end_index].copy()
                    return result
                else:
                    raise ValueError('Program must use either full or filtered CSV')
            def create_df(product_data, col_name, col_data):
                data = {'product': [i for i in product_data], col_name: [i for i in col_data]}
                return pd.DataFrame(data)
            def bar_chart(categories, values, col_name):
                plt.bar(categories, values, color='skyblue')
                plt.xlabel('Product')
                plt.ylabel(col_name)
                plt.show()
            def create_rankings(sample):
                return dict(sorted(sample.items(), key=lambda item: item[1], reverse=True))
            df = pd.read_csv(path)
            print(df.to_string())
            choice = input('Use (a) full CSV or (b) select range of dates: ')
            new_df = get_dates(df, choice)
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
            quantity_sold = np.array(quantity_sold)
            prices = np.array(prices)
            sales = np.multiply(quantity_sold, prices)
            product_sold = dict(zip(products, quantity_sold))
            product_prices = dict(zip(products, prices))
            product_sales = dict(zip(products, sales))
            while True:
                print('-' * 8)
                print('1. Product Groups | 2. Product Rankings | 3. Exit Program')
                option = input('Option: ')
                if option == '1':
                    print('a. Date | b. Quantity Sold | c. Price')
                    while True:
                        option = input('Group (e to Exit): ')
                        if option == 'a':
                            print(new_df.groupby('product')['date'].sum())
                        elif option == 'b':
                            print(new_df.groupby('product')['quantity_sold'].sum())
                        elif option == 'c':
                            print(new_df.groupby('product')['price'].sum())
                        elif option == 'e':
                            break
                        else:
                            print('Invalid input')
                elif option == '2':
                    while True:
                        print('-' * 8)
                        print('1. Quantity Sold\n2. Sales\n3. Profit\n4. Inventory')
                        rankings = input('Rankings (e to exit): ')
                        if rankings == '1':
                            while True:
                                print('a. Table | b. Bar Chart')
                                option = input('Presentation (e to exit): ')
                                if option == 'a':
                                    sorted_data = create_rankings(product_sold)
                                    print('-' * 8)
                                    print(create_df(sorted_data.keys(), 'quantity_sold', sorted_data.values()))
                                    print('-' * 8)
                                elif option == 'b':
                                    sorted_data = create_rankings(product_sold)
                                    bar_chart(sorted_data.keys(), sorted_data.values(), 'Quantity Sold')
                                elif option == 'e':
                                    break
                                else:
                                    print('Invalid input')
                        elif rankings == '2':
                            while True:
                                print('a. Table | b. Bar Chart')
                                option = input('Presentation (e to exit): ')
                                if option == 'a':
                                    sorted_data = create_rankings(product_sales)
                                    print('-' * 8)
                                    print(create_df(sorted_data.keys(), 'sales', sorted_data.values()))
                                    print('-' * 8)
                                elif option == 'b':
                                    sorted_data = create_rankings(product_sales)
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
                            product_profits = dict(zip(products, profits))
                            while True:
                                print('a. Table | b. Bar Chart')
                                option = input('Presentation (e to exit): ')
                                if option == 'a':
                                    sorted_data = create_rankings(product_profits)
                                    print('-' * 8)
                                    print(create_df(sorted_data.keys(), 'profit', sorted_data.values()))
                                    print('-' * 8)
                                elif option == 'b':
                                    sorted_data = create_rankings(product_profits)
                                    bar_chart(sorted_data.keys(), sorted_data.values(), 'Profit')
                                elif option == 'e':
                                    break
                                else:
                                    print('Invalid input')
                        elif rankings == '4':
                            orders = []
                            for p in products:
                                order = int(input(f'{p} sold {product_sold[p]} | items ordered: '))
                                if order >= product_sold[p]:
                                    orders.append(order)
                                else:
                                    raise ValueError('Items ordered cannot be less than quantity sold')
                            orders = np.array(orders)
                            quantity_sold = np.array(quantity_sold)
                            stocks = np.subtract(orders, quantity_sold)
                            product_stocks = dict(zip(products, stocks))
                            while True:
                                print('a. Table | b. Bar Chart')
                                option = input('Presentation (e to exit): ')
                                if option == 'a':
                                    sorted_data = create_rankings(product_stocks)
                                    print('-' * 8)
                                    print(create_df(sorted_data.keys(), 'stocks', sorted_data.values()))
                                    print('-' * 8)
                                elif option == 'b':
                                    sorted_data = create_rankings(product_stocks)
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
