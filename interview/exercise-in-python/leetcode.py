def longestPalindrome(s):
  """
  :type s: str
  :rtype: str
  """
  ns = "#"

  for c in s:
    ns += c + "#"
    #ns = ns + c
    #ns = ns + "#"

  print ns
  lenns = len(ns)

  p = [-1] * lenns

  maxRight = -1
  pos = -1

  maxLength = -1
  maxPos = -1

  for i in range(lenns):
    l = 0
    if i > maxRight:
      for j in range(min(lenns - 1 - i, i - 0)):
        if ns[i + j + 1] == ns[i - j - 1]:
          l += 1
        else:
          break
      p[i] = l
      maxRight = i + l
      pos = i
    else:
      ii = pos - (i - pos)
      if p[ii] >= maxRight - i:
        l = maxRight - i
        for j in range(min(lenns - 1 - maxRight, i - (maxRight - i))):
          if ns[maxRight + j + 1] == ns[i - (maxRight - i) - j - 1]:
            l += 1
          else:
            break
        p[i] = l
        maxRight = i + l
        pos = i
      else:
        p[i] = p[ii]

    if l > maxLength:
      maxLength = l
      maxPos = i

  f = (maxPos - maxLength) / 2


  print s[f:f+maxLength]

def longestPalindromeSubsequenceDP(s):
  lens = len(s)
  dp = [[-1 for col in range(lens)] for row in range(lens)]

  maX = -1;

  for i in range(lens):
    dp[i][i] = 1
    max = 1

  for k in range(1, lens):
    for i in range(lens - k):
      j = i + k
      if s[i] == s[j]:
        if (i+1 > j-1):
          dp[i][j] = 2
        else:
          dp[i][j] = dp[i+1][j-1] + 2
      else:
        dp[i][j] = max(dp[i][j-1], dp[i+1][j])
      if dp[i][j] > maX:
        maX = dp[i][j]

  print maX

def longestPalindromeDP(s):
  lens = len(s)
  dp = [[-1 for col in range(lens)] for row in range(lens)]

  maX = -1;
  res = ""

  for i in range(lens):
    dp[i][i] = 1
    maX = 1
    res = s[i:i+1]

  for k in range(1, lens):
    for i in range(lens - k):
      j = i + k
      if s[i] == s[j]:
        if (i+1 > j-1):
          dp[i][j] = 2
        elif dp[i+1][j-1] == j-1 - (i+1) + 1:
          dp[i][j] = dp[i+1][j-1] + 2
        else:
          dp[i][j] = dp[i+1][j-1]
      else:
        dp[i][j] = max(dp[i][j-1], dp[i+1][j])
      if dp[i][j] > maX:
        maX = dp[i][j]
        res = s[i:j+1]

  print res

def longestPalindromeBrute(s):
  lens = len(s)

  maX = -1;
  res = ""

  for i in range(lens):
    l = 1
    for j in range(min(i, lens - 1 - i)):
      if s[i - j - 1] == s[i + j + 1]:
        l += 2
      else:
        break
    if l > maX:
      maX = l;
      res = s[i - (l - 1) / 2:i + (l - 1) / 2 + 1]

  for i in range(lens - 1):
    l = 0
    for j in range(min(i+1, lens - 1 - i)):
      if s[i - j] == s[i + j + 1]:
        l += 2
      else:
        break
    if l > maX:
      maX = l;
      res = s[i - l / 2 + 1:i + l / 2 + 1]

  print res


def convert(s, numRows):
  """
  :type s: str
  :type numRows: int
  :rtype: str
  """
  cycle = (numRows - 1) * 2
  l = len(s)
  count = l / cycle
  remain = l % cycle
  print cycle
  result = ""
  for rowNum in range(numRows):
    row = ""
    for i in range(count):
      row = row + s[i * cycle + rowNum]
      if rowNum != 0 and rowNum != numRows - 1:
        row = row + s[i * cycle + cycle - rowNum]

    if (remain - 1) >= rowNum:
      row = row + s[count * cycle + rowNum]
    if (rowNum != 0 and rowNum != numRows - 1) and (remain-1) >= cycle - rowNum:
      row = row + s[count * cycle + cycle - rowNum]
    result = result + row
  return result

if __name__ == '__main__':
  # longestPalindrome("tattarrattat")
  # longestPalindromeSubsequenceDP("bacbb")
  # longestPalindromeDP("bacbb")
  # longestPalindromeBrute("abb")
  print convert("ABC", 3)
