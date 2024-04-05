def max_split_balanced_strings(s):
    count = 0
    balanced_strings = []
    current_substring = ''
    
    for char in s:
        current_substring += char  
        if char == 'L':
            count += 1
        else:
            count -= 1
            
        if count == 0:
            balanced_strings.append(current_substring)
            current_substring = ''  
    
    print(len(balanced_strings))
    for substring in balanced_strings:
        print(substring)

if __name__ == "__main__":
    s = input().strip() 
    max_split_balanced_strings(s)
