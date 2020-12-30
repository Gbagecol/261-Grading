'''
Author: Tanner Lorenz
261 Grading Script Version 0.1
Feel free to use or modify this software however you wish. I hold no
responsibility for anything that happens to break or go wrong when you use this
program.
'''


import sys


#penalties from syllabus applied to only the assignment points (not the lab
#points)
DEFAULT_PENALTIES = [
	("No extraneous files", "Submitted extra files other than code files", 0.05),
	("No missing files", "Missing some necessary files", 0.1),
	("Code compiles with g++", "Code does not compile", 0.25)
]


#verify args
if len(sys.argv) != 3:
	print("Usage: gradingScript.py path/to/rubric/file path/to/grades/file")
	sys.exit()

#input and output file
INPUT_FILE = sys.argv[1]
OUTPUT_FILE = sys.argv[2]

#load rubric
with open(INPUT_FILE, 'r') as inputFile:
	rubric = inputFile.readlines()
	possiblePoints = int(rubric[0])

#grade students until told to stop
while True:

	student = input("Enter student name: ") #get student name

	#check current student's grade
	with open(OUTPUT_FILE, 'a') as outputFile:

		studentTotal = possiblePoints

		outputFile.write(student + "\n\n") #write student name

		#check each criteria
		for x in range(1, len(rubric)):

			#get criteria parameters
			criteria = rubric[x].split(":")
			pointValue = float(criteria[0])
			prompt = criteria[1]
			result = criteria[2]

			#determine if this criteria is extra credit
			if criteria[0][0] == '+':
				prompt = "[EXTRA CREDIT] " + prompt

			#check if student follows criteria
			response = input(prompt + "? ")
			while response != 'y' and response != 'n':
				response = input("y or n: ")

			#deduct/add points based on answer/extra credit
			if response == 'n' and criteria[0][0] != '+':
				studentTotal -= pointValue
				outputFile.write("-" + str(pointValue) + ": " + result)
			elif response == 'y' and criteria[0][0] == '+':
				studentTotal += pointValue
				outputFile.write("+" + str(pointValue) + ": " + result)

		#TODO: add syllabus penalties for assignment

		#prompt for any extra notes
		notes = input("Notes (or just hit enter for no notes): ")
		if notes != "":
			outputFile.write("\n\nNotes: " + notes + "\n")

		outputFile.write("\n\nTotal: " + str(studentTotal) + "\n---------------------------------------------------------------------\n\n")

	#ask to grade another student
	nextStudent = input("Grade another student? ")
	while nextStudent != 'y' and nextStudent != 'n':
		nextStudent = input("y or n: ")

	if nextStudent == 'n':
		break