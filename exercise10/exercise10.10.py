from pathlib import Path

path = Path("python_exercise/exercise10/sample_text.txt")
contents = path.read_text()

# Count occurrences of 'the'.
word_count = contents.lower().count("the")

# Count occurrences of 'the '.
word_count_with_space = contents.lower().count("the ")

print(f"The word 'the' appears {word_count} times.")
print(f"The word 'the ' appears {word_count_with_space} times.")