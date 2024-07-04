def read_byte_file(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()
        print(content)

if __name__ =="__main__":
    file_path = input("Enter file path or name:\t")
    read_byte_file(file_path)
