from pathlib import Path

path = Path(input('CSV path: '))
if path.exists():
    pass
else:
    print('Path does not exist')
