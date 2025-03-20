import textwrap


def text_wrap(string, width):
    return textwrap.fill(string, width)


if __name__ == '__main__':

    string = str(input('String: ')).strip()     
    width = int(input('Width: '))

    wrap = text_wrap(string, width)
    print(wrap)