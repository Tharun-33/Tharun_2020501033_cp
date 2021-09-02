# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest 
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to 
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"

def longestcommonsubstring(s1, s2):
	m = len(s1)
	n = len(s2)

	# Create a table to store lengths of
	# longest common suffixes of substrings.
	# Note that LCSuff[i][j] contains length
	# of longest common suffix of X[0..i-1] and
	# Y[0..j-1]. The first row and first
	# column entries have no logical meaning,
	# they are used only for simplicity of program
	LCSuff = [[0 for i in range(n + 1)]
				for j in range(m + 1)]

	# To store length of the
	# longest common substring
	length = 0

	# To store the index of the cell
	# which contains the maximum value.
	# This cell's index helps in building
	# up the longest common substring
	# from right to left.
	row, col = 0, 0

	# Following steps build LCSuff[m+1][n+1]
	# in bottom up fashion.
	for i in range(m + 1):
		for j in range(n + 1):
			if i == 0 or j == 0:
				LCSuff[i][j] = 0
			elif X[i - 1] == Y[j - 1]:
				LCSuff[i][j] = LCSuff[i - 1][j - 1] + 1
				if length < LCSuff[i][j]:
					length = LCSuff[i][j]
					row = i
					col = j
			else:
				LCSuff[i][j] = 0

	# if true, then no common substring exists
	if length == 0:
		print("No Common Substring")
		return

	# allocate space for the longest
	# common substring
	resultStr = ['0'] * length

	# traverse up diagonally form the
	# (row, col) cell until LCSuff[row][col] != 0
	while LCSuff[row][col] != 0:
		length -= 1
		resultStr[length] = X[row - 1] # or Y[col-1]

		# move diagonally up to previous cell
		row -= 1
		col -= 1

	# required longest common substring
	print(''.join(resultStr))

# Driver Code
if __name__ == "__main__":
	X = "abcdef"
	Y = "abqrcdest"

	longestcommonsubstring(X, Y)
