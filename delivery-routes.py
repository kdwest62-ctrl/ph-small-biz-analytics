from pathlib import Path
import pandas as pd

path = Path(input('CSV path: '))
if path.exists():
    if path.suffix == '.csv':
        df = pd.read_csv(path)
        if df.empty:
            print('CSV is empty')
        else:
            pass
    else:
        print('File not CSV')
else:
    print('Path does not exist')
