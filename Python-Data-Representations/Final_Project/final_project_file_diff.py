"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """

    if len(line1) == len(line2):
        for idx in range(len(line1)):
            if line1[idx] != line2[idx]:
                return idx
    elif len(line1) > len(line2):
        for idx in range(len(line2)):
            if line2[idx] != line1[idx]:
                return idx
        return len(line2)
    else:
        for idx in range(len(line1)):
            if line1[idx] != line2[idx]:
                return idx
        return len(line1)

    return IDENTICAL


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if "\n" in line1 or "\r" in line1 or "\n" in line2 or "\r" in line2:
        return ""
    elif idx < 0 or idx > min(len(line1), len(line2)):
        return ""
    else:      
        diff = idx * "=" + "^"
        return '{0}\n{1}\n{2}\n'.format(line1, diff, line2)


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """

    idx = 0
    if len(lines1) == len(lines2):
        for list_number in range(len(lines1)):
            idx = singleline_diff(lines1[list_number], lines2[list_number])
            if idx != IDENTICAL:
                return (list_number, idx)
    elif len(lines1) > len(lines2):
        for list_number in range(len(lines2)):
            idx = singleline_diff(lines2[list_number], lines1[list_number])
            if idx != IDENTICAL:
                return (list_number, idx)
            
        return (len(lines2), 0)
    else:
        for list_number in range(len(lines1)):
            idx = singleline_diff(lines1[list_number], lines2[list_number])
            if idx != IDENTICAL:
                return (list_number, idx)
            
        return (len(lines1), 0)    
 

    return (IDENTICAL, IDENTICAL)


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    with open(filename, 'r') as doc_file:
        doc_text = doc_file.read()
        doc_text = doc_text.splitlines()

    return doc_text


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    return ""


# Unit Tests
# Single Line Differences
print(singleline_diff("line1", "line2"))
print(singleline_diff("line1", "line1"))
print(singleline_diff("line223", "line2"))
print(singleline_diff(" ", "line2"))
print(singleline_diff('abc', 'abcd'))
# Expected result
# 4
# -1
# 5
# 0
# 3

# singleline_diff_format
print(singleline_diff_format('abc', 'abd', 2))
# Expected result
# 'abc\n==^\nabd\n'

# multiline_diff
print(multiline_diff(['a'], ['b']))
#expected (0, 0)
print(multiline_diff(['line1', 'line2'], ['line1', 'line2']))
#expected (-1, -1)
print(multiline_diff(['line1', 'line2'], ['line1', 'lne2']))
#expected (1, 1)
print(multiline_diff(['lines1', 'line2'], ['line1', 'line2']))
#expected (0, 4)
print(multiline_diff(['line1', 'line2'], ['line1', 'line2', 'line3']))
#expected (2, 0)
print(multiline_diff(['line1', 'line2', 'line3'], ['line1', 'line2']))
#expected (2, 0)
print(multiline_diff([], ['line']))
#expected (0, 0)