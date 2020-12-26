import sys


#verify args
if len(sys.argv) != 3:
	print("Please provide only an input file and an output file.")
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

			#check if student follows criteria
			response = input(prompt + "? ")
			while response != 'y' and response != 'n':
				response = input("y or n: ")

			#if not, deduct points
			if response == 'n':
				studentTotal -= pointValue
				outputFile.write("-" + str(pointValue) + ": " + result)

		#prompt for any extra notes
		notes = input("Notes: ")
		if notes != "":
			outputFile.write("\n\nNotes: " + notes + "\n")

		outputFile.write("\n\nTotal: " + str(studentTotal) + "\n---------------------------------------------------------------------\n\n")

	#ask to grade another student
	nextStudent = input("Grade another student? ")
	while nextStudent != 'y' and nextStudent != 'n':
		nextStudent = input("y or n: ")

	if nextStudent == 'n':
		break