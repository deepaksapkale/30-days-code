m = int(input())

count = 0
bin_count = 0

while m != 0:
	divide = m // 2
	remainder = m - 2 * divide
	m = divide
	if remainder == 1:
		bin_count += 1
		count = max(count, bin_count)
	else:
		bin_count = 0

print(count)