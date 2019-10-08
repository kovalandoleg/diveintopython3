# -*- coding: utf-8 -*-
import string
upper = set(string.ascii_uppercase)
lower = set(string.ascii_lowercase)
digits = set(string.digits)


def checkio(data):
  'Return True if password strong and False if not'
  letters = set(data)
  print(upper & letters)
  print(lower & letters)
  print(digits & letters)
  return bool(len(data) >= 10 and upper & letters and lower & letters and digits & letters)

#Some hints
#Just check all conditions


if __name__ == '__main__':
  #These "asserts" using only for self-checking and not necessary for auto-testing
  assert checkio('A1213pokl') == False, "1st example"
  assert checkio('bAse730onE4') == True, "2nd example"
  assert checkio('asasasasasasasaas') == False, "3rd example"
  assert checkio('QWERTYqwerty') == False, "4th example"
  assert checkio('123456123456') == False, "5th example"
  assert checkio('QwErTy911poqqqq') == True, "6th example"
  print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
