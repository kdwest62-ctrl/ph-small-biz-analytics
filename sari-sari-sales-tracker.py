from pathlib import Path

path = Path(input('CSV path: '))
if path.exists():
    if path.suffix == '.csv':
        pass
    else:
        print('File not CSV')
else:
    print('Path does not exist')
