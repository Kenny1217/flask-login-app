# utilities.py

# Function to check if stings match
def stings_match(str1, str2):
    return str1 == str2

# Function to check if string is bigger then given length
def string_match_length(str1, str_len):
    return len(str1) < str_len 

# Function to check if there is whitespaces 
def string_contains_whitespaces_or_empty(str1):
    import string
    # False is not empty and contains no spaces 
    return (any(c in str1 for c in string.whitespace) or str1 == "")