#!/usr/bin/env python3

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
