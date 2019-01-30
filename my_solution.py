#This is my first code here
import os
def reverse_folder(dictionary):
	Filelist=[]
	for file in os.listdir(dictionary):
		Filelist.append(file)
		res = Filelist[::-1]
		print(res)

reverse_folder(dictionary)


