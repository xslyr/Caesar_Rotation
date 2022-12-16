#!/usr/bin/python
#encoding: utf-8

import sys, string, collections, traceback
from colorama import Fore as F
from colorama import Style


def print_help( filename ):
	print('''Usage:
\tpython3 {} [-v] [-az] [-AZ] [-09] hash-2-decode 
\t Default dictionary: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
\n
\t-v: Verbose mode.
\t-09: Exclude Numbers from dictionary
\t-AZ: Exclude Uppercase from dictionary
\t-az: Exclude Lowercase from dictionary

'''.format(filename))


def try_ciphers( arguments ):
	
	print(F.BLUE+'*************************')
	print('hash2decode: '+F.RED+'{}'.format(arguments['hash2decode']))
	print(F.BLUE+'*************************')
	
	decoded = []
	string_list = ''
	
	dL, dL = 0, 0
	
	if not arguments['-az']: 
		string_list+= string.ascii_lowercase 
		dl =  26
	if not arguments['-AZ']: 
		string_list+= string.ascii_uppercase 
		dL = 26
		
	if not arguments['-09']: string_list+= string.digits
		
	string_list = collections.deque(string_list)

	for shift_value in range( len(string_list) ):
		
		shifted_list = string_list.copy()
		shifted_list.rotate(shift_value)
		shifted_list = ''.join(list(shifted_list))
		
		if arguments['-v']:
			print(F.BLUE, '\nshift = {} : '.format(shift_value), end='')
			print(F.LIGHTBLACK_EX, '({})'.format(shifted_list))
			print('\n'+F.RED+'\t' ,end='')
		else:
			print(F.RED, end='')
			
		for character in arguments['hash2decode']:
			
			if character in string.ascii_lowercase and not arguments['-az']:
				position = string.ascii_lowercase.index(character)
				decoded.append(shifted_list[position])
				
			elif character in string.ascii_uppercase and not arguments['-AZ']:
				position = string.ascii_uppercase.index(character)
				if not arguments['-az']: position += dl
				decoded.append(shifted_list[position])
				
			elif character in string.digits and not arguments['-09']:
				position = string.digits.index(character)
				if not arguments['-az']: position += dl
				if not arguments['-AZ']: position += dL
				decoded.append(shifted_list[position])
				
			else:
				decoded.append(character)
		
		print(''.join(decoded), end='\n')
		decoded = []


if __name__ == '__main__':
	
	arg_list = ['-v','-09','-AZ','-az']
	arguments = {
		'-v' : False,
		'-09': False,
		'-AZ':False,
		'-az':False,
		'hash2decode': ''
	}
	
	try:
		if sys.argv[0] == sys.argv[-1]:
			print_help(sys.argv[0])
		
		for arg in sys.argv:
			if arg in arg_list:
				arguments[arg]= True
			
			elif ('.py' not in arg) and (arg not in arg_list) and (arg == sys.argv[-1]) :
				arguments['hash2decode'] = arg
				try_ciphers(arguments)
		
	except Exception as e:
		traceback.print_exc()
		print('\n\n',F.RED)
		print(e, end='\n\n')
	
	print(Style.RESET_ALL)
		
