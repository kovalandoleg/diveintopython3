'''Yield
'''

def make_counter(x):
    print('entering make_counter')
    while True:
        yield x
        print('incrementing x')
        x = x + 1

if __name__ == '__main__':
    counter = make_counter(2)
    print(counter)
    print(next(counter))
    print(next(counter))
    print(next(counter))