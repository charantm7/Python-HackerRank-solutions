def find_sub_string(string, sub_string):

    count = sum(1 for i in range(len(string)) if string.startswith(sub_string, i))

    return count

if __name__ == '__main__':


    string = input('String:').strip()
    sub_string = input('Sub String: ').strip()
    
    count = find_sub_string(string, sub_string)
    print(count)