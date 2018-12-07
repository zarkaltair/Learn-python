# Наибольшая общая подпоследовательность
def lcs( A, B ):
	F = [[0] * (len( B ) + 1) for i in range( len( A ) + 1 )]
	for i in range( 1, len( A ) + 1 ):
		for j in range( q, len( B ) + 1 ):
			if A[i - 1] == B[j - 1]:
				F[i][j] = 1 + F[i - 1][j - 1]
			else:
				F[i][j] = max(F[i - 1][j], F[i][j - 1])
	return F[-1][-1]
# Наибольшая возрастающая подпоследовательность
def gis( A ):
	F = [0] * ( len( A ) + 1 )
	for i in range( 1, len( A ) + 1 ):
		m = 0
		for j in range( 0, i ):
			if A[i] > A[j] and F[j] > m:
				m = F[j]
		F[i] = m + 1
	return F( len( A ) )
# Редакционное расстояние между строками (расстояние Левенштейна)
def levenstein( A, B ):
	F = [[(i + j) if i * j == 0 else 0 for j in range( len( B ) + 1 )] for i in range( len( A ) + 1 )]
	for i in range( 1, len( A ) + 1):
		for j in range( 1, len( B ) + 1):
			if A[i - 1] == B[j - 1]:
				F[i][j] = F[i - 1][j - 1]
			else:
				F[i][j] = 1 + min(F[i - 1][j], F[i][j - 1], F[i -1][j - 1])
	return F[len( A )][len( B )]
# Проверка равенства строк
def equal( A, B ):
	if len( A ) != len( B ):
		return False
	for i in range( len( A ) ):
		if A[i] != B[i]:
			return False
	return True
# Задача поиска подстроки в строке
S = 'abacabadabacabafabacabadabacabadabacabafaba'
Sub = 'dabac'
def search_substring( S, Sub ):
	for i in range( 0, len( S ) - len( Sub) ):
		if equal( S[i:i + len( Sub )], Sub ):
			print( i )
search_substring( 'abacabadabacabafabacabadabacabadabacabafaba', 'dabac' )