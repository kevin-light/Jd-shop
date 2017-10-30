 #!/usr/bin/env python
# -*- coding:utf-8 -*-


# class Foo:
#     def __str__(self):
#         return '<input type="text" />'
#
# f = Foo()
# print(f)

# 2222222、
d = {'name':'alvin','age':18,'k1':123,'k2':456}
t = "inset into tb(%s) values(%s)"

key_list = []
value_list = []

for k,v in d.items():
    key_list.append(k)
    value_list.append("%%(%s)s" %k)

print(key_list)
print(value_list)

sql = t %(','.join(key_list),','.join(value_list))
print(sql)