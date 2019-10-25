from collections import Counter, namedtuple, ChainMap
import json
from collections import OrderedDict
from collections import defaultdict
import heapq
from itertools import groupby
from operator import itemgetter

import os
import sys

# portfolie = [
#     {'name': 'IBM', 'share': 100, 'price': 91},
#     {'name': 'apple', 'share': 34, 'price': 45},
#     {'name': 'acme', 'share': 45, 'price': 23}
# ]

# print(portfolie[1]['price'])
#
# cheap = heapq.nsmallest(2, portfolie, key=lambda s:s['price'])
# expensive = heapq.nlargest(2, portfolie, key=lambda s:s['price'])

# print(cheap)
# print(expensive)

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

# head = list(nums)

# heapq.heapify(head)
# print(heapq.heappop(head))

# head = sorted(nums)
# print(head)
# print(len(head))
# print(head[1])


# d = defaultdict(list)
# d['a'].append(1)
# d['a'].append(2)
# d['c'].append(3)
# print(d)

# d = defaultdict(set)
# d['a'].add(1)
# d['a'].add(2)
# d['c'].add(3)
# print(d)

# d = {}
# d.setdefault('a', []).append(1)
# d.setdefault('a', []).append(3)
# d.setdefault('b', []).append(3)

# XXXXXXXX
# d = defaultdict(list)
# for key, value in range(10):
#     d[key].append(value)
# print(d)


# d = OrderedDict()
# d['foo'] = 1
# d['bar'] = 4
# d['spam'] = 3
#
# print(d)
#
# for key in d:
#     print(key, d[key])
#
#
# print(json.dumps(d))

# price = {
#     'acme': 34,
#     'apple': 23,
#     'FB': 56,
#     'dd': 0.2
# }
#
# min_price = min(zip(price.values(), price.keys()))
# print(min_price)
#
# max_price = max(zip(price.values(), price.keys()))
# print(max_price)
#
# sort_price = sorted(zip(price.values(), price.keys()))
# print(sort_price)
#
# sort_price = sorted(zip(price.keys(), price.values()))
# print(sort_price)
#
#
# print(min(price, key=lambda k: price[k]))
# print(max(price, key=lambda k: price[k]))
# print(max(price, key=lambda k: price[k]),
#       price[max(price, key=lambda k: price[k])])


a = {
    'x': 1,
    'y': 2,
    'z': 3
}
b = {
    'w': 10,
    'x': 11,
    'y': 2
}

# print(a.keys() & b.keys())
# print(a.keys() - b.keys())
# print(b.keys() - a.keys())
# print(a.items() & b.items())

# print(a.keys() - {'z', 'w'})
#
# c = {key:a[key] for key in a.keys() - {'z', 'w'}}
# print(c)


# def dedupe(items):
#     seen = set()
#     for item in items:
#         if item not in seen:
#             yield item
#             seen.add(item)

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


# a = [1, 5, 2, 1, 9, 1, 5, 10]

# print(a)
# print(list(dedupe(a)))
# print(a)

# b = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
#
# print(list(dedupe(b, key=lambda d: (d['x'], d['y']))))
#
# print(list(dedupe(b, key=lambda d: (d['x']))))

# record = '           100        513.25            '
#
# print(record[20:30], "   ",  record[31:37])
#
# print(int(record[20:30]), "   ",  record[31:37])

# cost = int(record[20:30] * int(record[31:37]))

# print(cost)

# items = [0, 1, 2, 3, 4, 5, 6]
#
# a = slice(2, 4)
# print(items[a])
#
# b = slice(1, 6, 2)
# print(b.start)
# print(b.stop)
# print(b.step)
#
# print(items[b])
#
# s =  'HelloWorld'
#
# b.indices(len(s))
# print(b)
#
# for i in range(*b.indices(len(s))):
#     print(s[i])

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']


# word_count = Counter(words)
# print(word_count['not'])
#
# top_word = word_count.most_common(3)
# print(top_word)
#
# word_count.update(morewords)
# a = Counter(words)
# b = Counter(morewords)
# print(a)
# print(b)
# print(a - b)

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

# from operator import itemgetter
#
# rows_by_fname = sorted(rows, key=itemgetter('fname'))
# rows_by_uid = sorted(rows, key=itemgetter('uid'))
# rows_by_item = sorted(rows, key=itemgetter('fname', 'uid'))
#
# print(rows_by_fname)
# print(rows_by_uid)
# print(rows_by_item)


# class Uset:
#     def __init__(self, user_id):
#         self.user_id = user_id
#
#     def __repr__(self):
#         return 'User({})'.format(self.user_id)
#
# def sort_nocompare():
#     users = [Uset(23), Uset(3), Uset(99)]
#     print(users)
#     print(sorted(users, key=lambda u: u.user_id))
#
# sort_nocompare()
#

# from operator import attrgetter
# users = [Uset(23), Uset(3), Uset(99)]
# print(sorted(users, key=attrgetter('user_id')))


rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# from operator import itemgetter
# from itertools import groupby

# groupby() 必须先进行关键字排序，再进行groupby筛选

# rows.sort(key=itemgetter('date'))
# for date, items in groupby(rows, key=itemgetter('date')):
#     print(date)
#     for i in items:
#         print('    ', i)
#
#
# mylist = [1, 4, -5, 10, -7, 2, 3, -1]
#
# pos = (n for n in mylist if n > 0)
# print(list(pos))

# values = ['1', '2', '-3', '-', '4', 'N/A', '5']
#
# def is_int(val):
#     try:
#         x = int(val)
#         return True
#     except ValueError:
#         return False
#
# ivals = list(filter(is_int, values))
#
# print(ivals)

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
#
# p1 =      {key: value  for key, value in prices.items() if value > 200}
# print(p1)
# # 上述字典推到比下面的dict快整整一倍
# p1 = dict((key, value) for key, value in prices.items() if value > 200)
# print(p1)
#
# p2 = {key: value for key, value in prices.items() if key in tech_names}

# subscriber = namedtuple('Subsctiber', ['addr', 'joined'])
# sub = subscriber('jonesy@example.com', '2010-10-10')
# print(sub)
#
# print(sub.addr)
# print(sub.joined)
#
# def conoute_cost(records):
#     total = 0.0
#     for rec in records:
#         total += rec[1] * rec[2]
#     return total
#


# 使用命名元组代码清晰
Stock = namedtuple('Stack', ['name', 'shares', 'price'])
# def compute1_cost(records):
#     total = 0.0
#     for rec in records:
#         s = Stock(*rec)
#         total += s.shares * s.price
#     return total

# # TypeError: __new__() takes 4 positional arguments but 7 were given
# stock_prototype = Stock('', 0, 0.0, None, None, None)
#
# def dict_to_stock(s):
#     return stock_prototype._replace(**s)
#
#
# a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
#
# dict_to_stock(a)
#
# print(a)


# nums = [1,2,3,4,5]
# s =sum(x*x for x in nums)
# print(s)

# files = os.listdir('../test')
#
# if any(name.endswith('.py') for name in files):
#     print('There be python')
# else:
#     print('Sorry be python')
#
# s = ('ACME', 50, 123.45)
#
# print(",".join(str(x) for x in s))

# portfolio = [
#     {'name': 'GOOG', 'shares': 50},
#     {'name': 'YHOO', 'shares': 75},
#     {'name': 'AOL', 'shares': 20},
#     {'name': 'SCOX', 'shares': 65}
# ]
#
# min_shares = sorted(s['shares'] for s in portfolio)
# print(min_shares)


a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

c = ChainMap(a, b)
print(c)
print(c['x'])
a['x'] = 23
print(c['x'])


values = ChainMap()
values['x'] = values.new_child()

print(values['x'])
values['x'] = values.parents
print(values['x'])
# print(c['y'])
# print(c['z'])
# print(len(c), list(c), list(c.values()))



merged = dict(b)
merged.update(a)

# print(merged['x'])
# print(merged['y'])
# print(merged['z'])


