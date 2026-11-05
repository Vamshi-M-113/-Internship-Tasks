# Problem 6: Find the Runner-Up Score!
# HackerRank: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    winner = float('-inf')
    runner = float('-inf')
    for i in arr:
        if i > winner:
            runner = winner
            winner = i
        elif i != winner and i > runner:
            runner = i
print(runner)               
