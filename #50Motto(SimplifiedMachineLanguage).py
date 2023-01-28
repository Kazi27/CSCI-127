#Name: Kazi Sameen Anwar
#Email: kazisameen.anwar39@myhunter.cuny.edu
#Date: October 14, 2021
#This program shows winning percentage

# Store 'MIPS is cool!' at the top of the stack
ADDI $sp, $sp, -20
ADDI $t0, $zero, 77 # M
SB $t0, 0($sp)
ADDI $t0, $zero, 73 # I
SB $t0, 1($sp)
ADDI $t0, $zero, 80 # P
SB $t0, 2($sp)
ADDI $t0, $zero, 83 # S
SB $t0, 3($sp)
ADDI $t0, $zero, 32 # (space)
SB $t0, 4($sp)
ADDI $t0, $zero, 105 # i
SB $t0, 5($sp)
ADDI $t0, $zero, 115 # s
SB $t0, 6($sp)
ADDI $t0, $zero, 32 # (space)
SB $t0, 7($sp)
ADDI $t0, $zero, 99 # c
SB $t0, 8($sp)
ADDI $t0, $zero, 111 # o
SB $t0, 9($sp)
ADDI $t0, $zero, 111 # o
SB $t0, 10($sp)
ADDI $t0, $zero, 108 # l
SB $t0, 11($sp)
ADDI $t0, $zero, 33 # (!)
SB $t0, 12($sp)

ADDI $t0, $zero, 0 # (null)
SB $t0, 12($sp)

ADDI $v0, $zero, 4 # 4 is for print string
ADDI $a0, $sp, 0
syscall 			# print to the log
