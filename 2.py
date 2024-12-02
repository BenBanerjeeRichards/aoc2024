
def main():
    lines = open("inputs/2.txt").readlines()
    report = [[int(l) for l in line.split()] for line in lines]
    
    def safe(levels: list[int]) -> bool:
        diffs = [a - b for (a, b) in zip(levels, levels[1:])]
        if len(set([-1 if diff < 0 else 1 for diff in diffs])) > 1:
            return False
        if 0 in diffs:
            return False 
        abs_diffs = [abs(x) for x in diffs]
        if max(abs_diffs) > 3:
            return False
        return True
    
    unsafe_levels = [level for level in report if not safe(level)]
    part_1 =  len(report) - len(unsafe_levels)
    print("Part 1: ", part_1)
    
    made_safe = 0
    for unsafe in unsafe_levels:
        perms = [unsafe[0:x] + unsafe[x+1:] for x in range(len(unsafe))]
        if any([safe(x) for x in perms]):
            made_safe += 1
    
    print("Part 2: ", part_1 + made_safe)
    
if __name__=="__main__":
    main()
    