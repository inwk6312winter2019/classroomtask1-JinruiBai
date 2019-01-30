#This is my first code here
import os
def traverse_list(dictionary):
	Filelist=[]
	for file in os.listdir(dictionary):
		Filelist.append(file)
		print(Filelist)

