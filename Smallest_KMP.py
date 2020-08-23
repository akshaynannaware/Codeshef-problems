'''. He also has another string P, called pattern. He wants to find the pattern in S, but that might be impossible. Therefore, he is willing to reorder the characters of S in such a way that P occurs in the resulting string (an anagram of S

) as a substring.

Since this problem was too hard for Chef, he decided to ask you, his genius friend, for help. Can you find the lexicographically smallest anagram of S
that contains P

as substring?

Note: A string B
is a substring of a string A if B can be obtained from A

by deleting several (possibly none or all) characters from the beginning and several (possibly none or all) characters from the end.
Input

    The first line of the input contains a single integer T

denoting the number of test cases. The description of T
test cases follows.
The first line of each test case contains a single string S
.
The second line contains a single string P

    .

Output

For each test case, print a single line containing one string ― the smallest anagram of S
that contains P

.
Constraints

    1≤T≤10

1≤|P|≤|S|≤105
S
and P
contain only lowercase English letters
there is at least one anagram of S
that contains P

Subtasks

Subtask #1 (20 points): |S|≤1,000

Subtask #2 (80 points): |S|≤105

Example Input

3
akramkeeanany
aka
supahotboy
bohoty
daehabshatorawy
badawy

Example Output

aaakaeekmnnry
abohotypsu
aabadawyehhorst
'''

test_case = int(input())

for i in range(test_case):
	S = input()
	P = input()
	dict1 = {chr(i) : 0 for i in range(97, 123)}
	for i in S:
		dict1[i] += 1
	for i in P:
		dict1[i] -= 1
	#S = sorted(S)
	#print(S)
	list1 = []
	list2 = []
	count = 0
	for i in range(97, 123):
		if(i==ord(P[0])):
			list2.append(P)
		list2.append(chr(i)*dict1[chr(i)])
		list1.append(chr(i)*dict1[chr(i)])

		if i == ord(P[0]):
			list1.append(P)
	#print('list1 :',list1)
	#print('list2 :',list2)
	list1 = ''.join(list1)
	#print(list1)
	
	list2 = ''.join(list2)
	#print(list2)
	print(min(list1,list2))
	
