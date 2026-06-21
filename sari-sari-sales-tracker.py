from pathlib import Path
import pandas as pd

path = Path(input('CSV path: '))
if path.exists():
    if path.suffix == '.csv':
        check_csv = pd.read_csv(path, nrows=0)
        required_columns = ['date', 'product', 'quantity_sold', 'price']
        all_exist = set(required_columns).issubset(check_csv.columns)
        if all_exist:
            df = pd.read_csv(path)
            dates = df['date'].tolist()
            dates_dict = dict(enumerate(dates))
            print(dates_dict)
            start_index = int(input('Start date (number): '))
            end_index = int(input('End date (number): '))
            end_index += 1
            new_df = df.iloc[start_index:end_index].copy()
            print('Menu')
            print('1. CSV\n2. Quantity Sold\n3. Sales\n4. Profit\n5. Inventory\n6. Exit')
            while True:
                choice = input('Select option: ')
                if choice == '1':
                    print(new_df.to_string())
                elif choice == '2':
                    pass
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
