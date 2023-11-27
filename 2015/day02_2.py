def parse_line(line):
    """Takes in an input line and returns three integers for the size of the box"""
    edges = line.strip().split('x')
    res = []
    for i in edges:
        res.append(int(i))

    """res = [int(i) for i in line.strip().split('x')]"""
    return res

def calculate_wrapping_paper(l, w, h):
    """takes in box dimensions and returns the sq ft of wrapping paper needed"""
    ordered_edges = sorted((l, w, h))
    extra_paper = ordered_edges[0]* ordered_edges[1]
    wrapping_paper = 2*l*w + 2*w*h + 2*h*l
    res = wrapping_paper + extra_paper
    return res

def calculate_ribbon(l, w, h):
    """takes in box dimensions and returns the length of ribbon needed"""
    ordered_edges = sorted((l, w, h))
    extra_ribbon = ordered_edges[0]* ordered_edges[1]* ordered_edges[2]
    ribbon_needed = 2*ordered_edges[0]+ 2*ordered_edges[1]
    """why did this not work: ribbon_needed = l+l+w+w """
    res = extra_ribbon+ribbon_needed
    return res

with open('2015/day02.txt') as f:
    total_paper = 0
    total_ribbon = 0
    for line in f.readlines():
        l, w, h = parse_line(line)
        paper_needed = calculate_wrapping_paper(l, w, h)
        total_paper += paper_needed
        ribbon_needed = calculate_ribbon(l, w, h)
        total_ribbon += ribbon_needed
        

    print(total_paper)
    print(total_ribbon)