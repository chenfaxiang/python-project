#!/usr/bin/env python
# -*- coding: utf-8 -*-

print 'hello word，这就是来测试中文的。'

print 'hello,%s' % '格式化字符串'

print '哈哈,%s,you just have $%d.' % ('zhangsan', 100)

print 'what? 今年的收入只有去年的 %d%%?' % 10

allClassmateName = ['a', 'b', 'c']
print allClassmateName
print '一共有同学：%d名' % len(allClassmateName)

tup = (1,)
print 'tuple数据类型在定义一个数据时必须加一个逗号，否则就会被当做括号1处理 %s' % tup

def power(x, n):
    s = 1
    while n > 0:
        n = n -1
        s = s * x
    return s
print power(2, 3)

a = [x * x for x in range(1, 11)]
print a

L = ['Hello', 'World', 18, 'Apple', None]
print [s.lower() for s in L if isinstance(s, str)]