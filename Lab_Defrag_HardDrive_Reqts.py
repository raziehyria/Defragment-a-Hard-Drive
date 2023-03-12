'''*H
* AUTHOR :   Razie Hyria        START DATE :    March 8th 2023
* FILENAME :        Defragment a hard drive
* COURSE NAME:      CMPSC 472 Section 001: Operating Systems
* SEMESTER:         SPRING 2023
*
* DESCRIPTION :
*      Simulate defragmenting a hard drive.  This is a maintenance operation the OS performs. 
*      Move sectors around so all sectors of a file are contiguous.
*
* FUNCTIONS USED: time, dictionary, queue, tabulate.
*
* 
* 
*H'''
from tabulate import tabulate
MAX_SECTORS = 40
SECTOR_SIZE = 500

sectors = ['A', 'B', 'B', '', 'D', '', 'X', 'X', '', 'E', 'F', 'G', '', 'H', 'H', 'J', 'J', '', '', '',
'J', 'K', 'K', 'J', 'L', 'L', 'L', '', 'M', 'M', 'P', 'P', 'M', 'P', 'P', '', '', 'R', '', '']

#Display a welcome message to the user and explain what the program does
print("Welcome to the sector de-fragmentation program.")
print("This program will move all file pieces together so that all sectors for the files are contiguous.\n")

#Display the BEFORE picture of all the array segments.

print("BEFORE defragmentation:")
before_table = [[i, sectors[i]] for i in range(MAX_SECTORS)]
print(tabulate(before_table, headers=["Sector", "File Piece"], tablefmt='fancy_grid', numalign="left"),"\n")

#for i in range(0, MAX_SECTORS, 10):
    #table = [" ".join(sectors[i:i+10])]
#print('\nProcesses Catalog:\n', tabulate(table, headers=header1, tablefmt="pretty"), '\n')

#Do the de-fragmentation process (on the ' ' spaces).
next_empty_sector = sectors.index('')
for i in range(next_empty_sector, MAX_SECTORS):
    if sectors[i] != '':
        sectors[next_empty_sector], sectors[i] = sectors[i], sectors[next_empty_sector]
        next_empty_sector = sectors.index('', next_empty_sector + 1)
    else:
        continue

#Display an AFTER picture of the de-fragmented parts. Print out all the sectors.
#for i in range(0, MAX_SECTORS, 10):
    #print(" ".join(sectors[i:i+10]))
print("AFTER DEFRAGMENTATION:")
after_table = [[i, sectors[i]] for i in range(MAX_SECTORS)]
print(tabulate(after_table, headers=["Sector", "File Piece"], tablefmt='fancy_grid', numalign="left"), "\n")    