lines = []
with open('LINErecord.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ')
	time = s[0][:5]
	name = s[1][:6]
	print('time: ', time)
	print('name: ', name)

lines2 = []
with open('LINErecord2.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		lines2.append(line.strip())

for line in lines2:
	s = line.split(' ')
	time = s[0][:5]	# In python, string can be regarded as a list, s[0][:5]:s清單中第一個位置的前5個字
	name = s[0][5:]
	print('time: ', time)
	print('name: ', name)