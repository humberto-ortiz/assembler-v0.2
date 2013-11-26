---------------------------------------------------------------------------------
| Author: Jhensen Grullon Sanabria						
| Program: Assembler								
| Purpose: The purpose of this program is to translate MIPS assembly instructions	
|		   to machine language represented in hexadecimal.					
---------------------------------------------------------------------------------

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
1) Description:											
	This program is a basic assembler for the mips instructions. The instructions
	are	translated to hex according to the specifications of the CPU tdesigned 
	in class. 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
2) How to use:											
	A) Open the command line on a UNIX system.						
	B) Find the directory where you have the program.					
	C) Type python <program_name.py> <file_with_assembly.txt>									
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
3) Instructions Format:										
												
	The program only read the instructions, do not send as parameter a complete 
	program, for example the data types (.data) at the beggining of each mips code.

	A) Labels, labels should be in a single line. Example:

		inst1
		inst2
		label: 
		.
		.
		.
		instn

	B) R-format, R-format instructions should look like this:
		
		"op rd rs rt"
		add $2, $3, $2 

		lw  #3, $5, $6 
	
	C) I-format

		addi $2, $3, $5
		bnz $2, loop 

		For the jump instrucion:
			j loop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is an example code fibo for:

 #Compute 10 elements of fibonacci sequence
 # Copyright 2011, 2013 - Humberto Ortiz-Zuazaga <humberto.ortiz@upr.edu>
# Released under the GNU General Public Licence v3 or later
# See http://www.gnu.org/licenses/gpl.html
 
# Uses the 16-bit assembly we made up for our less broken cpu.
# http://www.hpcf.upr.edu/~humberto/courses/arch2013/less-broken-cpu.html
 
	add $1, $0, $0 # $1 is base
	add $2, $0, $0 
	addi $2, 9     # $2 is end
	add $3, $0 ,$0 # $3 is offset
	addi $3, -2
 
	add $4, $0, $0 # $4 is a
	addi $4, 1
	sw $4, $1, $0
	
	addi $1, 1
	sw $4, $1, $0
 
loop:	
	addi $1, 1
	lw $4, $1, $3
 
	addi $3, 1
	lw $5, $1, $3
 
	add $6, $4, $5
	sw $6, $1, $0
 
	addi $3, -1
 
	add $7, $1, $0
	addi $7, -9
	bnz $7, -9


Output for Logisimi:

0100
0200
8209
0300
83fe
0400
8401
3410
8101
3410
8101
2413
8301
2513
0645
3610
83ff
0710
87f7
b7f7

