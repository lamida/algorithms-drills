def isBalanced(s):
    def mmatch(start: str, end: str) -> bool:
        return (start == "(" and end == ")") or (start == "[" and end == "]") or (start == "{" and end == "}")

    st = []
    start = "{[("
    for b in s:
        if b in start:
            st.append(b)
        else:
            if len(st) == 0:
                return False
            last = st.pop()
            if not mmatch(last, b):
                return False
    return len(st) == 0


def printString(string):
  print('[\"', string, '\"]', sep='', end='')


test_case_number = 1


def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1


if __name__ == "__main__":
  s1 = "{[(])}"
  expected_1 = False
  output_1 = isBalanced(s1)
  check(expected_1, output_1)

  s2 = "{{[[(())]]}}"
  expected_2 = True
  output_2 = isBalanced(s2)
  check(expected_2, output_2)

  # Add your own test cases here
