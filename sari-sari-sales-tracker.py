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
            pass
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
