def find( number, A ):
	''' ищет number в А и возвращает True, если такой есть и False, если такого нет '''
	for x in A:
		if number == x:
			return True
	return False

def generate_permetations( N:int, M:int = -1, prefix = None):
	''' Генерация всех перестановок N числе в M позициях, с перфиксом prefix '''
	M = N if M == -1 else M  # по умолчанияю N чисел в N позициях
	prefix = prefix or []
	if M == 0:
		print( *prefix, end=', ', sep='' )
		return
	for number in range( 1, N + 1 ):
		if find( number, prefix ):
			continue
		prefix.append( number )
		generate_permetations( N, M - 1, prefix )
		prefix.pop()

generate_permetations( 3 )
