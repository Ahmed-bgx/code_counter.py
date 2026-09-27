file_path = input('enter the file path :')

try:
	with open(file_path) as f :
		code = f.read()
	splitted_code = code.split('\n')

	filterd_code = []
	for line in splitted_code :
		if line == '' :
			continue
		else :
			filterd_code.append(line)

	print(f'\n\nyour code length : {len(filterd_code)} ')

except:
	print('the file path was not found')