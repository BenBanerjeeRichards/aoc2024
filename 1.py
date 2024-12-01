def main():
    l1: list[int] = []
    l2: list[int] = []
    for line in open("inputs/1.txt").readlines():
        parts = line.split("   ")
        l1.append(int(parts[0]))
        l2.append(int(parts[1]))
    
    # Part 1
    pairs = zip(sorted(l1), sorted(l2))
    part_1 = sum([abs(a - b) for (a, b) in pairs])
    print("Part 1: ", part_1)
    
    # Part 2
    l2_counts = {}
    for x in l2:
        if x not in l2_counts:
            l2_counts[x] = 0
        l2_counts[x] += 1
    part_2 = sum([x * l2_counts.get(x, 0) for x in l1])
    print("Part 2: ", part_2)
    
    
    
if __name__ == "__main__":
    main()