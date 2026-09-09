from pathlib import Path

folder = Path("D:\\Python\\Python-Sample\\FileUpload\\uploads1")

folder.mkdir(
    parents=True,
    exist_ok=True
)

file_path = folder / "test.txt"

with open(file_path, "w") as file:
    file.write("Hello Python")