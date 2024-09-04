#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re

def validate():
    first_name = input('Enter the first name:')
    last_name = input('Enter the last name:')
    zip_code = input('Enter the ZIP code:')
    employee_id = input('Enter and employee ID:')

    if len(first_name) == 0:
        print('The first name must be filled in.')
    elif 2 > len(first_name) > 0:
        print('\"{0}\" is not a valid first name. It is too short.' .format(first_name))

    if len(last_name) == 0:
        print('The last name must be filled in.')
    elif 2 > len(last_name) > 0:
        print('\"{0}\" is not a valid last name. It is too short.' .format(last_name))

    if not zip_code.isdigit():
        print('The ZIP code must be numeric.')

    if len(employee_id) != 7:
        print('{0} is not a valid ID.' .format(employee_id))
    elif not employee_id[0].isalpha() or not employee_id[1].isalpha():
        print('{0} is not a valid ID.' .format(employee_id))
    elif employee_id[2] != '-':
        print('{0} is not a valid ID.' .format(employee_id))
    elif not employee_id[3].isdigit() or not employee_id[4].isdigit() or not employee_id[5].isdigit() or not employee_id[6].isdigit():
        print('{0} is not a valid ID.' .format(employee_id))

    return
