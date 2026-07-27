from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
            print('1. Average Usage Comparison\n2. Actual vs Predicted Usage\n3. Forecast Needs\n4. Exit')
            print('-' * 8)
            while True:
                option = input('Select option: ')
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
                    print('')
                    print(result.to_string())
                    print('-' * 8)
                elif option == '2':
                    ingredient = input('Ingredient: ')
                    data = np.array(new_df[ingredient].to_list())
                    unique_data = np.unique(data)
                    probability = []
                    for num in unique_data:
                        num_count = np.count_nonzero(data == num)
                        num_prob = num_count / len(data)
                        probability.append(num_prob)
                    predicted_data = np.random.choice(unique_data, size=len(data), p=probability)
                    x = [n for n in range(1, len(data) + 1)]
                    y1 = [i for i in data]
                    y2 = [i for i in predicted_data]
                    fig, ax = plt.subplots()
                    ax.plot(x, y1, label='Actual', color='darkblue', linestyle='-')
                    ax.plot(x, y2, label='Predicted', color='red', linestyle='--')
                    ax.set_xlabel('Days')
                    ax.set_ylabel('Ingredient Usage')
                    ax.legend()
                    plt.show()
                    print('-' * 8)
                elif option == '3':
                    def moving_average(d, window_size):
                        weights = np.ones(window_size) / window_size
                        return np.convolve(d, weights, mode='valid')
                    ingredient = input('Ingredient: ')
                    data = np.array(new_df[ingredient].tolist())
                    print(f'Daily usage: {data}')
                    try:
                        size = int(input('Window size (days): '))
                    except ValueError:
                        print('Error! Input a number')
                    else:
                        print(f'Moving average: {moving_average(data, size)}')
                        print('-' * 8)
                elif option == '4':
                    print('Program closed')
                    break
    else:
        print('File not csv')
else:
    print('Path does not exist')
