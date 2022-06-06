"""
Project for "Python Data Representations".
Find the first difference in text file contents. The function 'difference'
called with two text file names as arguments prints out the number of the line
and a visual indication of the character where the difference is located.
"""

IDENTICAL = -1


def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs (or the index right after
      the shorter of the two lines).

      Returns IDENTICAL if the two lines are the same.
    """
    if len(line1) <= len(line2):
        shortest = line1
    else:
        shortest = line2

    for index in range(len(shortest)):
        if line1[index] != line2[index]:
            return index

    if len(line1) == len(line2):
        return IDENTICAL
    return len(shortest)


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index of first difference between the lines
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2:

      Abcdefg
      ===^
      Abccefg

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if len(line1) <= len(line2):
        shortest = line1
    else:
        shortest = line2

    if ("\n" or "\r") in (line1 or line2):
        return ""
    elif not -1 < idx <= len(shortest):
        return ""
    return line1 + "\n" + ("=" * idx) + "^\n" + line2 + "\n"


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number and the index in that line
      where the first difference between lines1 and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    if len(lines1) <= len(lines2):
        shortest = lines1
    else:
        shortest = lines2

    for line in range(len(shortest)):
        if singleline_diff(lines1[line], lines2[line]) != IDENTICAL:
            return (line, singleline_diff(lines1[line], lines2[line]))

    if len(lines1) == len(lines2):
        return (IDENTICAL, IDENTICAL)
    return (len(shortest), 0)


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
    with open(filename) as openfile:
        data = openfile.readlines()
        lines = []
        for line in data:
            line = line.strip("\n\r")
            lines.append(line)

    return lines


def difference(filename1, filename2):
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
    lines1 = get_file_lines(filename1)
    lines2 = get_file_lines(filename2)
    (line, index) = multiline_diff(lines1, lines2)

    if lines1 == []:
        print_line1 = ""
    else:
        print_line1 = lines1[line]

    if lines2 == []:
        print_line2 = ""
    else:
        print_line2 = lines2[line]

    if (line, index) == (-1, -1):
        print("No differences\n")
        return
    print("Line {}:\n".format(line + 1)
          + singleline_diff_format(print_line1, print_line2, index))
    return


# Demonstration

difference('testfile1.txt', 'testfile2.txt')
