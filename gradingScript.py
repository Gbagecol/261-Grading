'''
Author: Tanner Lorenz
261 Grading Script Version 1.0
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
INPUT_FILE_PATH = sys.argv[1]
OUTPUT_FILE_PATH = sys.argv[2]

#load rubric
with open(INPUT_FILE_PATH, 'r') as inputFile:

	rubric = inputFile.readlines()

	#store different point totals
	totalPoints = int(rubric[0])
	labPoints = int(rubric[1])
	assignmentPoints = int(rubric[2])

#grade students until told to stop
while True:

	student = input("Enter student name: ") #get student name

	#check current student's grade
	with open(OUTPUT_FILE_PATH, 'a') as outputFile:

		studentTotal = totalPoints #TODO: probably could be removed, but too lazy right now
		studentLab = labPoints
		studentAssignment = assignmentPoints

		outputFile.write(student + "\n\n") #write student name

		#check each criteria
		for x in range(3, len(rubric)):

			#get criteria parameters
			criteria = rubric[x].split(":")
			pointValue = float(criteria[0])
			pointType = criteria[1]
			prompt = criteria[2]
			result = criteria[3]

			#determine if this criteria is extra credit
			if criteria[0][0] == '+':
				prompt = "[EXTRA CREDIT] " + prompt

			#check if student follows criteria
			response = input(prompt + "? ")
			while response != 'y' and response != 'n':
				response = input("y or n: ")

			#deduct/add points based on answer/extra credit
			if response == 'n' and criteria[0][0] != '+':

				#subtract correct point type
				if pointType == 'L':
					studentLab -= pointValue
				else:
					studentAssignment -= pointValue

				studentTotal -= pointValue #subtract from total
				outputFile.write("-" + str(pointValue) + ": " + result)

			elif response == 'y' and criteria[0][0] == '+':

				#add correct point type
				if pointType == 'L':
					studentLab += pointValue
				else:
					studentAssignment += pointValue

				studentTotal += pointValue #add to total
				outputFile.write("+" + str(pointValue) + ": " + result)

		totalPenalty = 0 #total percentage to deduct due to penalties

		#assess penalties from the syllabus (not including late penalties)
		for penalty in DEFAULT_PENALTIES:

			#prompt for current penalty
			response = input(penalty[0] + "? ")
			while response != 'y' and response != 'n':
				response = input("y or n: ")

			#add penalty if student fails criteria
			if response == 'n':

				totalPenalty += penalty[2]
				outputFile.write("\n-" + str(penalty[2]) + "%: " + penalty[1])

		studentAssignment -= (studentAssignment * totalPenalty) #apply penalty to assignment points only
		studentTotal = studentAssignment + studentLab #recombine points to account for any penalties

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