from pathlib import Path

path = Path("python_exercise/exercise10/learning_python.txt")

# Read the entire file.
print("--- Reading the entire file ---")
contents = path.read_text()
print(contents)

# Read the file line by line.
print("--- Reading the file line by line ---")
lines = contents.splitlines()

for line in lines:
    print(line)