import pandas as pd
from pathlib import Path

path = Path(input('CSV path: '))
if path.exists():
    df = pd.read_csv(path)
    print('Menu')
    print('1. Data\n2. Sales\n3. Revenue\n4. Profit\n5. Inventory\n6. Exit')
    while True:
        option = input('Select option: ')
        if option == '1':
            print(df.to_string())
            print('-' * 8)
        elif option == '2':
            column_data = df['product'].tolist()
            products = []
            for entry in column_data:
                if entry not in products:
                    products.append(entry)
            quantity_sold = []
            for product in products:
                if column_data.count(product) > 1:
                    prod = df[df['product'] == product]
                    sales = prod['quantity_sold'].tolist()
                    quantity_sold.append(sum(sales))
                elif column_data.count(product) == 1:
                    sales = df[df['product'] == product]['quantity_sold'].values[0]
                    quantity_sold.append(sales)
            data = {'product': [i for i in products],
                    'sales': [i for i in quantity_sold]}
            result = pd.DataFrame(data)
            res = result.groupby('product')['sales'].sum().sort_values(ascending=False)
            print(res.to_string())
        elif option == '3':
            pass
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
