# How to use the code
- Change the file paths in the main function to the test cases and expected output
- Run the code, output should look something like this:
```
$ python algo.py
Test cases:
Predicted                                Actual                                   Match?
------------------------------------------------------------------------------------------
[1, 0, 0, 0, 1, 0]                       [1, 0, 0, 0, 1, 0]                       ✓
[0, 1, 0, 1, 0]                          [0, 1, 0, 1, 0]                          ✓
[]                                       []                                       ✓
[]                                       []                                       ✓
[0, 0, 0, 0, 1, 0, 0]                    [0, 0, 0, 0, 1, 0, 0]                    ✓
[1, 1, 0, 1, 0, 1, 0]                    [1, 1, 0, 1, 0, 1, 0]                    ✓
[0, 0, 1, 1, 1]                          [0, 0, 1, 1, 1]                          ✓
[0, 1, 0, 1, 1, 0, 0, 0]                 [0, 1, 0, 1, 1, 0, 0, 0]                 ✓
[1, 0, 0, 0, 0]                          [1, 0, 0, 0, 0]                          ✓
[0, 0, 0, 0, 1, 0, 1, 1]                 [0, 0, 0, 0, 1, 0, 1, 1]                 ✓

Overall match: ✓
```