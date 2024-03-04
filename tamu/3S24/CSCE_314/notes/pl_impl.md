# Programming Language Implementation
## A Tour of Language Implementation
- Here we discuss characterization of programming languages, and the implementation of programming languages.
- The compiler checks all the syntax and semantics of the program, and then translates the program into machine code.
- Understanding these steps will help you understand how a compiler works and the errors it can produce.
- Ultimately this will help learning new programming languages.
### Programming Language Characteristics
- There exist different approaches to:
    - Decribe computation/instruct computing devices
        - Imperative
            - C/C++
            - Java
            - Python
        - Declarative
            - SQL
            - Prolog
            - Haskell
        - Functional
            - Lisp
            - Scheme
            - Haskell
            - Sort of python
    - Communicate idea between humans
        - Procedural
            - FORTRAN
            - C
            - Pascal
        - Object-Oriented
            - Java
            - Eiffel
        - Domain-Specific
            - SQL
            - LaTeX
- Programming langauges are **specified** by:
    - Semantics
        - Meaning of the program
    - Syntax
        - Structure of the program
- All sentences should be **unambiguously** specified, with semantics and syntax.
### Programming Language Expressiveness
- The level of abstraction can also characterize programming languages.
- **High-level** languages are more abstract, and are closer to human language.
- **Low-level** languages are closer to machine language.
- Programming langauges tend to become more abstract over time.
### Defining Programming Languages
- Syntax: Define the set of valid programs
    - Usually defined with the help of grammars and other conditions
- Semantics: Define the meaning of the programs
### Implementing a Programming Language
- The task is to undo abstraction, match assembly to the source code.
- This process is usually called compilation, even though the scope of tasks during compilation varies.
- The process of undoing abstraction happens in this kind of process:
    - Source code
    - Lexical Analysis / Lexer
        - Separates the symbols and checks if the code is well formed
        - Produces a sequence of lexical components, or **tokens**
        - Places the tokens in a token table
        - If there is an error in symbols or keywords or syntax, the lexer will produce an error message, and compilation will stop.
        - Final output is a stream of tokens or token table
    - Syntax Analysis / Parser
        - Checks the syntactic structure of the program using the stream of tokens from the lexer
        - For example, the Glasgow Haskell Compiler would check if an `if` statement has a corresponding `then` statement
        - If all syntax is correct, the parser will produce a syntax tree, sometimes called a **parse tree**
        - If there is an error in syntax, the parser will produce an error message, and compilation will stop.
        - Final output is a syntax tree/parse tree
    - Type checker
        - Annotates the syntax tree with type information
        - Checks if all types are used correctly
        - Outputs a type-annotated syntax tree
    - At this point, the program can be run in an interpreter, or compiled to machine code.
    - Many compilers these days are optimizing, so the annotated syntax tree will be optimized before being compiled to machine code.
    - In the case of Java, the Java compiler will produce bytecode, which is then run in the Java Virtual Machine (JVM).
- Recap:
    - Lexical Analysis
        - From a stream of characters to a stream of tokens
        - `if (a == b) return;` would translate to:
        - `keyword['if']`
        - `symbol['(']`
        - `identifier['a']`
        - `symbol['==']`
        - `identifier['b']`
        - `symbol[')']`
        - `keyword['return']`
        - `symbol[';']`
    - Syntax Analysis
        - From a stream of tokens to a syntax tree
        - `if` statement
            - expression
                - `==` operator
                    - identifier
                        - `a`
                    - identifier
                        - `b`
            - statement
                - `return` statement
    - Type Checker
        - From a syntax tree to a type-annotated syntax tree
        - `if` statement: OK
            - expression: bool
                - `==` operator: integer equality
                    - identifier: integer
                        - `a`
                    - identifier: integer
                        - `b`
            - statement: OK
                - `return` statement: void
    - Optimization
        - Say we have that `a` and `b` always have the same value, we can optimize the `==` operator to always return `true`.
        - Then the tree just becomes:
            - `return` statement: void
    - Code Generation
        - Undos the abstraction, and matches the syntax tree to machine code.
            - Control structures become jumps and conditional jumps
                - These are basically `goto` statements
            - Variables become memory addresses
            - Variable names become addresses
            - ADTs disappear, and are broken down to the most primitive types
            - Expressions become load memory, register operations, and store memory
### Typical Errors at Each Stage
- Lexical analysis catches errors in symbols and keywords
    - misspelled keywords
    - wrong symbols
- Syntax analysis ensures that proper experssions are formed
    - e.g. cant have `if` without `then` in Haskell
    - e.g. cant use `+` on `if` statements
- Type checking ensures that types are used correctly
    - Catches type errors
## Formal Languages: Motivation
- We describe the syntax of programming languages using a **phrase structure grammar**.
- A phrase structure grammar is a universal set of rules that can generate all the sentences in a language.
- Regular expressions are a simple form of phrase structure grammar.
- Formal languages are the foundational of computational complexity theory.
### Formal languages
- An **alphabet** $A$ is a set of letters, symbols, or tokens.
- The **binary alphabet** is $\{0, 1\}$, and is used very often in computer science.
- We denote $A^*$ as the set of all strings of any finite length over the alphabet $A$.
    - $A^* = A^0 \cup A^1 \cup A^2 \cup \dots$
    - The exponent denotes the length of the string.
    - $A^0 = \{\epsilon\}$
- An element $s$ of $A^*$ is a **string**, and is given by a concatenation of symbols from $A$.
- The **empty string** is denoted by $\epsilon$.
- A **formal language** over an alphabet $A$ is a subset of $A^*$.
- We refer to the elements of $A^*$ as **words**, or sometimes **sentences**, over the alphabet $A$.
## Formal Languages: Grammars
- The American linguist Noam Chomsky introduced the concept of a **phrase structure grammar**.
- He grouped formal languages into four nested subsets of more and more specific types of grammars.
- A sentence $S$ can be divided into a noun phrase $N_P$ and a verb phrase $V_P$.
    - We can express this as $S \rightarrow N_P V_P$.
    - The noun phrase $N_P$ can be something like $N_P \rightarrow \text{the dog}$ or $N_P \rightarrow \text{the steak}$.
    - The verb phrase $V_P$ can be divided into a verb $V$ and a noun phrase $N_P$.
        - We can express this as $V_P \rightarrow V N_P$.
    - So in this grammar we can form the sentence "the dog ate the steak" as $S \rightarrow N_P V_P \rightarrow \text{the dog ate the steak}$.
    - Here the noun phrase $N_P$ is $\text{the dog}$, and the verb phrase $V_P$ is $\text{ate the steak}$.
- However, we can also say "the steak ate the dog" in this grammar, which doesn't make sense in English.
- Thus, grammars mainly govern the syntax of a language, and not the semantics.
### Phrase Structure Grammars
- A **phrase structure grammar** G consists of:
    - A non-empty finite set $T$ of **terminal symbols**.
        - These are the symbols that appear in the strings of the language.
    - A set $N$ of **non-terminal symbols** (or **variables**).
        - These are the symbols that can be replaced by strings of terminal and non-terminal symbols.
        - These include the start symbol $S$ and is assumed to be disjoint from $T$.
    - The **vocabulary** $V = N \cup T$.
    - A finite set $P$ of **production rules**
        - These production rules are of the form $a \rightarrow b$, such that $a, b \in V^*$.
        - The LHS of the production rule is a single non-terminal symbol.
- We say that the grammar $G$ has the data $G = (N, T, P, S)$.
- We define a binary relation $\Rightarrow$ on $V^*$ such that $v \Rightarrow v'$ if and only if there exist $c, d \in V^*$ and a production rule $a \rightarrow b \in P$ such that $v = c a d$ and $v' = c b d$.
- This just means that we can replace a non-terminal symbol with a string of terminal and non-terminal symbols.
- We denote $\Rightarrow ^*$ as the reflexive and transitive closure of $\Rightarrow$.
- This just means that we can replace a non-terminal symbol with a string of terminal and non-terminal symbols any number of times.
- The grammar $G$ defines the language $L(G)$ as the set of all terminal strings that can be derived from the start symbol $S$.
    - $L(G) = \{w \in T^* | S \Rightarrow^* w\}$.
## Formal Languages: Chomsky Hierarchy
- The Chomsky hierarchy has the following types:
    - Type 0: Phrase structure grammars
        - Universal set of grammars
    - Type 1: Context-sensitive grammars
        - Some restrictions on the production rules
    - Type 2: Context-free grammars
        - More restrictions on the production rules
    - Type 3: Regular grammars
        - Most restrictions on the production rules
- Being regular implies being context-free, and being context-free implies being context-sensitive, and being context-sensitive implies being phrase structure.
- All the types have common uses in computer science
    - Type 3 often form regexes
    - Type 2 often form the syntax of programming languages
    - Type 1 are often used in natural language processing
### Type 3: Regular Grammars
- A grammar is type 3 if and ony if every production rule is of one of the following forms:
    - $A \rightarrow aB$ for some $A, B \in N$ and $a \in T$
        - A and B are non-terminal symbols
        - a is a terminal symbol
    - $A \rightarrow a$ for some $A \in N$ and $a \in T$
        - A is a non-terminal symbol
        - a is a terminal symbol
    - $A \rightarrow \epsilon$ for some $A \in N$
### Type 2: Context-Free Grammars
- A grammar is type 2 if and only if every production rule is of the form:
    - $A \rightarrow w$ for some $A \in N$ and $w \in V^*$
    - $A$ is a single non-terminal symbol
    - $w$ is a string of terminal and non-terminal symbols, or simply just some word
### Type 1: Context-Sensitive Grammars
- A grammar is type 1 if and only if every production rule is of the form:
    - $uAw \rightarrow uvw$
        - for some nonterminal $A \in N$ 
        - words $u, w \in V^*$
        - some word $v \in V^+ = V^*\setminus \{\epsilon\}$
### Type 0: Phrase Structure Grammars or Recursively Enumerable Languages
- A type 0 grammar has no restrictions on the production rules.
- It is called recursively enumerable because the words can be enumerated given enough memory.
### Other stuff
- A formal language without the empty string is called **proper**.
- $\mathcal{L}_3 \subset \mathcal{L}_2 \subset \mathcal{L}_1 \subset \mathcal{L}_0$
Understanding the type of a language in the Chomsky hierarchy and its mathematical restrictions can be quite abstract. However, there are intuitive approaches to both determining a language's type and understanding the restrictions placed on it.

### Intuitive Understanding of Language Types

1. **Type 3 (Regular Languages):**
   - **Intuition**: Think of these as the simplest patterns. If you can imagine a language that can be described by patterns that don't require remembering anything beyond the current symbol (like a simple search pattern), then it's likely a regular language. Regular languages are what you can match with regular expressions.
   - **Example**: Identifiers in programming languages, simple numeric constants, or even the format of phone numbers and email addresses.

2. **Type 2 (Context-Free Languages):**
   - **Intuition**: These languages can be described by rules that don't depend on the context of the use. If you can represent the structure of the language with a nested, tree-like diagram without needing to know what's around a particular element (e.g., the syntax of expressions in programming languages), then it's a context-free language.
   - **Example**: The syntax of arithmetic expressions or the nested structure of HTML/XML documents.

3. **Type 1 (Context-Sensitive Languages):**
   - **Intuition**: Here, the context starts to matter. If you need to know the surrounding elements to decide how a part of the language can be used or interpreted (like agreement between subjects and verbs in some natural languages, or dependencies in complex programming constructs), then it's likely a context-sensitive language.
   - **Example**: Certain aspects of natural languages (such as gender agreement in languages like French or Spanish), or compiler checks that require understanding more than just the local syntax (e.g., variable declarations must precede their use).

4. **Type 0 (Recursively Enumerable Languages):**
   - **Intuition**: These are the most general and powerful languages, capable of expressing any computable function. If the language can describe anything that a computer program can do, without any restrictions on memory or runtime, then it fits here. This includes languages that are too complex to be described by simpler automata or grammars.
   - **Example**: Problems that require complex computations, like some problems in artificial intelligence or cryptography.

### Understanding Mathematical Restrictions Intuitively

- **Type 3 (Regular Languages):** The key restriction is memorylessness. Imagine a device that reads input left to right without going back or remembering past symbols except for the state it's in. This limitation makes regular languages the least powerful but fastest to process.

- **Type 2 (Context-Free Languages):** These languages allow for a "stack" memory (imagine nesting, like parentheses in math expressions). The restriction is that each rule's application doesn't depend on "where" in the language (or input) it's applied. This allows for hierarchical structures but not for enforcing complex relationships that depend on context beyond immediate nesting.

- **Type 1 (Context-Sensitive Languages):** The restrictions loosen further, allowing rules that depend on the surrounding context. The intuition here is like understanding a sentence's meaning by considering the words around a particular word. This allows for expressing more complex relationships but at the cost of greater computational resources to process.

- **Type 0 (Recursively Enumerable Languages):** Essentially, there are no restrictions besides computability. If you can imagine a procedure (no matter how complex) to generate or recognize the language, it fits here. The intuition is the power of full computer programs, with the trade-off being that some problems might not have a guaranteed solution method (i.e., they can be undecidable).

Understanding these types and restrictions intuitively helps demystify the formal definitions and makes it easier to classify languages or understand the capabilities and limitations of different computational models.