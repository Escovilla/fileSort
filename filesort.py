import subprocess


import os
import os.path
from os import path
import shutil
from datetime import datetime
import getpass 

date = datetime.now()
date = date.strftime("%m-%d-%y")

os.system("clear")
def cont():
	username = getpass.getuser()
	print("\n")
	print("Hello "+username.upper()+",                  Integrate.py                        Date:"+date)


	print("\n")
	name = raw_input("Enter Module CFUND, SYSTEMSETTINGS, CIF, CLITE\nMODEL all letters should be in all caps: ")


	def jspFunc():

		print("\n")
		print "If you want to enter multiple names,\nmake sure to use a comma ', ' and a space next to it"
		print("\n")
		

	

		name = raw_input("Enter name: ")

		if name != "":

			toArr = name.split(", ")

			#checks if dir exists
			check = str(path.exists("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date))
			

			try:
				#code creates dir
				if check == "False":
					os.mkdir("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date)
					print "- BACK UP CREATED"
					os.mkdir("/home/nsdevs-u01/Desktop/Link to Developer/2019/NIKO BACK UP/WAR/WAR_"+date)
					print "- WAR FOLDER CREATED"
				for x in toArr:

					
					paths = [line[0:] for line in subprocess.check_output("find /home/nsdevs-u01/Desktop/Link\ to\ workspace/CFUND -iname '"+x+"'", shell=True).splitlines()]
					
					paths2 = [line[0:] for line in subprocess.check_output("find /home/nsdevs-u01/Desktop/Link\ to\ workspace/CERPSYS -iname '"+x+"'",	shell=True).splitlines()]
					
					
						
					listToStr = ''.join([str(elem) for elem in paths])
					listToStr2 = ''.join([str(elem) for elem in paths2])

					print "- FROM "+listToStr
					print "- TO "+listToStr2


					checker = str(path.exists(listToStr2))
					

					checkerer = str(os.path.isfile("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/"+x))
					
	
	
					checkerDirRep = str(path.exists("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/repeated_file_"+x+"_1/"+x))
					exis =  os.path.dirname("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/repeated_file_"+x+"_1/"+x)	
	
					sliptter = list(exis)
					getNum = sliptter[-1]	
	
					newcount = int(getNum) + 1	
					forConcat = str(newcount)

					print checkerer
					print checker
					if checker == "False":

						#code copy files
						shutil.copy2(listToStr, listToStr2)

					else:
		
						if checkerDirRep == "True":
			
			
							os.mkdir("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/repeated_file_"+x+"_"+forConcat) 

							#code moves files
							shutil.move( listToStr2, "/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/repeated_file_"+x+"_"+forConcat+"/"+x)
			
						else:
							
							if checkerer == "True":
								
								os.mkdir("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/repeated_file_"+x+"_1") 

								#code moves files
								shutil.move( listToStr2, "/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/repeated_file_"+x+"_1/"+x)
								print "IMHERE"
							
							else:
								#code moves files
								shutil.move(listToStr2, "/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/"+x)

						#code copy files
						shutil.copy2(listToStr, listToStr2)


				print "\n"
				print "Success"

			except NameError:
				print "\nnot defined\n"
			
			
		else:
			print "\nInput data!"
	#--------------------------------------------------------------------------------CIF--------------------------------------------------------------------------------------------------------------------------------
	#--------------------------------------------------------------------------------CIF--------------------------------------------------------------------------------------------------------------------------------
	#--------------------------------------------------------------------------------CIF--------------------------------------------------------------------------------------------------------------------------------
	#--------------------------------------------------------------------------------CIF--------------------------------------------------------------------------------------------------------------------------------
	#--------------------------------------------------------------------------------CIF--------------------------------------------------------------------------------------------------------------------------------
	def CIF():

		print("\n")
		print "If you want to enter multiple names,\nmake sure to use a comma ', ' and a space next to it"
		print("\n")
		

	

		name = raw_input("Enter name: ")

		if name != "":

			toArr = name.split(", ")

			#checks if dir exists
			check = str(path.exists("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date))
			

			try:
				#code creates dir
				if check == "False":
					os.mkdir("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date)
					print "- BACK UP CREATED"
					os.mkdir("/home/nsdevs-u01/Desktop/Link to Developer/2019/NIKO BACK UP/WAR/WAR_"+date)
					print "- WAR FOLDER CREATED"
				for x in toArr:

					
					paths = [line[0:] for line in subprocess.check_output("find /home/nsdevs-u01/Desktop/Link\ to\ workspace/CIF -iname '"+x+"'", shell=True).splitlines()]
					
					paths2 = [line[0:] for line in subprocess.check_output("find /home/nsdevs-u01/Desktop/Link\ to\ workspace/CERPSYS -iname '"+x+"'",	shell=True).splitlines()]
					
					
						
					listToStr = ''.join([str(elem) for elem in paths])
					listToStr2 = ''.join([str(elem) for elem in paths2])

					print "- FROM "+listToStr
					print "- TO "+listToStr2


					checker = str(path.exists(listToStr2))
					

					checkerer = str(os.path.isfile("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/"+x))
					
	
	
					checkerDirRep = str(path.exists("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/repeated_file_"+x+"_1/"+x))
					exis =  os.path.dirname("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/repeated_file_"+x+"_1/"+x)	
	
					sliptter = list(exis)
					getNum = sliptter[-1]	
	
					newcount = int(getNum) + 1	
					forConcat = str(newcount)

					print checkerer
					print checker
					if checker == "False":

						#code copy files
						shutil.copy2(listToStr, listToStr2)

					else:
		
						if checkerDirRep == "True":
			
			
							os.mkdir("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/repeated_file_"+x+"_"+forConcat) 

							#code moves files
							shutil.move( listToStr2, "/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/repeated_file_"+x+"_"+forConcat+"/"+x)
			
						else:
							
							if checkerer == "True":
								
								os.mkdir("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/repeated_file_"+x+"_1") 

								#code moves files
								shutil.move( listToStr2, "/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/repeated_file_"+x+"_1/"+x)
								print "IMHERE"
							
							else:
								#code moves files
								shutil.move(listToStr2, "/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/"+x)

						#code copy files
						shutil.copy2(listToStr, listToStr2)


				print "\n"
				print "Success"

			except NameError:
				print "\nnot defined\n"
			
			
		else:
			print "\nInput data!"
	#--------------------------------------------------------------------------------CLITE--------------------------------------------------------------------------------------------------------------------------------
	#--------------------------------------------------------------------------------CLITE--------------------------------------------------------------------------------------------------------------------------------
	#--------------------------------------------------------------------------------CLITE--------------------------------------------------------------------------------------------------------------------------------
	#--------------------------------------------------------------------------------CLITE--------------------------------------------------------------------------------------------------------------------------------
	#--------------------------------------------------------------------------------CLITE--------------------------------------------------------------------------------------------------------------------------------
	def CLITE():

		print("\n")
		print "If you want to enter multiple names,\nmake sure to use a comma ', ' and a space next to it"
		print("\n")
		

	

		name = raw_input("Enter name: ")

		if name != "":

			toArr = name.split(", ")

			#checks if dir exists
			check = str(path.exists("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date))
			

			try:
				#code creates dir
				if check == "False":
					os.mkdir("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date)
					print "- BACK UP CREATED"
					os.mkdir("/home/nsdevs-u01/Desktop/Link to Developer/2019/NIKO BACK UP/WAR/WAR_"+date)
					print "- WAR FOLDER CREATED"
				for x in toArr:

					
					paths = [line[0:] for line in subprocess.check_output("find /home/nsdevs-u01/Desktop/Link\ to\ workspace/CLITE -iname '"+x+"'", shell=True).splitlines()]
					
					paths2 = [line[0:] for line in subprocess.check_output("find /home/nsdevs-u01/Desktop/Link\ to\ workspace/CERPSYS -iname '"+x+"'",	shell=True).splitlines()]
					
					
						
					listToStr = ''.join([str(elem) for elem in paths])
					listToStr2 = ''.join([str(elem) for elem in paths2])

					print "- FROM "+listToStr
					print "- TO "+listToStr2


					checker = str(path.exists(listToStr2))
					

					checkerer = str(os.path.isfile("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/"+x))
					
	
	
					checkerDirRep = str(path.exists("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/repeated_file_"+x+"_1/"+x))
					exis =  os.path.dirname("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/repeated_file_"+x+"_1/"+x)	
	
					sliptter = list(exis)
					getNum = sliptter[-1]	
	
					newcount = int(getNum) + 1	
					forConcat = str(newcount)

					print checkerer
					print checker
					if checker == "False":

						#code copy files
						shutil.copy2(listToStr, listToStr2)

					else:
		
						if checkerDirRep == "True":
			
			
							os.mkdir("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/repeated_file_"+x+"_"+forConcat) 

							#code moves files
							shutil.move( listToStr2, "/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/repeated_file_"+x+"_"+forConcat+"/"+x)
			
						else:
							
							if checkerer == "True":
								
								os.mkdir("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/repeated_file_"+x+"_1") 

								#code moves files
								shutil.move( listToStr2, "/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/repeated_file_"+x+"_1/"+x)
								print "IMHERE"
							
							else:
								#code moves files
								shutil.move(listToStr2, "/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/"+x)

						#code copy files
						shutil.copy2(listToStr, listToStr2)


				print "\n"
				print "Success"

			except NameError:
				print "\nnot defined\n"
			
			
		else:
			print "\nInput data!"


	#--------------------------------------------------------------------------------SYS--------------------------------------------------------------------------------------------------------------------------------
	#--------------------------------------------------------------------------------SYS--------------------------------------------------------------------------------------------------------------------------------
	#--------------------------------------------------------------------------------SYS--------------------------------------------------------------------------------------------------------------------------------
	#--------------------------------------------------------------------------------SYS--------------------------------------------------------------------------------------------------------------------------------
	#--------------------------------------------------------------------------------SYS--------------------------------------------------------------------------------------------------------------------------------
	def SYS():

		print("\n")
		print "If you want to enter multiple names,\nmake sure to use a comma ', ' and a space next to it"
		print("\n")
		

	

		name = raw_input("Enter name: ")

		if name != "":

			toArr = name.split(", ")

			#checks if dir exists
			check = str(path.exists("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date))
			

			try:
				#code creates dir
				if check == "False":
					os.mkdir("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date)
					print "- BACK UP CREATED"
					os.mkdir("/home/nsdevs-u01/Desktop/Link to Developer/2019/NIKO BACK UP/WAR/WAR_"+date)
					print "- WAR FOLDER CREATED"
				for x in toArr:

					
					paths = [line[0:] for line in subprocess.check_output("find /home/nsdevs-u01/Desktop/Link\ to\ workspace/SYSTEMSETTINGS -iname '"+x+"'", shell=True).splitlines()]
					
					paths2 = [line[0:] for line in subprocess.check_output("find /home/nsdevs-u01/Desktop/Link\ to\ workspace/CERPSYS -iname '"+x+"'",	shell=True).splitlines()]
					
					
						
					listToStr = ''.join([str(elem) for elem in paths])
					listToStr2 = ''.join([str(elem) for elem in paths2])

					print "- FROM "+listToStr
					print "- TO "+listToStr2


					checker = str(path.exists(listToStr2))
					

					checkerer = str(os.path.isfile("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/"+x))
					
	
	
					checkerDirRep = str(path.exists("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/repeated_file_"+x+"_1/"+x))
					exis =  os.path.dirname("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/repeated_file_"+x+"_1/"+x)	
	
					sliptter = list(exis)
					getNum = sliptter[-1]	
	
					newcount = int(getNum) + 1	
					forConcat = str(newcount)

					print checkerer
					print checker
					if checker == "False":

						#code copy files
						shutil.copy2(listToStr, listToStr2)

					else:
		
						if checkerDirRep == "True":
			
			
							os.mkdir("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/repeated_file_"+x+"_"+forConcat) 

							#code moves files
							shutil.move( listToStr2, "/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/repeated_file_"+x+"_"+forConcat+"/"+x)
			
						else:
							
							if checkerer == "True":
								
								os.mkdir("/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/repeated_file_"+x+"_1") 

								#code moves files
								shutil.move( listToStr2, "/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/repeated_file_"+x+"_1/"+x)
								print "IMHERE"
							
							else:
								#code moves files
								shutil.move(listToStr2, "/home/nsdevs-u01/Desktop/research/backuppp/backup_"+date+"/"+x)

						#code copy files
						shutil.copy2(listToStr, listToStr2)


				print "\n"
				print "Success"

			except NameError:
				print "\nnot defined\n"
			
			
		else:
			print "\nInput data!"

	if name == "CFUND" :
		os.system("clear")
		jspFunc()
	if name == "CIF" :
		os.system("clear")
		CIF()
	if name == "CLITE" :
		os.system("clear")
		CLITE()
	if name == "SYS" :
		os.system("clear")
		SYS()

	if name != "CFUND" and "CIF" and "DAO" and "MODEL" :
		print "\n"
		print "Invalid Module"

	yn = raw_input("\nContinue? y/n: ")
	if yn == "y":
		os.system("clear")
		cont()	
	
cont()	
