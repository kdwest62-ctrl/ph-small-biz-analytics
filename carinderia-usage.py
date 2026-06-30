from pathlib import Path

path = Path(input("CSV path: "))
if path.exists():
    print('Path exists')
else:
    print("Path does not exist")
