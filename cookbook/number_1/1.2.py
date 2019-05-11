# -*- encoding=utf-8 -*-

# 从任意长度的可迭代对象中分解元素

# record = ['Dave', 'dave@example.com', '773-555-1212', '847-555-1212']
# name, email, *phone_numbers = record
# print(name)
# print(email)
# print(phone_numbers)

# *trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
# print(trailing)
# print(current)

# records = [
#     ('foo', 1, 2),
#     ('bar', 'hello'),
#     ('foo', 3, 4)
# ]
#
# def do_foo(x, y):
#     print('foo', x, y)
# # do_foo(1, 2)
#
# def do_bar(s):
#     print('bar', s)
# # do_bar('hello')
#
# for tag, *args in records:
#     if tag == 'foo':
#         do_foo(*args)
#     elif tag == 'bar':
#         do_bar(*args)
#     else:
#         print('hello')

# line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
# uname, *fields, homedir, sh = line.split(':')
# print(uname)
# print(homedir)
# print(sh)

# record = ('ACME', 50, 123.45, (12, 18, 2012))
# name, *_, (*_, year) = record
# print(name)
# print(year)

# items = [1, 10, 7, 4, 5, 9]
# head, *tail = items
# print(head)
# print(tail)

