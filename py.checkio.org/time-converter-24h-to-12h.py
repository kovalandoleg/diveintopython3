def time_converter(time):
    hour, minutes = time.split(':')
    hour = int(hour)
    apm = 'p' if hour >= 12 else 'a'
    hour = hour - 12 if hour > 12 else hour
    hour = 12 if hour == 0 else hour
    return "{}:{} {}.m.".format(hour, minutes, apm)

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")