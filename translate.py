#!/usr/bin/python
#################################################################################
# Author: Jhensen Grullon Sanabria						
# Program: Assembler								
# Purpose: The purpose of this program is to translate MIPS assembly instructions	
#		   to machine language represented in hexadecimal.					
#################################################################################

from assembler import *
import os

filename=chkCMLArgs() #first, we validate the user input.
f = open(filename)

# remove the input file path and extension
outfile = os.path.splitext(os.path.basename(filename))[0]
# append .bin
outfile += ".bin"

out = open(outfile,'w') # file to save the instructions in hex. 


#we get a list of the code without lines, comments, and the '$' symbol. 
file_lines = getParsedCode(f.readlines())
f.close()

op = imm = rd = "" # this variales will hold the structure of an instruction(op code, register and immediate bits)

cnt = -1 # used to know the current line. 

# output logisim header
out.write("v2.0 raw\n")

# now we go through the code.
for line in file_lines:
	
	print line # we print the line to see the input and output instructions.
	# if there are two words, that means that the instruction is for a jump.
	if len(line) == 2:

		# The instruction jr is of length two but it is an r-format instruction.
		# We check if the instruction is jr.
		if line[0] == 'jr':
			out.write("%s%s%s\n"%(tohex(operations[line[0]]),tohex(bin(int(line[1]))),"00"))
			print "%s%s%s"%(tohex(operations[line[0]]),tohex(bin(int(line[1]))),"00")
		
		# If the instruction is not 'jr', then we are dealing with a normal J-format instruction.
		else:
			# we get the immediate value, according to the position of the label.
			# the two complement of the difference btwn the current line and the position
			# of the label because we have to go -N steps back.
			imm = twocomp(cnt-label_list[line[1]],12) 

			#we print and write into the output file, the instruction in hex. 
			print "%s%s%s%s"%(tohex(operations[line[0]].zfill(4)),tohex(imm[0:4]),tohex(imm[4:8]),tohex(imm[8:12]))	
			out.write("%s%s%s%s\n"%(tohex(operations[line[0]].zfill(4)),tohex(imm[0:4]),tohex(imm[4:8]),tohex(imm[8:12])))	

	#if there are three words, that means that the instruction is in I-format.
	elif len(line) == 3:
		
		op = operations[line[0]].zfill(4) # we get the operator value.
		rd = bin(int(line[1]))[2::].zfill(4) # we get the rd register number.
		
		#if the instructions does not start with "-".
		if line[2][0] != "-" and not line[2].isdigit():
			# we search for the label name.	
			imm = twocomp(cnt-label_list[line[2]],8)
			
		else: imm = getimm(line[2],8) #else, we get the 8 immediate number.
		
		print "%s%s%s%s"%(tohex(op),tohex(rd),tohex(imm[0:4]),tohex(imm[4:8]))
		out.write( "%s%s%s%s\n"%(tohex(op),tohex(rd),tohex(imm[0:4]),tohex(imm[4:8])))

	# if there are four words, that means that the instructions are R-format.
	elif len(line) == 4:

		# We get each part of the R-format instruction in machine language.
		op = operations[line[0]].zfill(4) # we get the operator value.
		rd = bin(int(line[1]))[2::].zfill(4) #rd number
		rs = bin(int(line[2]))[2::].zfill(4) #rs number
		rt = bin(int(line[3]))[2::].zfill(4) #rt number
		
		# Now, we print the instruction in hex and save it in the output file.
		print "%s%s%s%s" %(tohex(op),tohex(rd),tohex(rs),tohex(rt))
		out.write( "%s%s%s%s\n" %(tohex(op),tohex(rd),tohex(rs),tohex(rt)))

	cnt+=1 #we move to the next line.
	
	#**END OF FOR LOOP**

out.close() # we close the file.

print("The translated logisim bin file is in the file '%s'" % outfile)
