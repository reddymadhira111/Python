#1.manual sorting
l = [3,44,3,13,44,24,2,4,4]

def msort(l):
	if len(l) > 1:
		mid = int(len(l)/2)
		left = l[:mid]
		right = l[mid:]

		msort(left)
		msort(right)

		i = 0
		j = 0
		k = 0
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				l[k] = left[i]
				i = i+1
			else:
				l[k] = right[j]
				j = j+1
			k = k+1

		while i < len(left):
			l[k] = left[i]
			i = i+1
			k = k+1

		while j < len(right): 
			l[k] = right[j]
			j = j+1
			k = k+1
print(l)
msort(l)
print(l)


