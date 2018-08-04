#!/usr/bin/env python

whitelist = {'s'}

def f():
    def callback():
        whitelist.add('new entry')
        whitelist = {'replace contents'}
        if 's' in whitelist:
            print('yes')
        else:
            print('no')


    from main import main

    main(callback)


f()


def g():
    print(h_variable)

def h():
    h_variable = 99
    g()

h()
