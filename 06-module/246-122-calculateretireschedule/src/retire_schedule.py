#! /usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
def calculate():
	current_age = int(input('What is your current age?'))
	retire_age = int(input('At what age would you like to retire?'))

	left_year = retire_age - current_age
	current_year = datetime.datetime.now().year
	retire_year = current_year + left_year

	if retire_year >= current_year:
		print(f'You have {left_year} years left until you can retire.')
		print(f'It\'s {current_year}, so you can retire in {retire_year}.')
	else:
		print(f'You have 0 years left until you can retire.')
		print(f'It\'s {current_year}, so you can retire in {retire_year}.')
	return
