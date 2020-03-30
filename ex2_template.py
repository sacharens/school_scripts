#----- 1 - Variables, math, printing     #                                  <editor-fold>
print('% -------------------------------------------------- 1')

x = 10 # Declaration of variable named x + assignment of a value
y = 30
y       # When run as a single line in the console, value will be "out".
        # However, when running a few lines or the whole file - must use print()
z = x + y
s = (x + y) / 3 # Notice order of arithmetic operations
print(z)
print(s)
s = s + 1 # Running order is important!
print(s)

#------------------------------------------------------------------------ </editor-fold>

#----- 2 - String length and indexes                                        <editor-fold>
print('% -------------------------------------------------- 2')

my_string1 = 'Programmer'
my_string2 = 'a machine that converts coffee into code'

# Please add these strings to form one single string we are going to work with:
# 'Programmer - a machine that converts coffee into code'
# Since we want to keep using the new string, we will define a new variable and store the string in it:


# print new string length (two ways):

# Print first letter:

#------------------------------------------------------------------------ </editor-fold>

#----- 3@ Print last letter (3 ways)                                      <editor-fold>
print('% -------------------------------------------------- 3')

#------------------------------------------------------------------------ </editor-fold>

#----- 4 - Slicing                                                        <editor-fold>
print('% -------------------------------------------------- 4')

print(my_string[28:53]) # will return indexes 28 to 52
print(my_string[28:]) # will return indexes 28 to end
print(my_string[28:53:2]) # with jumps of 2 - each second letter

#------------------------------------------------------------------------ </editor-fold>

#----- 5@ Print last 4 letters                                            <editor-fold>
print('% -------------------------------------------------- 5')


#------------------------------------------------------------------------ </editor-fold>

#----- 6@ Print new string = 'Programmer - code machine', using slicing of my_string   <editor-fold>
print('% -------------------------------------------------- 6')


#------------------------------------------------------------------------ </editor-fold>

#----- 7@ difference in length between my_string and new_string?          <editor-fold>
print('% -------------------------------------------------- 7')

#------------------------------------------------------------------------ </editor-fold>

#----- 8 - string.count(substring)                                        <editor-fold>
print('% -------------------------------------------------- 8')

my_string.count('c')
my_string.count('code')

#------------------------------------------------------------------------ </editor-fold>

#----- 9 - string.index(substring)                                        <editor-fold>
print('% -------------------------------------------------- 9')

print(my_string.index('code'))
print(my_string.index('c')) # index for the *first* 'c'!
# print(my_string.index('z')) # no z in the string - will raise an error!

index_code = my_string.index('code')
# print('code index: ' + index_code) # No! Will not work! can't concatenate string and integer.
print('code index: ' + str(index_code)) # Yes! str() turns the int into a string, then it can be concatenated to another string.

type(index_code) # This will return the type of the variable! Very useful

#------------------------------------------------------------------------ </editor-fold>

#----- 10@ print: 'The first a out of x is at index y' (replace x and y)  <editor-fold>
print('% -------------------------------------------------- 10')

num_a = my_string.count('a')
first_a = my_string.index('a')
print('The first a out of ' + str(num_a) + ' is at index ' + str(first_a))

# Check
my_string[first_a]

#------------------------------------------------------------------------ </editor-fold>

#----- 11  *new string                                                    <editor-fold>
print('% -------------------------------------------------- 11')

my_string = 'Ben Gurion University'
# print how many 'r's in my_string
#------------------------------------------------------------------------ </editor-fold>

#----- @12 print: 'The second r is x locations after the first'           <editor-fold>
print('% -------------------------------------------------- 12')


#------------------------------------------------------------------------ </editor-fold>

#----- 13 Lists                                    <editor-fold>
print('% -------------------------------------------------- 13')

my_roomies = ['Shlomia', 'Shosh', 'Anna', 3, 5]
print(my_roomies)

print(my_roomies[1])
print(my_roomies[0:2])
print(my_roomies[::2])

### First roomie's second letter?
print(my_roomies[0][1])

# same as
first_roomie = my_roomies[0]
print(first_roomie[1])

#------------------------------------------------------------------------ </editor-fold>

#----- 14 Range                                   <editor-fold>
print('% -------------------------------------------------- 14')

my_range = range(10,25)
print(my_range)
print(list(my_range)) # to turn the range object to a list of all numbers

# Can store it as a list in advance
my_range = list(range(10,25))

#------------------------------------------------------------------------ </editor-fold>

#----- 15@ Print numbers from 0 to 50 (including) that can be divided by 5 <editor-fold>
print('% -------------------------------------------------- 15')

range_5 = list(range(0,51,5))
print(range_5)

#------------------------------------------------------------------------ </editor-fold>

#----- 16@ Using 15@'s list, print only numbers that can be divided by 10      <editor-fold>
print('% -------------------------------------------------- 16')

range_10 = range_5[::2]

#------------------------------------------------------------------------ </editor-fold>

#----- 17@ Concatenate lists, without the 0 number in each list      <editor-fold>
print('% -------------------------------------------------- 17')

new_list = range_5 + range_10 # this not what we were asked. why?
print(new_list)

# Add another item to the list
new_list = new_list + [100] # not new_list + 100! Can't concatenate a list and an integer.

#------------------------------------------------------------------------ </editor-fold>