def read_file(filename):
	lines = []
	with open(filename, 'r' , encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert_file(lines):
	person1_word_count = person1_sticker = person1_image = 0
	person2_word_count = person2_sticker = person2_image = 0
	name1 = name2 = None
	for line in lines:
		s = line.split(' ')
		name = s[1]
		if name == '政剛':
			name1 = name
			if s[2] == '貼圖':
				person1_sticker += 1
			elif s[2] == '圖片':
				person1_image += 1
			else:
				for m in s[2:]:
					person1_word_count += len(m)
		elif name == '阿鈞':
			name2 = name
			if s[2] == '貼圖':
				person2_sticker += 1
			elif s[2] == '圖片':
				person2_image += 1
			else:
				for m in s[2:]:
					person2_word_count += len(m)
		else:
			continue
	print('%s 一共說了 %d 個字 傳了 %d 張貼圖 傳了 %d 張圖片' % (name1, person1_word_count, person1_sticker, person1_image))
	print('%s 一共說了 %d 個字 傳了 %d 張貼圖 傳了 %d 張圖片' % (name2, person2_word_count, person2_sticker, person2_image))

def write_file(filename, lines):
	with open(filename, 'w', encoding='utf-8') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('[LINE]阿鈞.txt')
	convert_file(lines)
	# write_file('output.txt', lines)

main()