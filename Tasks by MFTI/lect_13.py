'''
Модуль описывающий струкруду данных - стэк
>>> clear()
>>> is_empty()
True
>>> push(1)
>>> push(2)
>>> push(3)
>>> is_empty()
False
>>> pop()
3
>>> pop()
2
>>> pop()
1
>>> is_empty()
True
'''

_stack = []

def push( x ):
	'''
	Добавляет элемент х в конец стека
	
	>>> size = len(_stack)
	>>> push(5)
	>>> len(_stack) - size
	1
	>>> _stack[-1]
	5
	'''
	_stack.append( x )

def pop():
	x = _stack.pop()
	return x

def clear():
	_stack.clear()

def is_empty():
	return len( _stack ) == 0

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=False)

import A_stack

def is_braces_sequence_correct( s: str ):
	'''
	Проверяет корректность скобочной последовательности
	из круглых и квадратных скобок () []
	>>> is_braces_sequence_correct( '(([()]))[]' )
	True
	>>> is_braces_sequence_correct( '([)]' )
	False
	>>> is_braces_sequence_correct( '(' )
	False
	>>> is_braces_sequence_correct( ']' )
	False
	'''
	for brace in s:
		if brace not in '()[]':
			continue
		if brace in '([':
			A_stack.push( brace )
		else:
			assert brace in ')]', 'Ожидалась закрывающая скобка: ' + str( brace )
			if A_stack.is_empty():
				return False
			left = A_stack.pop()
			assert left in '([', 'Ожидалась закрывающая скобка: ' + str( brace )
			if left == '(':
				right = ')'
			elif left == '[':
				right = ']'
			if right != brace:
				return False
	return A_stack.is_empty()

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=False)