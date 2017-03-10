import PyPDF2

def copy_pdf(read_pdf_path, save_pdf_path, nums = []):
    with open(read_pdf_path, 'rb') as read_obj, open(save_pdf_path, 'wb') as write_obj:
        pdf_reader = PyPDF2.PdfFileReader(read_obj)
        pdf_writer = PyPDF2.PdfFileWriter()

        for n in nums:
            page = pdf_reader.getPage(n)
            pdf_writer.addPage(page)
        
        # pdf_writer.encrypt('miaodx') # when encrypt, I failed to save to file.
        pdf_writer.write(write_obj)
        print('Done')

if __name__ == '__main__':
    # nums = list(range(0,11,2))
    nums = [0]
    read_pdf_path = 'H:\class_material\python101\other_material\python_101.pdf'
    write_pdf_path = 'pdf_copy_test.pdf'
    copy_pdf(read_pdf_path, write_pdf_path, nums)