#This script shows different built in formatting options - written by Kody Noe


names = ['Jeff', 'Gary', 'Jill', 'Samantha', ]


print('Concatenation example...')
for name in names:
	print('Hi, ' + name)


print('\nJoin example...')
for name in names:
	print(''.join(['Hello, ', name]))


print('\nFormatting Example...')
for name in names:
	print('Hello, {}'.format(name))
