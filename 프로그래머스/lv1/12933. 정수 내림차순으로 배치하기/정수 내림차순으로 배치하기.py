def solution(n: int) -> int:
  # convert the integer to a string
  s = str(n)

  # split the string into a list of characters
  chars = list(s)

  # sort the list of characters in descending order
  chars.sort(reverse=True)

  # convert the list of characters back to a string
  s = "".join(chars)

  # convert the string back to an integer and return it
  return int(s)