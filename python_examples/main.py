import logging

from integer import convert
from literals import convert as convert_l
from setting import some_var, config
from utils import add, get_time
log = logging.getLogger('mylogger')
log2 = logging.getLogger('yourlogger')

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s -- %(levelname)s %(name)s || %(message)s")

# Critical
# error
# warning
# info
# debug

def seperator_example():
    # _ seperator example
    # num = 1000000000
    # print(num)

    # above is same as below
    sep_num = 1_000_000_000
    print(sep_num)


def fstring_example(name='tom', surname='elliot', age=34):
    # f-string example
    # using format
    # description = "Hello his name is {} {} and his age is {}".format(name, surname, age)
    # print(description)

    # using fstrings
    description = f"Hello his name is {name=} {surname=} and his age is {age=}"
    print(description)


def single_line_assignment():
    value = True
    # value = False

    if value == True:
        final_val = "hello"
    else:
        final_val = "ehlo"

    final_val = 'hello' if value else 'ehlo'
    print(final_val)


def dry_example():
    one = 3455
    two = 3909.234
    three = -0.2343434

    operation = (three * one / two * three + one - three)
    print(operation)


def test_settings():
    print(config)
    print(some_var)


def log_example(var):
    """
    this will log some examples in the file
    """

    log.info('example code started')
    log.debug('calling settings')
    test_settings()
    log2.error('there is no error this is example ')
    log2.info('finished')


def docstring_example(name, age, role='manager'):
    """This is just a docstring example

    Parameters
    ----------
    name : str
        this is name parameter
    age : int
        this is age parameter
    role : str, optional
        this defines the role of the person, by default 'manager'
    """
    print(name, age, role)


def with_example():
    filename = "run.txt"
    fh = open(filename, 'w')
    # fh.close()

    # print(fh.closed)

    with open(filename, 'r+') as fw:
        fw.read()
        print(fw.closed)
    print(fw.closed)


def fixed_return_type_example():
    o = frte()
    print(o)
    print(o in 'random')


def frte():
    class Test:
        ...

    val = 4
    if val == 1:
        return "hello"
    elif val == 2:
        return 34
    elif val == 3:
        return True
    elif val == 4:
        return 34.55
    elif val == 5:
        return Test()
    else:
        return


def dict_get_example():
    sdict = {
        'name': 'test',
        'age': 34
    }

    # print(sdict['address'])

    print(sdict.get('name', 'delhi'))


def enumerate_example():
    # counter = 0
    ex_list = ['hey', 'there', 'whats', 'going', 'on']

    # for i in ex_list:
    #     print(counter)
    #     print(i)
    #     counter += 1

    for count, i in enumerate(ex_list, start=2):
        print(count)
        print(i)


def override_builin_ex():
    print(list('amit'))
    # list = 'amit'
    # print(list)
    # print(list('amit'))


def try_except_example():
    ex_dict = {
        'name': 'test',
        'phone': 'abckdfk'
    }

    try:
        # print(ex_dict['mark'])
        int(ex_dict['abc'])
    except KeyError as e:
        print('key no found', e)
        failed = True
    except ValueError as e:
        print('not suitable value,', e)
        conv_fail = True
    except Exception as e:
        raise


def test_star_import():
    convert_l(34)


def truthy_compare_ex():
    val = {}
    val = []

    if val != []:
        print('data is there')
    else:
        print('data is not there')

    val = {1, 2, 3}
    if val:
        print('present')
    else:
        print('absent')


def unpacking_ex():
    def arg_unpack(a, b, c, d, e):
        print(a, b, c, d, e)

    def kwarg_unpack(name=None, sender=None):
        print(f"sender: {name}  {sender}")

    arg = [3, 4.0, 'amit', 'ch', 'character', {}]
    kwarg = {
        'name': 'tom',
        # 'sender': 'jerry',
        # 'process': 3434
    }
    # arg_unpack(*arg)
    kwarg_unpack(**kwarg)


def pretty_print_ex():
    import pprint

    ex = {'name': 'user', "subjects": {'english': {'marks': 34, 'pass': True}, 'hindi': {'marks': 22, 'pass': False}}}
    # print(ex)

    pprint.pprint(ex, indent=4)


def assign_value_same_time_ex():
    def return_dump():
        return 1, 'name', 'task'

    ex_code, name, task = return_dump()
    print(ex_code, name, task)


def counter_example():
    data = [1, 1, 3, 3, 7, 4, 5, 6, 1, 1, 1, 5, 2, 3, 3, 0, 0, 0, 8]

    from collections import Counter

    c = Counter(data)
    print(c)
    # print(dir)
    print(c.keys())
    # print(c[3])


def first_class_object_ex():
    def callback(val):
        print(val)
        print('callback recived val')

    def process(call_fn):
        final_val = 'done'
        call_fn(final_val)
        return call_fn

    v = process(callback)
    v('again')


def environ_ex():
    import os
    print(os.environ.get('SECRET'))


# seperator_example()
# fstring_example()
# single_line_assignment()
# dry_example()
# test_settings()

# log_example()
# print(docstring_example.__doc__)
# print(add(1,2,3))
# print(get_time())
# fixed_return_type_example()
# dict_get_example()
# enumerate_example()
# override_builin_ex()
# try_except_example()
# test_star_import()

# truthy_compare_ex()
# unpacking_ex()
# pretty_print_ex()
# assign_value_same_time_ex()
# counter_example()
# first_class_object_ex()
environ_ex()
# with_example()