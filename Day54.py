# Input Format

# The first line contains an integer,n, the number of students who have subscribed to the English newspaper.
# The second line contains"n"space separated roll numbers of those students.
# The third line contains ,b  the number of students who have subscribed to the French newspaper.
# The fourth line contains b space separated roll numbers of those students.

#Output Format
# Output the total number of students who have at least one subscription.

# Sample Input
# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8

# Sample Output

# 13

eng_news=int(input())
eng_news_students=list(map(int,input().split(" ")))
fr_news=int(input())
fr_news_students=list(map(int,input().split(" ")))
ans= list(set(eng_news_students)| set(fr_news_students))
print(len(ans))
