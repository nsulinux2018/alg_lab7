#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


def main():
    print(Person('Ivan', 'Sidorov') == Person('Ivan', 'Sidorov'))
    # telephone_book = {Person('Ivan', 'Petrov'): '+123456'}
    # p2 = Person('Ivan', 'Sidorov')
    # telephone_book[p2] = '+456789'
    # print(telephone_book[Person('Ivan', 'Petrov')])
    # print(telephone_book[p2])
    # p2.first_name = 'Fedor'
    # print(telephone_book[Person('Ivan', 'Sidorov')])
    # print(telephone_book[Person('Fedor', 'Sidorov')])


if __name__ == "__main__":
    main()
