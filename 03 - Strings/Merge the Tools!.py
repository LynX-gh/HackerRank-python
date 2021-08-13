def merge_the_tools(string, k):
    x = 0
    y = k
    print_order = []
    while y <= len(string):
        st = string[x : y]
        pr = ''
        for ch in st:
            if ch not in pr:
                pr += ch
        print_order.append(pr)
        x += k
        y += k
    for a in print_order:
        print(a)