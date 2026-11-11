from pathlib import Path

filenames = ["python_exercise/exercise10/cats.txt", "python_exercise/exercise10/dogs.txt"]

for filename in filenames:
    path = Path(filename)

    try:
        contents = path.read_text()

    except FileNotFoundError:
        pass

    else:
        print(f"\nReading file: {filename}")
        print(contents)