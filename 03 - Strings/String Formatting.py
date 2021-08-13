def print_formatted(number):
    w = len(str(bin(number)).replace('0b',''))
    for i in range(number):
        ans = print("{} {} {} {}".format(str(i+1).rjust(w, ' '), oct(i+1).lstrip('0o').rjust(w, ' '), hex(i+1).lstrip('0x').upper().rjust(w, ' '), bin(i+1).lstrip('0b').rjust(w, ' ')))