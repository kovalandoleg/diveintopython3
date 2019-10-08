'''Convert to and from Roman numerals
This program is part of 'Dive Into Python 3', a free Python book for
experienced programmers.  Visit http://diveintopython3.org/ for the
latest version.
'''
import re

class OutOfRangeError(ValueError): pass
class NotIntegerError(ValueError): pass
class InvalidRomanNumeralError(ValueError): pass

roman_numeral_map = (('M',  1000),
                     ('CM', 900),
                     ('D',  500),
                     ('CD', 400),
                     ('C',  100),
                     ('XC', 90),
                     ('L',  50),
                     ('XL', 40),
                     ('X',  10),
                     ('IX', 9),
                     ('V',  5),
                     ('IV', 4),
                     ('I',  1))
roman_numeral_pattern = re.compile('''
  ^                   # beginning of string
  M{0,4}              # thousands - 0 to 3 Ms
  (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                      #            or 500-800 (D, followed by 0 to 3 Cs)
  (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                      #        or 50-80 (L, followed by 0 to 3 Xs)
  (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                      #        or 5-8 (V, followed by 0 to 3 Is)
  $                   # end of string
  ''', re.VERBOSE)

to_roman_table = [ None ]   # list [ None, 'I', .. , 'MMMMCMXCIX' ]
from_roman_table = {}       # map { 'I':1, .. , 'MMMMCMXCIX':4999 }

def to_roman(n):
  '''convert integer to Roman numeral'''
  if not (0 < n < 5000):
    raise OutOfRangeError('number out of range (must be 1..4999)')
  if int(n) != n:
    raise NotIntegerError('non-integers can not be converted')
  return to_roman_table[n]

def from_roman(s):
  if not isinstance(s, str):
    raise InvalidRomanNumeralError('Input must be a string')
  if not s:
    raise InvalidRomanNumeralError('Input can not be blank')
  if s not in from_roman_table:
    raise InvalidRomanNumeralError('Invalid Roman numeral: {0}'.format(s))
  return from_roman_table[s]

def build_lookup_tables():
  def to_roman(n):
    result = ''
    for numeral, integer in roman_numeral_map:
      if n >= integer:
        result = numeral
        n -= integer
        break
    if n > 0:
      result += to_roman_table[n]
    return result

  for integer in range(1, 5000):
    roman_numeral = to_roman(integer)
    to_roman_table.append(roman_numeral)
    from_roman_table[roman_numeral] = integer

build_lookup_tables()

# def to_roman(n):
#   '''convert integer to Roman numeral'''

#   if not (0 < n < 5000):
#     raise OutOfRangeError('number out of range (must be 1..4999)')
#   result = ''
#   if not isinstance(n, int):
#     raise NotIntegerError('non-integers can not be converted')

#   for numeral, integer in roman_numeral_map:
#     while n >= integer:
#       result += numeral
#       # print('{0} - {1} add {2}'.format(n,integer,numeral))
#       n -= integer
#   return result

# def from_roman(s):
#   '''convert Roman to integer'''
#   if not s:
#     raise InvalidRomanNumeralError('Input can not be blank')
#   if not roman_numeral_pattern.search(s):
#     raise InvalidRomanNumeralError('Invalid Roman numeral: {0}'.format(s))

#   result = 0
#   index = 0
#   for numeral, integer in roman_numeral_map:
#     while s[index:index+len(numeral)] == numeral:
#       result += integer
#       index += len(numeral)
#   return result
