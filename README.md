#######################################################
##Sheet for how to write the commands for .ffes-files##
#######################################################

Intructions -   4 bit
Registers   -   3 bit
Imm         -   9 bit
------------------------------------------------------------------------------------------------------
rd - destination register
rs1 = file source 1
rs2 = file source 2
imm = integer x, 0 <= x >= 511
ra1 = destination for jump1
ra2 = destination for jump2

------------------------------------------------------------------------------------------------------
Math:
    madd rd rs1/imm rs2/imm     |   Add rs1/imm and rs2/imm and puts it in rd
    
    msub rd rs1/imm rs2/imm     |   Subtract rs1/imm and rs2/imm and puts it in rd
------------------------------------------------------------------------------------------------------
Jump:
    jjt1                    |   Jump to ra1
    
    jjt2                    |   Jump to ra2
------------------------------------------------------------------------------------------------------
Logic:
    lgrt x rs1 imm          |   If rs1 > imm do x
    
    llst x rs1 imm          |   If rs1 < imm do x
    
    leql x rs1 imm          |   If rs1 = imm do x
------------------------------------------------------------------------------------------------------
Special:
    sprt rs1                |   Print stored element
    
    semp rs1                |   Clear stored element
    
    scpy rd rs1             |   Copy element from rs1 to rd
    
    sbrk                    |   Quit the program
    
------------------------------------------------------------------------------------------------------

