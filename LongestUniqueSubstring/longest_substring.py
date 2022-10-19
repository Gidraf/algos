

def find_longest_substring_without_repeating_characters(string):
    result = ""
    result_string = ""
    result_len = 0
    for s in string:
        if s in result:
            result = result[result.index(s)+1:]
        result = f"{result}{s}"
        if(len(result)> result_len):
            result_len = len(result)
            result_string = result
    print(result_string)
    return result_len

test = "GEEKSFORGEEKS"

result  = find_longest_substring_without_repeating_characters(test)
print(result)