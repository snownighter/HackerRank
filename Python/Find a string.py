def count_substring(string, sub_string):
    strlen, sublen = len(string), len(sub_string)
    count = 0
    for i in range(strlen-sublen+1):
        if sub_string == string[i:i+sublen]:
            count += 1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
