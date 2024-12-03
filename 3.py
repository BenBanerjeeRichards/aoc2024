import re 


def main():
    program = open("inputs/3.txt").read()
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", program)
    part_1 = sum([int(a) * int(b) for (a, b) in matches])
    print("Part 1: ", part_1)
    
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(d)o\(\)|(d)on't", program)
    active = True 
    total = 0
    for match in matches:
        if match[2]:
            active = True 
        if match[3]:
            active = False 
        if active and match[0]:
            total += int(match[0]) * int(match[1])
    print("Part 2: ", total)

            

if __name__ == "__main__":
    main()