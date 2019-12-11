from pprint import pprint
import os
import subprocess

def simple_search(search, items):
    simple_search = search.lower().replace(" ", "")
    best_option = None
    best_score = float("inf") # Lower is better

    for item in items:
        simple_name = item.name.lower().replace(" ", "")
        if simple_search in simple_name:
            score = len(simple_name.replace(simple_search, ""))
            if score < best_score:
                best_option = item
                best_score = score

    return best_option


def get_num_option(max_val):
    invalid_num = True
    while invalid_num:
        prompt = input("    > ")
        invalid_num = False
        
        if prompt == "q":
            return "q"

        try:
            prompt = int(prompt)
            prompt -= 1
            if prompt < 0 or prompt > max_val:
                print("Enter a number between 0 and", max_val)
                invalid_num = True
        except:
            print("Enter a number between 0 and", max_val), 
            invalid_num = True

    if not invalid_num:
        return prompt
    else:
        return False
    

def get_term_cols_rows():
    return [
        int(os.popen('stty size', 'r').read().split()[1]),
        int(os.popen('stty size', 'r').read().split()[0])
    ]

cols = int(os.popen('stty size', 'r').read().split()[1])
rows  = int(os.popen('stty size', 'r').read().split()[0])

def get_term_width():
    return int(os.popen('stty size', 'r').read().split()[1])


def print_wrap(text, width=get_term_width()):
    print("\n".join(text_wrap(text, width)))


def get_wrap(text, margin = 0):
    width = get_term_width() - margin
    return ("\n" + margin * " ").join(text_wrap(text, width))


def text_wrap(text, width=get_term_width()):
    lines = []

    line = ""
    for word in text.split(" "):
        if len(line + " " + word) > width:
            lines.append(line)
            line = ""

        while len(word) > width:
            lines.append(word[0:width-1] + "-")
            word = word[width:]

        if(line != ""):
            line += " " + word
        else:
            line += word

    lines.append(line)

    return lines


def print_table(name, rows, header=None):
    # We need to find the max size of each row
    col_maxs = [0] * len(rows[0])
    
    for row in rows:
        col_index = 0
        for col in row:
            if (len(col) + 3) > col_maxs[col_index]:
                col_maxs[col_index] = len(col) + 3
            col_index += 1

    col_maxs[0] += 1

    col_sizes = [cols // len(col_maxs)] * len(col_maxs)

    index = 0
    for col in col_maxs:
        if col < col_sizes[index]:
            col_sizes[index] = col

            remainingCols = len(col_sizes[index+1:])
            remainingDist = cols - sum(col_sizes[0:index+1])
            thisIndex = index+1
            for nextcol in col_sizes[index+1:]:
                col_sizes[thisIndex] = remainingDist // remainingCols
                thisIndex += 1
        
        index += 1

    if sum(col_sizes) < cols:
        col_sizes[len(col_sizes)-1] += cols - sum(col_sizes)

    for row in rows:
        row_str = "|"
        
        col_index = 0
        newRow = []
        for col in row:
            newRow.append(text_wrap(col, col_sizes[col_index]))
            col_index += 1
        
        maxColROws = 0
        for col in newRow:
            if len(col) > maxColROws:
                maxColROws = len(col)


        colRowString = "|"
        for colRow in range(0, maxColROws):

            colVal = ""
            if(len(col) >= colRow):
                colVal = col[colRow]

            col_index = 0
            for col in newRow:
                colWidth = col_sizes[col_index]
                colRowString += " {0:{1}} |".format(colVal, colWidth)
                col_index += 1
            colRowString += "\n"


        print(row_str)
