from pathlib import Path
import pandas as pd

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
                    pass
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
