# Problem 1: String Split and Join
# HackerRank: https://www.hackerrank.com/challenges/python-string-split-and-join/problem

# Your accepted HackerRank code here
def split_and_join(line):
    # write your code here
    line = line.split()
    line  = "-".join(line)
    return line
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
