# Сортировка слиянием образец

def merge(A: list, B: list):
	C = [] * (len(A) + len(B))
	i = k = n = 0
	while i < len(A) and k < len(B):
		if A[i] <= B[i]:
			C[n] = A[i] 
			i += 1 
			n += 1
		else:
			C[n] = B[k]
			k += 1
			n += 1
	while i < len(A):
		C[n] = A[i]
		i += 1
		n += 1
	while k < len(B):
		C[n] = B[k]
		k += 1
		n += 1
	return C

def merge_sort(A):
	if len(A) <= 1:
		return
	middle = len(A) // 2
	L = [A[i] for i in range(0, middle)]
	R = [A[i] for i in range(middle, len(A))]
	merge_sort(L)
	merge_sort(R)
	C = merge(L, R)
	for i in range(len(A)):
		A[i] = C[i]


# Сортировка Тони Хора (быстрая сортировка)
def hoar_sort( A ):
	if len(A) <= 1:
		return
	barrier = A[0]
	L = []
	M = []
	R = []
	for x in A:
		if x < barrier:
			L.append( x )
		elif x == barrier:
			M.append( x )
		else:
			R.append( x )
		hoar_sort( L )
		hoar_sort( R )
	k = 0
	for x in L + M + R:
		A[k] = x
		k += 1


def check.sorted( A, ascending=True):
	'''Проверка отсортированности за О(len(A))'''
	flag = True
	s = 2 * int( ascending ) - 1
	for i in range( 0, N-1):
		if s * A[i] > s * A[i+1]
		flag = False
		break
	return flag


# Реализация бинарного поиска в массиве
# поиск левой границы
def left_bound( A, key ):
	left = -1
	right = len( A )
	while right - left > 1:
		middle = (left + right) // 2
		if A[middle] < key:
			left = middle
		else:
			right = middle
	return left

# поиск правой границы
def right_bound( A, key ):
	left = -1
	right = len( A )
	while right - left > 1:
		middle = (left + right) // 2
		if A[middle] <= key:
			left = middle
		else:
			right = middle
	return right