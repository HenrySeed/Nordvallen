letters = {}
lines = open("./alphabet", 'r').readlines()
alpha = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')

chars_below_line = "ygpq"

line_count = 0
this_char = []
for line in lines:
    this_char.append( line.replace("\n", ""))

    if line_count == 5:
        max_width = 0
        for line in this_char:
            if len(line) > max_width: max_width = len(line)
        
        line_index2 = 0
        for line in this_char:
            if len(line) < max_width:
                this_char[line_index2] += " " * (max_width - len(line))

            line_index2 += 1

        if alpha[len(letters.keys())] in chars_below_line:
            this_char = [" " * max_width] * 2  + this_char

        letters[alpha[len(letters.keys())]] = this_char
        this_char = []
        line_count = 0
    else:
        line_count += 1    
        

def get_ascii(text):
    chars = []
    for char in text:
        if char in alpha:
            chars.append(letters[char])

    output = ""
    line = ""
    for line_count in range(0, 9):
        found_chars = False
        for char in chars:
            if len(char) > line_count:
                found_chars = True
                if char != chars[0]:
                    if line[-1] == " ":
                        line = line[:-1] + char[line_count][0]
                    line += char[line_count][1:]
                else:
                    line += char[line_count]
            else:
                if char != chars[0]:
                    line += (len(char[0])-1) * " "
                else:
                    line += len(char[0]) * " "

        if found_chars == False:
            break


        output += line + "\n"
        line = ""

    return output.strip("\n")

