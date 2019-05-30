dict={}  #key=persian val=english
dict_r={}#key=english val=persian
def make_files_ready(input_name):

	global dict_r,dict
	input_file=open(input_name)
	file_raw_content=input_file.read().split(" " or'\n')
	input_file.close()
	import csv
	
	with open('..\\in\\Entries.csv', 'r') as csvFile:
		reader = csv.reader(csvFile)
		for row in reader:
			data2= row[0]
			data1=row[1]
			dict[data1]=data2
			dict_r[data2]=data1
	csvFile.close()
	file_second_content=""
	for i in file_raw_content:
		if (i in dict):
			file_second_content+=dict[i]
	return file_second_content
	
def main_function(content,output_name):
	global dict_r,dict
	# global total_size
	total_size=len(content)
	table= []
	for  i in range(total_size):
		table.append([])
	raw_of_table=[]
	total_size=len(content)
	for i in range(0,total_size):
		for j in range (0,i):
			raw_of_table=[]
			cur_word=content[j:i+1]
			if(cur_word in dict_r):
				#this word has meaning so in i index we add all possible sentence from j + this word
				#if j!=0 and with no sentence we'll ignore it
				if(j==0):
					raw_of_table.append([cur_word])
				else:
					if(table[j-1]==0):
						pass
					else:
						for t in table[j-1]:
							k=t[:]
							k.append(cur_word)
							raw_of_table.append(k)
			for t in raw_of_table:
				table[i].append(t)
	
	#for i in table[total_size-1]:
	for i in table[total_size-1]:
		string_out=""
		for j in i:
			string_out+=dict_r[j]+"-"
		#print (string_out[:-1])
		file1=open(output_name,"a")
		file1.write(string_out[:-1])
		file1.write("\n")
		file1.close()
	

for i in range(1,6):
	input_name="..\\in\\in_"+str(i)+".txt"
	output_name="..\\out\\out_"+str(i)+".txt"
	content=make_files_ready(input_name)
	main_function(content,output_name)
