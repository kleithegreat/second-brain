## 01/30/2024
- truth tables should be sorted in ascending order (start from 0, start accumulating 1s starting from the right)
- truth tables have $2^n$ rows where $n$ is the number of variables
- example:
$$ \begin{array}{c c c | c}
    a & b & c & abc > 5 \\
    \hline
    0 & 0 & 0 & 0 \\
    0 & 0 & 1 & 0 \\
    0 & 1 & 0 & 0 \\
    0 & 1 & 1 & 0 \\
    1 & 0 & 0 & 0 \\
    1 & 0 & 1 & 1 \\
    1 & 1 & 0 & 1 \\
    1 & 1 & 1 & 1 \\
\end{array} $$
- abc > 5 = ab'c + abc' + abc
- sum of minterms form should have one minterm for each true row in the truth table
    - very easy conversion to truth table
- in schematic diagrams a filled dot means the signal is combined
- EJ prefers directly converting sum of minterms to a column of AND gates feeding into a single OR gate
- silicon naturally has the (complete) NAND and NOR gates
- completeness of NAND:
    - NOT is a 1 input NAND gate
    - NOT can also be a 2 input NAND with the inputs tied together
    - AND is just NAND followed by NOT (remember NOT can be made by NAND)
        - involution
    - OR is NAND preceded by NOTS

> QUIZ: can you build OR with only NAND?
f = (a' * b')' = a + b (DeMorgan's Law)

- encoding and decoding helps save space

> QUIZ: definition of decoder + decoder truth table (2 input decoder)

## 02/01/2024
vahid chapter 2 and 3
> QUIZ: D flip-flop shit and the other example