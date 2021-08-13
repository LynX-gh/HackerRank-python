# Complete the solve function below.
def solve(s):
    names = s.split(' ')
    name = ' '.join(t.capitalize() for t in names)
    return name