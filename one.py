#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a *.py module '
__author__ = 'ChenFaxiang'

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

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print 'Hello, world!'
    elif len(args) == 2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'

if __name__ == '__main__':
    test()


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

newStu = Student('chen', 100)
print 'this is the Student Class name: %s' % newStu.name
print 'this is the Student Class score: %s' % newStu.score


class Fib(object):
    def __init__(self):
        # 初始化两个计数器a，b
        self.a, self.b = 0, 1

    def __iter__(self):
        # 实例本身就是迭代对象，故返回自己
        return self

    def next(self):
        # 计算下一个值
        self.a, self.b = self.b, self.a + self.b

        # 退出循环的条件
        if self.a > 100000:
            raise StopIteration()
        # 返回下一个值
        return self.a

for n in Fib():
    print n


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

fact(1)
