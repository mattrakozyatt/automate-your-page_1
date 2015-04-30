def generate_concept_HTML(concept_title, concept_notes): #function to create HTML of the current concept
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-notes">
        ''' + concept_notes
    html_text_3 = '''
    </div>
</div>'''
    
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def get_title(concept): #function to get the title inputs
    start_location = concept.find('TITLE:')
    end_location = concept.find('NOTES:')
    title = concept[start_location+6 : end_location-1]
    return title

def get_notes(concept): #function to get the notes inputs
    start_location = concept.find('NOTES:')
    notes = concept[start_location+6:]
    return notes

def get_concept_by_number(text, concept_number):
    counter = 0
    while counter < concept_number:
        counter = counter + 1 #increment the counter for loop control
        next_concept_start = text.find('TITLE:') #position of the the string 'TITLE:'
        next_concept_end = text.find('TITLE:', next_concept_start + 1) #position of the next string 'TITLE:'
        if next_concept_end >= 0: # -1 check for result of next_concept_start evaluation
            concept = text[next_concept_start:next_concept_end] #assigns the body of title&notes to variable 'concept'
        else:
            next_concept_end = len(text)
            concept = text[next_concept_start:] 
        text = text[next_concept_end:] #removes the current concept from the variable 'text'
    return concept

TEST_TEXT = """
TITLE:Programming is the core of computer science.
NOTES:
A computer is a universal machine.
When we program computers, the computer needs to interpret that program. We want to make sure that the computer interprets the program the exact same way that programmer intends for it to be interpreted.
TITLE:Interesting facts
NOTES:
Light travels approximately 29 centimeters in one nanosecond (1/1billionth).
Modern computer processors run at speeds in the billionths of cycles per second.
Speed of light is 299,792,458 meters per second.
TITLE:Python
NOTES:
Python is a widely used general-purpose, high-level programming language.  Its design philosophy emphasizes code readability.
TITLE:Python components
NOTES:
String - A string is a sequence of characters encapsulated by quotes.
Variable - Variables are assigned values using the '=' operator, which is not to be confused with the '==' sign used for testing equality.
Variables can also vary...
In Python "=" means assignment.
"#" at the beginning of a line of text will exclude the line from the operable code.  This is used for adding notes within the code.
TITLE:Assignments in Python
NOTES:
Syntax: 	&lt;name&gt; = &lt;expression&gt;
Example:	speed_of_light = 2997924588
TITLE:print
NOTES:
Prints expressions or variables.  When using print with a string, you can combine, or concatenate, segments of text with the "+" sign.
	Example: 	print 'Hello' + ' world!' &lt;-- will print: Hello world!
You cannot combine numbers with strings.
	Example:	print 'hello' + 13 &lt;-- This will result in an error
It is possible to multiply strings.
	Example:	print 'hello ' * 3 &lt;-- will print: hello hello hello

TITLE:String indexing
NOTES:
String indexing evaluates the characters of a string.
	Example: 'udacity'[3] - produces the result 3 (fourth character in the string, counting from 0)
Index numbering starts with 0.
Indexing also works on variables.
	Example:	name = "Matthew"
			print name[4] &lt;-- will print "h"
When using negative numbers in the indexing evaluation, the character count starts from the end of the string starting with -1.
	Example: 	"pomade"[-1] &lt;-- result with "e"

TITLE:Selecting subsequences of strings
NOTES:
	Syntax: 	&lt;string&gt;[&lt;start expression&gt;:&lt;stop expression&gt;]
The first expression in the evaluation is the starting position, and the second expression is the stop.  The result will be a string that is a subsequence of the characters in the string, starting from the start position, and ending at the stop position -1.
	Example:	name = 'awesome'
			print name[2:5] &lt;-- will print 'eso'

Selecting a subsequence without a 'stop' value will result with an evaluation with all characters starting at the 'start' character, and will include all remaining characters through the end of the string.
	Example:	statement = "OK, let's begin"
			print statement[10:] &lt;-- will print "begin"

When selecting a subsequence without a 'start' value will result with an evaluation with all characters from the beginning of the string, and ending at the 'stop' position -1.
	Example: 	name = "Harkness"
			print name[:5] &lt;-- will print "Harkn"

TITLE:Finding strings within strings using .find
NOTES:
	Syntax: 	&lt;string&gt;.find(&lt;string to find&gt;)
Results in a number that gives the position in the searched string, of the first character of the string that is being sought.
** If the sought string is not found, the result is -1.
	Example:	name = 'hello'
			print name.find('ll') &lt;-- will print the result '2'

TITLE:Finding strings with a starting position
NOTES:
	Syntax:	&lt;string&gt;.find(&lt;string&gt;,&lt;expression&gt;)
The expression will give the start position in the searched string, where the target string appears at, or after, the start position.
	Example:	name = "Okay, Okay, Okay"
			print name.find('O',3) &lt;-- will print the result '6'
TITLE:Functions
NOTES:
Also called procedures.  A series of statements which returns some value to a caller. It can also be passed zero or more arguments which may be used in the execution of the body.
	Syntax:	def &lt;function&gt;(&lt;input&gt;,&lt;input&gt;,&lt;input&gt;....):
				&lt;operation&gt;
Inputs are also called 'operands' and 'arguments'.
	Example:	def rest_of_string(string):
				return string[1:]
			print rest_of_string('audacity') &lt;-- will print 'udacity'
When a function is called, the execution jumps to the function.  It assigns the parameters, or the values passed as input.  In the body of the procedure, the input(s) are acted upon by the operation.  Using 'return' in the operation, tells the function to return the results to where the function was called.
TITLE:Control Flows and Loops: if and while
NOTES:
if - controls which code gets executed when
	Syntax:	if &lt;test expression&gt;:
				&lt;block&gt;
	Example:	def bigger(a,b):
				If a &gt; b:
					return a
				return b
'else' after an 'if' will execute the &lt;block&gt; under 'else' when the 'if' statement is False.
	Example:	def bigger(a,b):
				if a &lt; b:
					return a
				else:
					return b

while - loops code to perform the same task many times
	Syntax:	while &lt;test expression&gt;:
				&lt;block&gt;
As long as the test expression in a 'while' is True, the function will repeat.
	Example:	i = 0
			while i &lt; 10:
				print i
				i = i + 1
'break' exits the loop if conditions are True.
	Example:	i = 1
			while True:
				if I &gt; 20:
					break
				print i
				i = i + 1
TITLE:Using 'or' in 'if' statements
NOTES:
	Syntax:	&lt;expression&gt; or &lt;expression&gt; or &lt;expression&gt;...
If the first expression evaluates to True, the value is True, and the second expression is not evaluated.  If the value is False, then the next expression is tested.
TITLE:Making decisions
NOTES:
Results of comparisons are not numbers.  Results of comparisons are Boolean values: True or False.
Operators for comparison
	'&lt;' less than
	'&gt;' greater than
	'==' equal
	'!=' does not equal
TITLE:Debugging
NOTES:
If the code does not work, isolate it by commenting it out.  If you were construction your code by copying code from a known good program, replace the broken code with the good example.  This will help to identify the error.
Bugs happen to all programmers.  It is not important to avoid bugs, but it is important to know what to do when you encounter an error.
Copy code into a separate file to preserve versions.
TITLE:Debugging Strategy recap
NOTES:
1)	Examine error messages when programs crash
2)	Work from example code
3)	Make sure examples work
4)	Check(print) intermediate results
5)	Keep and compare versions of code
TITLE:Structured Data: Lists and For Loops
TITLE:Lists
NOTES:
A list is a sequence of anything.  A list can include characters, strings, numbers, and other lists.
Both lists and strings can be assigned to variables.
A string is identified by the encapsulation of characters by quotation marks(either single or double).
A list is identified by its encapsulation by brackets [].  The elements in a list are separated by commas.
Strings vs. Lists
	Example:	strings		lists
			s = 'yabba'	p = ['y','a','b','b','a']
			s[0] - 'y'		p[0] - 'y'
			s[2:4] - 'bb'	p[2:4] - ['b','b']

A string is a sequence of characters(the only thing you can put in a string is a character)

A list can be empty
	Example:	[]

A list can have one element
	Example:	[3]

A list can contain lists(called nested lists)
	Example:	['apple',3,'oranges',27[1,2['alpha','beta']]]

List mutation changes the value of the list after it is created.
	Example:	p = ['y','e','l','l','o']
			p[0] = 'H' &lt;-- changes the 'y' to an 'H' in position 0

A list can change assignment
	Example:	q = p &lt;-- assigns the list p to q
			q[4] = '!' &lt;-- This changes the value in both p and q
TITLE:List operations
NOTES:
Append - Adds a new element to a list
	Syntax:	&lt;list&gt;.append(&lt;element&gt;)
	Example:	alpha = ['A','B','C']
			alpha.append('D') &lt;-- resulting list is ['A','B','C','D']
Concatenating lists with '+'
	Example:	[0,1] + [2,3] &lt;-- resulting list is [0,1,2,3]
len - Length of object
	Syntax:	len(&lt;list or string&gt;)
	Example:	len([0,1]) &lt;-- resulting value is 2
			len(['a',['b',['c']]] &lt;-- resulting value is 2
			len('udacity') &lt;-- resulting value is 7
TITLE:For loops
NOTES:
	Syntax:	for &lt;name&gt; in &lt;list&gt;:
				&lt;block&gt;
For each element in the list, we are going to assign the element to the &lt;name&gt;, and evaluate the &lt;block&gt;.  And were are going to do this for each element in the list(in order).
	Example:	def print_all_elements(p):
				For e in p:
					print e
TITLE:Indexing lists
NOTES:
The output of index is the first position of the found value in the list.  If the &lt;value&gt; is found in the list, returns the first position where &lt;value&gt; is found in &lt;list&gt;.  Otherwise produces and error.
	Syntax:	&lt;list&gt;.index(&lt;value&gt;)
	Example:	nums=[6,7,8,9]
			print nums.index(8) &lt;-- will print the value '2'
TITLE:in
NOTES:
If &lt;value&gt; is in the list, result is True, otherwise the result is False.
	Syntax: &lt;value&gt; in &lt;list&gt;
TITLE:not in
NOTES:
If &lt;value&gt; is not in the &lt;list&gt;, result is True, otherwise the result is False.
	Syntax: &lt;value&gt; not in &lt;list&gt;
TITLE:How to Solve Problems
NOTES:
The first thing you should do to solve a problem is make sure you understand the problem.

Example of a problem: Given your birthday, and the current date, calculate your age in days.  
The input(set) of this it the first part of the problem: "birthday, and the current date".  The output is the second part of the problem statement: "age in days".

The solution to a problem is a procedure that can take any inputs in the (set), and produces output, the desired output that satisfies the relationship we want.

A problem is defined by the set of possible inputs(this is usually an infinite set for most interesting problems), and the relationship between those inputs and their desired outputs.

Solution
	Input -&gt; Procedure -&gt; output
TITLE:Pythonista's Guide to All Problems in the Galaxy
NOTES:
    1) Don't Panic!
    2) What are the inputs?
    3) What are the outputs?
    4) Solve the problem!
"""


def generate_all_html(text):
    current_concept_number = 1 #assigns the first concept number for loopong control
    concept = get_concept_by_number(text, current_concept_number) #call to the function to grab the concept 
    all_html = '' #assigns a blank variable for building the output
    while concept != '': #loop the following block while the input is not empty
        title = get_title(concept) #call to get_title function
        notes = get_notes(concept) #call to get_notes function
        concept_html = generate_concept_HTML(title, notes) #call to function that builds the HTML for currnet concept
        all_html = all_html + concept_html #concatenates the current concept to all_html
        current_concept_number = current_concept_number + 1 #increments the concept number for loop control
        concept = get_concept_by_number(text, current_concept_number) #gets the next concept title and notes
    return all_html


print generate_all_html(TEST_TEXT)
