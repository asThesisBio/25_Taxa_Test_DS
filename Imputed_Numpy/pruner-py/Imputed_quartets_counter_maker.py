import sys
import os

if(len(sys.argv) < 3):
	print("format: <handle.py> input_dir input_file")
	exit()

input_dir = sys.argv[1]
input_file = sys.argv[2]


file_sep = input_file.split("_")
print("working with replicate -> ", file_sep[2])

input_file_name = input_file

out_file="Imputed_Quartets_with_count_" + file_sep[2]

with open(input_dir +  "/" + input_file_name, "r") as input_file:
	data = input_file.read()

out_dir = "Imputed_Quartets_wqmc_format"
if not os.path.exists(out_dir):
	os.mkdir(out_dir)


lines=data.split("\n")
no_of_lines=len(lines)
dictionary={}

for i in range(0,no_of_lines):
	parts=lines[i].split('|')
	left_part=parts[0].split(',')
	right_part=parts[1].split(',')
	q1=left_part[0]
	q2=left_part[1]
	q3=right_part[0]
	q4=right_part[1]

	seq_1=q1+","+q2+","+q3+","+q4
	seq_2=q2+","+q1+","+q3+","+q4
	seq_3=q1+","+q2+","+q4+","+q3
	seq_4=q2+","+q1+","+q4+","+q3
	seq_5=q3+","+q4+","+q1+","+q2
	seq_6=q3+","+q4+","+q2+","+q1
	seq_7=q4+","+q3+","+q1+","+q2
	seq_8=q4+","+q3+","+q2+","+q1

	key=""
	count=0

	if dictionary.get(seq_1)!=None:
		key=seq_1
		count=dictionary[key]
	elif dictionary.get(seq_2)!=None:
		key=seq_2
		count=dictionary[key]
	elif dictionary.get(seq_3)!=None:
		key=seq_3
		count=dictionary[key]
	elif dictionary.get(seq_4)!=None:
		key=seq_4
		count=dictionary[key]
	elif dictionary.get(seq_5)!=None:
		key=seq_5
		count=dictionary[key]
	elif dictionary.get(seq_6)!=None:
		key=seq_6
		count=dictionary[key]
	elif dictionary.get(seq_7)!=None:
		key=seq_7
		count=dictionary[key]
	elif dictionary.get(seq_8)!=None:
		key=seq_8
		count=dictionary[key]
	else:
		key=seq_1
		#print(key)

	dictionary[key]=count+1


string=""
for key,value in dictionary.items():
	parts=key.split(',')
	q1 = parts[0]
	q2 = parts[1]
	q3 = parts[2]
	q4 = parts[3]
	string+=q1+","+q2+"|"+q3+","+q4+":"+str(value)+"\n"

with open(out_dir+"/"+out_file, "w+") as f:
	f.write(string)

