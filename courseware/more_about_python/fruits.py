"""
Run in vscode, Korean is okay.
"""
class Fruit(object):
    def __init__(self, c_name, e_name, k_name): # Korean
        self.c_name = c_name
        self.e_name = e_name
        self.k_name = k_name

    def print_names(self):
        print('{} in English, {} in Chinese, {} in Korean'.format(self.e_name, self.c_name, self.k_name))

f1 = Fruit('苹果', 'Apple', '사과')
f2 = Fruit('橘子', 'Orange', '오렌지')
f3 = Fruit('香蕉', 'Banana', '바나나')

f1.print_names()
f2.print_names()
f3.print_names()