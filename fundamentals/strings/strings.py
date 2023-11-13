# Strings could be defined in both single and double quotes it depends on the situation we find ourselves in

# Case 1 --
fullname = "Dawood Sulaimon"
# # Case 2 --
sentence = "I have enrolled on this guy's course"
# # Case 3 --
quote= 'Abraham lincoln said "To fail to prepare is to prepare to fails'


# Maintaining texts with formats it's been written could be done using tripple quotes (''' ''' or  """ """)

email_sample = '''
Hi Dawood,

Here is our first congratulatory message to you/

Thank yo,
Support team.
'''
# print(email_sample)



# ****FORMATTED STRINGS (f"")*****
# Basic Concatenation
f_name = "Sulaimon"
l_name = "Dawood"
full_name = f_name + " " + l_name + " is a python dev"
print(full_name)

# formatted string
f_full_name = f"{f_name} {l_name} is a python dev"
print(f_full_name)




# ****STRING FUNCTIONS****


# 1.)
# [] - for getting char at an index 
# [negative index] - for getting char at an index 
# from the end
#  [index-start : index-end] - getting substring starting from the index ends without including the index-end
#  [index-start : ] - getting substring starting from the index ends with default index value which is the last character for the string
#  [ : index-end ] - Same with top
#  [ : ] - Starts with the default index and ends with the default index

next_of_kin = "Dawood taoheed"
# print(next_of_kin[-2])
# print(next_of_kin[-1])
# print(next_of_kin[0:8]) 
# print(next_of_kin[0:]) 
# print(next_of_kin[:8]) 
# print(next_of_kin[:]) 


# 2.)
# len() - for getting total string lenth in int
print(len(next_of_kin))

# 3.)
# ()".") to access all methods related to strings
# - upper() - transform to uppercase
# - lower() - transform to lowercase
# - find(char or chars) - finds the first matching charater inthe string and returns it's index
# - there are many more methods

# print(next_of_kin.upper())
# print(next_of_kin.lower())
print(next_of_kin.title())