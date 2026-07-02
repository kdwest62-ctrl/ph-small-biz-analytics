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
                    start_index = int(input('Start date (number): '))
                    end_index = int(input('End date (number): '))
                    end_index += 1
                    result = csv.iloc[start_index:end_index].copy()
                    return result
                else:
                    raise ValueError('Program must use either full or filtered CSV')
            print(df.to_string())
            choice = input('Use (a) full CSV or (b) select range of dates: ')
            new_df = get_dates(df, choice)
            print(new_df.to_string())
    else:
        print("File not csv")
else:
    print("Path does not exist")
