


# constant variables
MAX_SECTORS = 40
SECTOR_SIZE = 500

# initialize sectors
sectors = ['A', 'B', 'B', 'D', 'X', 'X', 'E', 'F', 'G', 'H', 'H', 'J', 'J', 'J', 'K', 'K', 'J', 'L', 'L', 'L', 'M', 'M', 'P', 'P', 'M', 'P', 'P', 'R', '', '', '', '', '', '', '', '', '', '']

# helper function to print sectors
def print_sectors():
    for i in range(0, MAX_SECTORS, 5):
        print('{:3}-{:3}: {}'.format(i, i+4, sectors[i:i+5]))

# display welcome message and BEFORE picture
print('Welcome to the hard drive defragmenter.')
print('BEFORE:')
print_sectors()

# perform defragmentation
for i in range(MAX_SECTORS):
    if not sectors[i]:
        for j in range(i+1, MAX_SECTORS):
            if sectors[j]:
                sectors[i], sectors[j] = sectors[j], sectors[i]
                break

# display AFTER picture
print('AFTER:')
print_sectors()
