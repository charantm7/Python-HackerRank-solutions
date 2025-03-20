def capitalize(string):

    word = string.split(' ')

    result =[]

    for w in word:
        if w:
            result.append( w[0].upper()+w[1:] if w[0].isalpha() else w)

        else:
            result.append('')

    return ' '.join(result)

if __name__ == '__main__':
    string = input('String:')
    capitalize_check = capitalize(string)
    print(capitalize_check)