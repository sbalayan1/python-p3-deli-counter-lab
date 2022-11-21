def line(deli_line):
    if (len(deli_line) > 0):
        output = 'The line is currently:'
        for idx, name in enumerate(deli_line):
            output += f" {idx+1}. {name}"
        print(output)
    else: 
        print("The line is currently empty.")

    

def take_a_number(line, name):
    line.append(name)
    print(f"Welcome, {name}. You are number {len(line)} in line.")
    


def now_serving(line):
    if (len(line) > 0):
        print(f"Currently serving {line[0]}.")
        line.pop(0)
    else: 
        print("There is nobody waiting to be served!")