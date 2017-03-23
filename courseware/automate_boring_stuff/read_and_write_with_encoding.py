def get_encoding(file_path):
    import chardet
    with open(file_path, 'rb') as file:
        first_line = file.readline()

    encoding = chardet.detect(first_line).get('encoding')

    print('encoding by chardet:{}'.format(encoding))

    if 'utf' in encoding.lower():
        return 'utf-8'
    elif 'ascii' in encoding.lower():
        return 'gbk'
    else:
        return None


def transfer_format(src_file_path, dst_file_path, dst_encoding='utf-8'):
    import codecs
    src_encoding = get_encoding(src_file_path)
    with codecs.open(src_file_path, 'r', src_encoding) as file:
        content = file.read()
    with codecs.open(dst_file_path, 'w', dst_encoding) as file:
        byte_form = codecs.encode(content, dst_encoding, 'ignore') # Get the byte form, **PLEASE PAY ATTENTION TO IGNORE**
        dst_content = codecs.decode(byte_form, dst_encoding) # Save byte as dst form
        file.write(dst_content)
    
    print('{}-{} > {}-{}'.format(src_encoding, src_file_path, dst_encoding, dst_file_path))

if __name__ == '__main__':
    src_file_path = 'read_file_ansi.txt'
    encoding = get_encoding(src_file_path)
    print(encoding)
    
    dst_file_path = 'write_file_test_code.txt'
    transfer_format(src_file_path, dst_file_path, 'gbk')