from pathlib import Path

path = Path("python_exercise/exercise10/learning_python.txt")
contents = path.read_text()

print("--- Reading the file line by line ---")

for line in contents.splitlines():
    print(line)