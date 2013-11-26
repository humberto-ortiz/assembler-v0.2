import string
import sys
import os.path

# Dictionary to store the name of the label and its position. 
# Example label_list = {label:position,label2:position2,label3:position3....}
label_list = dict()

# This is a dicitionary with all the operations used in 
# the 16-bit CPU and their respective op-code.
operations ={
	"add":"0000",
	"addi":"1000",
	"sub":"0001",
	"lw":"0010",
	"sw":"0011",
	"and":"0100", 
	"or":"0101",
	"not":"0110",
	"ldhi":"1001",
	"bz":"1010",
	"bnz":"1011",
	"jal":"1101", 
	"jr":"1110", 
	"j":"1111"
}

#==========================================================
# The function getParsedCode takes the assembly
# code and removes all the symbol(',','$','#') and
# returns a list with a instruction in each line.
# Parameters: The function receives a string containing the
# assembly code to be parsed.
# NOTE: This is a very basic parser.
#==========================================================

def getParsedCode(user_code):

	new_code = [] # this list will contain the parsed code.
	line_number = 0

	# we go through all the code
	for line in user_code:
		# this condition checks if the line is empty. The the result of a 
		# split over a empty string or a string containing ' \n\t' or '\n  '
		# is [].
		if line.split() == []: 
			continue

		# this is the case when the complete line is a comment, so we skip
		# the complete line. NOTE: We could put the above case toguether with
		# this one, but, the index over an empty list, returns a python exception.
		elif line.strip()[0] == '#':
			continue

		index = line.find('#') # we get the index of the '#' character(if one exists)
		# if the '#' was not found, that means we found somewhere the comment symbol
		# So, we get only the string before the '#'.
		if index != -1:
			new_code.append(line[0:index].strip().replace(',',' ').replace('$','').split())

		# Our last option, we are dealing with a line without comments.
		else:
			new_code.append(line.strip().replace(',',' ').replace('$','').split())
		
		# If the line we are reading is a label, then we add the label hash
		# the label as the index, and the its position as the value.
		if len(new_code[line_number]) == 1:

			label_list["".join(new_code[line_number])[0:-1]] = line_number
			#print '-----------\n\n%s-----------\n\n'%labe
		line_number += 1 #we update the line number.

		#**END OF FOR LOOP**

	return new_code

#==========================================================
# The function addbin, add two binary numbers. 
# Parameters: bina and binb-strings containing 
# binary numbers.
#==========================================================

def addbin(bina,binb):
	return bin(int(bina,2)+int(binb,2))[2::]

#==========================================================
# The function twocomp receives a number(b10)  
# and returns the two's complement as a string.
# Parameters, receive the number to be changed and the 
# numbe of bits for the offset.
#==========================================================

def twocomp(number,bits):
	
	number = bin(int(number))[2::].zfill(bits) # we set the number to the number of bits.
	new = "" 

	#we flip the bits.
	for i in number:
		if i == "0": new+="1"
		else: new+="0"
	
	return addbin(new,"1") #we save the sum of 1 + the inverted number.

#==========================================================
# This fuction returns the inmmediate of a number.
# Parameters: Receives a string with the number to be 
# converted and the number of bits for the offset.
#==========================================================

def getimm(number,bits): 
	if number[0] == "-": return twocomp(number[1::],bits)
	else: return bin(int(number))[2::].zfill(8)

#==========================================================
# This function receives a binary number
# as a string and return the number as		
# an hexadecimal number.
# Parameters: Receives a string with the binary number.	
#==========================================================

def tohex(binarynum):
	return ''.join(["%x"%string.atoi(bin,2) for bin in binarynum.split()])

#==========================================================
# The function chkCMLArgs is used to validate the user 
# input at the command line. The input validation is very 
# basic, we only check the parameters the user entered and
# we check if the name of the file received is a file.
# Parameters: None, we use the arguments of the system.
#==========================================================
def chkCMLArgs():
	# first, we check is the user has inserted the corret number of parameters.
	if len(sys.argv) < 2:
		print "\n\n!!ERROR: You should indicate the name of the file.!!"
		print "Usage: python <program_name.py> <filename>\n\n"
		sys.exit()

	# if the file does not exist, an error is returned to the user and the program finish.
	elif not os.path.isfile(sys.argv[1]):
		print "\n\n !!ERROR: The file %s does not exist, please check your input file.!!\n\n" %sys.argv[1]
		sys.exit()

	return sys.argv[1] # the user input is returned.