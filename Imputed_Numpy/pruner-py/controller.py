import subprocess
import os
import shutil

start = 16
end = 21
def numpy_to_quartets():
	direc = "Imputed_Quartets"
	if not os.path.exists(direc):
		os.mkdir(direc)

	for i in range(start,end):
		f_name = "imputed_array_" + str(i) + "_fp_removed"
		out_file = "Imputed_Quartets_" + str(i) + "_fp_removed"
		subprocess.call(['python','numpy_to_quartets.py',f_name])
		shutil.move(out_file,direc+"/"+out_file)

def quartets_wqmc_format():

	for i in range(start,end):
		input_dir = "Imputed_Quartets"
		input_file = "Imputed_Quartets_" + str(i) + "_fp_removed"
		subprocess.call(['python','Imputed_quartets_counter_maker.py',input_dir,input_file])

def file_rename():
	for i in range(start,end):
		direc = "Imputed_Quartets_wqmc_format"
		input_file = direc + "/Imputed_Quartets_with_count_" + str(i)
		output_file = direc + "/Imputed_Quartets_wqmc_" + str(i) + ".qrtt"
		os.rename(input_file,output_file)


# ./max-cut-tree qrtt='17_Imputed_Quartets_with_count' weights=on otre='Species_tree_imputed_17'

def quartets_to_sp_tree_wqmc():
	input_dir = "Imputed_Quartets_wqmc_format"
	
	output_dir = "Species_tree_Imputed_Prunener-py"
	if not os.path.exists(output_dir):
		os.mkdir(output_dir)



	for file_name in os.listdir(input_dir):
		print(file_name)
		idx = file_name.split("_")[3].split(".")[0]
		#print(idx)
		output_file = "Species_tree_imputed_" + idx + "_fp_removed"
		
		subprocess.call(['sudo','./max-cut-tree','qrtt='+input_dir+"/"+file_name,'weights=on','otre='+output_dir+"/"+output_file])
		print("done with " + idx)


def main():
	
	#numpy_to_quartets()
	# quartets_wqmc_format()
	# file_rename()
	quartets_to_sp_tree_wqmc()

if __name__ == '__main__':
	main()