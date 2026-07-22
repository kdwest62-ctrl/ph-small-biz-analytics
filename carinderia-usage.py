from pathlib import Path
import pandas as pd
import numpy as np

path = Path(input('CSV path: '))
if path.exists():
    if path.suffix == '.csv':
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
                    return csv.iloc[start_index:end_index].copy()
                else:
                    raise ValueError('Program must use either full or filtered CSV')
            def create_rankings(sample):
                return dict(sorted(sample.items(), key=lambda item: item[1], reverse=True))
            print(df.to_string())
            choice = input('Use (a) full CSV or (b) select range of dates: ')
            new_df = get_dates(df, choice)
            print('-' * 8)
            print('1. Average Usage\n2. Actual + Predicted Usage\n3. Forecast Needs\n4. Exit')
            while True:
                option = input('Option: ')
                if option == '1':
                    total = int(input('Number of ingredients to compare: '))
                    averages = []
                    ingredients = []
                    count = 1
                    while count <= total:
                        ingredient = input(f'Ingredient {count}: ')
                        check = pd.read_csv(path, nrows=0)
                        if ingredient in check.columns:
                            ingredients.append(ingredient)
                            col_data = np.array(new_df[ingredient].tolist())
                            average = np.mean(col_data)
                            averages.append(round(average, 2))
                            count += 1
                        else:
                            print('Ingredient does not exist')
                    avg_usage = dict(zip(ingredients, averages))
                    usage_ranked = create_rankings(avg_usage)
                    data = {'ingredient': [i for i in usage_ranked.keys()],
                            'average usage': [i for i in usage_ranked.values()]}
                    result = pd.DataFrame(data)
                    print(result.to_string())
                elif option == '2':
                    pass
                elif option == '3':
                    pass
                elif option == '4':
                    print('Program closed')
                    break
    else:
        print('File not csv')
else:
    print('Path does not exist')
