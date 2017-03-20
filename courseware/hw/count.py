from pprint import pprint

s = """
- "Times end, River, because they have to.
Because there's no such thing as happy ever after.
It's just a lie we tell ourselves because the truth is so hard."
- "No, Doctor, happy ever after doesn't mean forever,
It just mean time."
"""

# print(s)

# 1.COUNT CHAR

c_d = dict();

for c in s:
    c_d.setdefault(c, 0)
    c_d[c] += 1


pprint(c_d)

# Check
to_check = ['n', 'N']
for t_c in to_check:
    print('number of {}, by dict: {}, by count: {}'.format(t_c, c_d.get(t_c), s.count(t_c)))




# COUNT WORD

s_li = s.split(' ')

w_d = dict()

for w in s_li:
    w_d.setdefault(w, 0)
    w_d[w] += 1

pprint(w_d)


# COUNT WORD and replace '\n'

s_no_n = s.replace('\n', ' ');

s_li = s.split(' ')

w_d = dict()

for w in s_li:
    w_d.setdefault(w, 0)
    w_d[w] += 1

pprint(w_d)