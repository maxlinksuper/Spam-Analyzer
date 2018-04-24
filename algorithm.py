import re
import sys
import os
import json

'''
MAIN FUNCTION
'''
def kmp(list_of_posts, keywords):
    # Status that hold the string is spam or not
    list_of_status = {}

    index = 0
    for string in list_of_posts:
        # Append the result based on spam or not
        if (search_kmp(string.lower(), keywords.lower())):
            list_of_status[index] = True
        else:
            list_of_status[index] = False
        index += 1

    return list_of_status


def regular_expression(list_of_posts, keywords):
    # Status that hold the string is spam or not
    list_of_status = {}

    # Split the pattern to each character to insert .*
    pat_split = list(keywords.lower())
    pattern = ""

    # Generate pattern from keyword inserting .* to each char
    for i in range(len(pat_split)):
        pattern += (".*" + pat_split[i])
    pattern += ".*"

    # Compile pattern into regex pattern
    regex = re.compile(pattern)
    
    index = 0
    for string in list_of_posts:
        # Append the result based on spam or not
        if (regex.match(string.lower())):
            list_of_status[index] = True
        else:       
            list_of_status[index] = False
        index += 1
        
    return list_of_status

def boyer_moore(list_of_posts, keywords):
    # Status that hold the string is spam or not
    list_of_status = {}

    index = 0
    for string in list_of_posts:
        # Set string and keywords to lower case
        bm = search_occurence(string.lower(), keywords.lower())

        # Append the result based on spam or not
        if (bm != -1):
            list_of_status[index].append(True)
        else:
            list_of_status[index].append(False)
        index += 1

    return list_of_status

'''
HELPER FUNCTION
'''

def search_kmp(text, word):
    # Create index table
    idx_table = []
    idx_table.append(0)
    j = 0
    cont = False
    
    # Searching word while appending to index table
    for i in range(1, len(word) - 1):
        if (word[i] == word[j]):
            j += 1
            cont = True
        else:
            cont = False
        if (not(cont)):
            j = 0
        idx_table.append(j)

    idx = 0
    found = False
    j = 0

    # Iterate until finding matching or at the end of text
    while (idx < len(text) and not found):
            if (text[idx] == word[j]):
                j += 1
                if (j == len(word)):
                    found = True
            else:
                if (j > 0):
                    j = idx_table[j-1]
                    idx -= 1
            idx += 1
        
    return found

def generate_last_occurence(string, size):
    # Set all number of chars to be -1
    last = [-1] * 128
 
    # Fill the actual value of last occurence
    for i in range(size):
        last[ord(string[i])] = i
 
 	# Return last occurence list
    return last
 
def search_occurence(text, pattern):
	# Store the pattern and text length
    pat_length = len(pattern)
    txt_length = len(text)
 
    # Create the last character list
    last = generate_last_occurence(pattern, pat_length) 
 
    shifted = 0	
    while (shifted <= txt_length - pat_length):
    	# Last idx for backward iteration
        j = pat_length - 1
 
 		# Keep reducing j while text still matched pattern
        while (j >= 0 and pattern[j] == text[shifted + j]):
            j -= 1
 
        # Get the matching between pattern and text
        if j < 0:
            return shifted

        else:
            # Shift depend on it's availability in list
            shifted += max(1, j - last[ord(text[shifted + j])])

    # Return -1 when didn't find any match
    return -1

if __name__ == '__main__':

    with open("post.json") as f:
        list_of_posts = json.loads(f.read())
    f.close()

    with open("command.txt") as fc:
        command = fc.readline()
    fc.close()

    with open("keyword.txt") as fk:
        keyword = fk.readline()
    fk.close()

    if (command == "bm"):
        json_out = kmp(list_of_posts, keyword)
        print(json.JSONEncoder().encode(json_out))
    elif (command == "regex"):
        json_out = regular_expression(list_of_posts, keyword)
        print(json.JSONEncoder().encode(json_out))
    else:
        json_out = kmp(list_of_posts, keyword)
        print(json.JSONEncoder().encode(json_out))