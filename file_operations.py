def write_file():
    filename = input("Enter file name:")
    content = input("Enter content: ")

    file = open(filename,"w")
    file.write(content)
    file.close()

    print("File written successfully!")

def read_file():
    filename = input("Enter file name: ")

    try:
        file = open(filename, "r")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("File not found!")

if __name__ == "__main__":
    print("File Operations Modules")
    