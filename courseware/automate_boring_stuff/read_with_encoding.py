# vi read_with_encoding.py

if __name__ == '__main__':
    file = open('read_file.txt', 'r')
    text = file.read()
    file.close()
    print(text)