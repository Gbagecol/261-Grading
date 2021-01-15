Author: Tanner Lorenz

261 Grading Assistance Script
Version: 1.0

This is a basic Python script to assist with grading student code for CSCI261.
It is geared specifically towards 261, but could probably be generalized to any
other class if you feel inclined to use it as such. Feel free to modify this
script however you want. I take no responsibility for anything that goes wrong
if you use or change this code.


USAGE
--------------------

This script is best run from a command line interface using Python 3. Simply
run the script like you would a normal .py file. The script takes two
arguments:

gradingScript.py path/to/rubric/file path/to/grades/file

The first argument is the path to a special rubric.txt file for the assignment
you are currently grading. This file contains the criteria for the current
assignment. The contents of this file are described in the next section. But
if you don't want to construct your own rubric file, I will email a rubric file
to everyone whenever a new assignment is ready to be graded. The second argument
is an output file where each student's grade will be written.

When the script is launched, it will first ask for the name of the student you
are currently grading. After you enter a name, the script will go through all
of the criteria in the rubric and ask you if the student correctly followed
them. For each requirement, just answer yes (y) if the student got the points,
and no (n) otherwise. When you have gone through the entire rubric, the script
will ask if you want to grade another student. Enter y to continue grading and
n to stop.

When you have finished grading, you can open the output file you provided to
see the grades. Each student will have listed their grade for the assignment,
a list of rubric criteria they got wrong, and any notes you wrote about that
student. The list of points missed is written in a format such that you can
easily copy and paste them into a Canvas comment along with their assignment
grade. This list will also include any extra credit points earned.


RUBRIC FILE
--------------------

If for some reason you don't want to use the rubric files I send, you can create
your own rubric file using the criteria from the instructor's rubric sent via
email. The rubric file must be formatted as follows:

Line 1 is the total points that can be earned for the assignment, usually 30.
This total does not include possible extra credit, which the script will take
into account. Line 2 is the amount of points corresponding to lab submissions.
Each lab is worth 4 points, so normally this number will be between 8 and 16.
Line 3 is the amount of points corresponding to the actual assignment criteria,
which will always be the total number of points minus the total number of lab
points.

Each line from line 4 onward corresponds to a single criteria from the rubric
and must be formatted as:

point value:point type:criteria prompt:criteria description

Point value is the amount of points a single criteria from the rubric is worth.
For normal requirements this is just the point value, like 0.5 or 2. For
criteria that are extra credit, the format is the same, except that a + should
be added to the point value (+2 instead of just 2).

Point type indicates if the criteria is for lab points or for assignment points.
This will be a single character, 'L' if the criteria pertains to a lab, and 'A'
if it pertains to the actual assignment.This is necessary since the syllabus
penalties, like compiler error or missing files, only apply to the actual
assignment and not the labs.

The criteria prompt is the question the script will ask you when determining if
a student correctly meets that specific requirement; for example, "Student
follows style guide?". A question mark is automatically appended by the script,
so there is no need to put one in the file.

The criteria description is the brief note that will appear in the output file
when the student loses points for that requirement; for example, "Code does
not follow style guide". In the output file, each missed requirement by the
student will appear as the amount of points they lost followed by this
criteria description explaining why they lost those points. For an EXTRA CREDIT
requirement, this description will instead appear only if the student DID meet
the requirement (in other words, if you answered 'y' to the prompt).

All three parts of the line must be separated by colons (chosen because I often
use commas in my prompts and descriptions). This is easily modifiable in the
script if you wish to do so.

Here is a sample of what a rubric file may look like:

30
4
26
+2:L:Did L1C extra credit:L1C extra credit
4:L:Has L1C:Did not finish L1C
12:A:Completed first half of assignment:Did not complete first half of assignment
12:A:Completed second half of assignment:Did not complete second half of assignment
2:A:Made funny joke:Did not make a funny joke

Here is an example of what the output for a single student might look like when
you are done grading them:

Test Student

+2.0: L1C extra credit
-12.0: Did not complete second half of assignment
-2.0: did not make a funny joke

Notes: Joke was awful, please kick student out of Mines


Total: 18.0
---------------------------------------------------------------------

You can view the files in the test directory for more examples.


SFML
--------------------

If you are like me and prefer to make things as hard as possible for yourself,
you can compile SFML code manually from the command line or with something like
VSCode. I ripped the following g++ commands from a valid compilation using
Eclipse, so I think they should work, but I haven't actually tested it yet.

To compile any cpp file into an object file (including main.cpp):

g++ "-I<directory containing SFML library>\\SFML-2.5.1\\include" -c filename.cpp -o filename.o

Then to compile all of those object files into an executable:

g++ "-L<directory containing SFML library>\\SFML-2.5.1\\lib" -lsfml-graphics -lsfml-window -lsfml-system *.o -o program_name


CHANGELOG
--------------------

Version 1.0 (1/10/20)
    - Added ability to apply percentage penalties from the syllabus (Compiler
      error, missing/extraneous files)