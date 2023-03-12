# Defragment-a-Hard-Drive
Simulate defragmenting a hard drive.  This is a maintenance operation the OS  performs. Move sectors around so all sectors of a file are contiguous
CmpSc472, Lab
Defragment a hard drive.
Simulate defragmenting a hard drive. This is a maintenance operation the OS
performs.
Move sectors around so all sectors of a file are contiguous.
1. This lab can be written in Java, Python, or “C”.
a. If written in “C”, for simplicity, make all file names one character.
b. If writing in Python or Java, the fiels names can be string up to 8
characters.
2. Create an array to simulate sectors on a storage device.
3. The sectors will be initialized with pieces of files, listed in the diagram below.
4. In this lab, move all file pieces together so all sectors, for the files, are
contiguous.
5. Some constant variables suggested.
a. int MAX_SECTORS = 40; The number of sectors cannot change.
b. char sectors[MAX_SECTORS];
c. Const int SECTOR_SIZE = 500;
6. To start the program . . .
a. Display a message welcoming the user and a brief description what this program
will do.
b. Display the BEFORE picture of all the arrays segments. Make this look neat and
easy to follow.
c. Do the defragmentation process.
d. Finally, display an AFTER picture of the defragmented parts. Print out of all the
sectors.
Initialize the 40 sectors to look like this.
