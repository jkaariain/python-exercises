def pisin_jarjestetty_alimerkkijono(string):
    ret_string = ""
    prev_string = ""

    if string:
        prev_char = string[0]
        ret_string += prev_char
        prev_string += prev_char
    else:
        return ""

    for i in range(0, len(string)):
        if string[i].isalpha() and ord(string[i]) > ord(prev_char):
            if ret_string != "":
                if string[i] == ret_string[len(ret_string)-1]:
                    break
            else:
                ret_string += string[i-1]
            ret_string += string[i]
        else:
            if len(string) <= 2:
                first_char = string[0]
                if ord(first_char) > ord(string[1]):
                    return first_char
                else:
                    return string[1]
            elif len(ret_string) > len(prev_string):
                prev_string = ret_string
                ret_string = ""
                ret_string += string[i]
            elif len(ret_string) <= len(prev_string):
                ret_string = ""
        prev_char = string[i]

    if len(ret_string) > len(prev_string):
        return ret_string
    elif len(ret_string) == len(prev_string):
        return prev_string
    else:
        return prev_string

