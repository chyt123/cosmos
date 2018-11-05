def isValid(s):
  """
  :type s: str
  :rtype: bool
  """

  stack = []

  for ch in s:
    if ch == '(':
      stack.append(ch)
    elif ch == '{':
      stack.append(ch)
    elif ch == '[':
      stack.append(ch)
    elif ch == ')':
      if len(stack) == 0:
        return False
      if not stack.pop() == '(':
        return False
    elif ch == '}':
      if len(stack) == 0:
        return False
      if not stack.pop() == '{':
        return False
    elif ch == ']':
      if len(stack) == 0:
        return False
      if not stack.pop() == '[':
        return False

  if len(stack) > 0:
    return False
  return True


def isValid2(s):
  """
  :type s: str
  :rtype: bool
  """
  stack = []
  for i in s:
    if i in ["(", "{", "["]:
      stack.append(i)
    else:
      if not stack or stack.pop() + i not in ["()", "[]", "{}"]:
        return False
  return len(stack) == 0

if __name__ == '__main__':
  print isValid2("()")
