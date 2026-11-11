from pathlib import Path

path = Path("python_exercise/exercise10/learning_python.txt")
contents = path.read_text()

for line in contents.splitlines():
    modified_line = line.replace("Python", "C")
    print(modified_line)