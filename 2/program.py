import os
import sys

found_nums = list()
engine = list()
ooga = set()
sum = 0

with open("input.txt") as file:
	lines = file.readlines()
	line_num = 0
	for line in lines:
		line = line
		engine.append([line_num, line])
		line_num+=1

	for lineN in range(0, len(engine)):
		line = engine[lineN]
		print(line)
		number = str()
		building_number = False
		start_index = 0
		for index in range(0, len(line[1])):
			lineData = line[1]
			letter = str(lineData[index])
			if not building_number:
				start_index = index
			building_number = letter.isdigit()
			if building_number:
				number += letter
				end_index = index
			else:
				# print(sum)
				if len(number) != 0:
					extra_start = start_index-1
					if extra_start < 0:
						extra_start = 0
					extra_end =end_index+2
					if extra_end > len(line[1]):
						extra_end = len(line[1])-1
					print(f'data around number {lineData[extra_start:extra_end]}')
					added = False
					if lineN > 0:
						prev_line = engine[lineN-1][1]
						print(f'prev_line {prev_line}')
						prev_line_snippet = prev_line[extra_start:extra_end]
						for prev_line_letter in prev_line_snippet:
							prev_line_letter = str(prev_line_letter)
							if not prev_line_letter.isdigit() and prev_line_letter != '.' and prev_line_letter != '\n':
								print(f'prev_line {prev_line_snippet}')
								sum += int(lineData[start_index:end_index+1])
								ooga.add(int(lineData[start_index:end_index+1]))
								added = True
								break
					if lineN+1< len(engine) and not added:
						next_line_index = lineN+1
						next_line = engine[next_line_index][1]
						print(f'next_line {next_line}')
						next_line_snippet = next_line[extra_start:extra_end]
						for next_line_letter in next_line_snippet:
							next_line_letter = str(next_line_letter)
							if not next_line_letter.isdigit() and next_line_letter != '.' and next_line_letter != '\n':
								print(f'next_line {next_line_snippet}')
								sum += int(lineData[start_index:end_index+1])
								ooga.add(int(lineData[start_index:end_index+1]))
								added = True
								break
					if not added:
						for letter in lineData[extra_start:extra_end]:
							if not str(letter).isdigit() and str(letter) != '.' and letter != '\n':
								print(f'this_line {lineData[extra_start:extra_end]}')
								sum += int(lineData[start_index:end_index+1])
								ooga.add(int(lineData[start_index:end_index+1]))
								break
					number = str()
				# print(sum)
	print(sum)
	fff = 0
	for item in ooga:
		fff += item
	print(fff)
