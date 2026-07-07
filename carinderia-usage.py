from pathlib import Path
import pandas as pd
import numpy as np

path = Path(input("CSV path: "))
if path.exists():
    if path.suffix == ".csv":
        df = pd.read_csv(path)
        if df.empty:
            print("CSV is empty")
        else:
            def get_dates(csv, user_choice):
                if user_choice == 'a':
                    return csv
                elif user_choice == 'b':
                    start_index = int(input('Start date (index): '))
                    end_index = int(input('End date (index): '))
                    end_index += 1
                    result = csv.iloc[start_index:end_index].copy()
                    return result
                else:
                    raise ValueError('Program must use either full or filtered CSV')
            print(df.to_string())
            choice = input('Use (a) full CSV or (b) select range of dates: ')
            new_df = get_dates(df, choice)
            print('-' * 8)
            print('1. Average Usage\n2. Actual + Predicted Usage\n3. Forecast Needs\n4. Exit')
            while True:
                option = input('Option: ')
                if option == '1':
                    total = int(input('Number of columns to compare: '))
                    averages = []
                    columns = []
                    count = 1
                    while count <= total:
                        col_name = input(f'Column {count}: ')
                        check = pd.read_csv(path, nrows=0)
                        if col_name in check.columns:
                            columns.append(col_name)
                            col_data = np.array(new_df[col_name].tolist())
                            col_avg = np.mean(col_data)
                            averages.append(col_avg)
                            count += 1
                        else:
                            print('Column does not exist')
                    reference = dict(zip(columns, averages))
                    print(reference)
                elif option == '2':
                    pass
                elif option == '3':
                    pass
                elif option == '4':
                    print('Program closed')
                    break
    else:
        print("File not csv")
else:
    print("Path does not exist")
