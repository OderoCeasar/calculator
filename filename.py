def get_filename():
    filename = input("Please enter the filename: ")
    return filename

try:
    filename = get_filename()
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"File '{filename}' not found. Please check the filename and try again.") 