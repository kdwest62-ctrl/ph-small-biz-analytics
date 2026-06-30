from pathlib import Path
import pandas as pd

path = Path(input("CSV path: "))
if path.exists():
    if path.suffix == ".csv":
        df = pd.read_csv(path)
        if df.empty:
            print("CSV is empty")
        else:
            print("CSV is not empty")
    else:
        print("File not csv")
else:
    print("Path does not exist")
