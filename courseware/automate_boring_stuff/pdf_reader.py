import PyPDF2

def get_pdf_num_text(pdf_path, page_num):
    """
    Chances are that it will not succeed to extractText.
    """
    pdfFileObj = open(pdf_path, 'rb')
    pdf = PyPDF2.PdfFileReader(pdfFileObj)
    print('{} have {} pages'.format(pdf_path, pdf.getNumPages()))
    if pdf.isEncrypted:
        print('it seems that this pdf is encrypted, so we can not extract text from it')
        return None
    page = pdf.getPage(page_num)
    return page.extractText()


if __name__=='__main__':
    # pdf_path = 'template.pdf'
    pdf_path = 'H:\\class_material\\计算机视觉\\ImageSearchEngineResourceGuide.pdf'
    # pdf_path = 'H:\\class_material\\计算机视觉\\Computer Vision A Modern Approach 2nd Edition.pdf'
    print(get_pdf_num_text(pdf_path, 1))