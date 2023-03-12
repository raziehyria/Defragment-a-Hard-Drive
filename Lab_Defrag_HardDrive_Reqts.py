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
*H'''
from tabulate import tabulate

#constant variables
MAX_SECTORS = 40 
SECTOR_SIZE = 500

#initialize de-fragmented sectors
sectors = ['A', 'B', 'B', '', 'D', '', 'X', 'X', '', 'E', 'F', 'G', '', 'H', 'H', 'J', 'J', '', '', '',
'J', 'K', 'K', 'J', 'L', 'L', 'L', '', 'M', 'M', 'P', 'P', 'M', 'P', 'P', '', '', 'R', '', ''] 

#Display a message welcoming the user and a brief description what this program will do.
print("Welcome to the sector de-fragmentation program.")
print("This program will move all file pieces together so that all sectors for the files are contiguous.\n")

#Display the BEFORE picture of all the arrays segments. Make this look neat and easy to follow.
print("BEFORE defragmentation:")
print("0                                                                               19")
before_table = [sectors[i:i+20] for i in range(0, len(sectors), 20)]
print(tabulate(before_table, tablefmt='grid'))
print("20                                                                              39")

#Do the de-fragmentation process (on the ' ' spaces).
next_empty_sector = sectors.index('')
for i in range(next_empty_sector, MAX_SECTORS):
    if sectors[i] != '':
        sectors[next_empty_sector], sectors[i] = sectors[i], sectors[next_empty_sector]
        next_empty_sector = sectors.index('', next_empty_sector + 1)
    else:
        continue

#Display an AFTER picture of the de-fragmented parts. Print out all the sectors.
print("AFTER DEFRAGMENTATION:")
print("0                                                                               19")
after_table = [sectors[i:i+20] for i in range(0, len(sectors), 20)]
print(tabulate(after_table, tablefmt='grid'))
print("20                                                                              39")