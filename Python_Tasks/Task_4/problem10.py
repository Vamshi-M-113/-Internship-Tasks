# Problem 10: Find a String
# HackerRank: https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    cnt = 0
    i=0
    while i<=(len(string)-len(sub_string)):
        if string[i:i + len(sub_string)] == sub_string:
            cnt += 1
        i +=1
    return cnt
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
