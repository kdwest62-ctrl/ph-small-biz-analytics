from pathlib import Path

path = Path(input("CSV path: "))
if path.exists():
    if path.suffix == ".csv":
        print("Success")
else:
    print("Path does not exist")
