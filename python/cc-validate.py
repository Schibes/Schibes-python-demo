#!/usr/bin/env python3

import re

my_cc = input("Enter credit card number: ")

def is_good_start_digit(my_cc):
  startdigit_pattern = r'^[4-6]'
  if re.match(startdigit_pattern, my_cc):
    return True
  else:
    return False

def is_good_cc_length(my_cc):
  alldigits_pattern = r'\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d'
  dash_pattern = r'\d\d\d\d-\d\d\d\d-\d\d\d\d-\d\d\d\d'
  if re.match(alldigits_pattern, my_cc):
    return True
  else:
    if re.match(dash_pattern, my_cc):
      return True
    else:
      return False

def is_good_nonrepeating_digits(my_cc):
  repeat_pattern = r'(\d)\1{3}'
  my_cc_digits = re.sub('[^0-9]','', my_cc)
  if re.search(repeat_pattern, my_cc_digits):
    return False
  else:
    return True

if is_good_start_digit(my_cc):
  if is_good_cc_length(my_cc):
    if is_good_nonrepeating_digits(my_cc):
      print("Valid")
    else:
      print("Invalid")
  else: 
    print("Invalid")
else:
  print("Invalid")
