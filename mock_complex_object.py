#!/usr/bin/env python

def real_code():

    thing = RealCompexThing()

    thing.do_something_else()
    thing.xxx.yyy.zzz.do_something()




def test():

    def return_false():
        return False

    mock_complex_thing = Mock()
    mock_complex_thing.xxx.yyy.zzz.do_something = return_false

    with patch.object(module, 'RealCompexThing', lambda: mock_complex_thing):
        real_code()  #
