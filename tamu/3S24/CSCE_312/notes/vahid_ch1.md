# 1 - Introduction
## 1.1 Digital Systems in the World Around Us
Blah blah blah computers are small and they help us do things.
## 1.2 The World of Digital Systems
### Digital versus Analog
- A **digital** signal is discrete
    - It can only take on a finite number of values
    - Example: number of fingers you can hold up
- An **analog** signal is continuous
    - It can take on any value in a range
    - Example: temperature outside
- Computing systems typically use digital signals that are on or off
    - This is called binary
- A **digital system** is a system that takes digital inputs and makes digital outputs
- A **digital circuit** is a circuit that uses digital components to make a digital system
- A single binary digit is called a **bit**
#### Digital Circuits are the Basis for Computers
- Digital circuits let us build microprocessors
    - Microprocessors serve as the brain for general purpose computers
#### Digital Circuits are the Basis for Much More
- More and more new applications convert analog signals to digital signals
    - This can result in numerous benefits
        - Easier to store and transmit
        - Easier to process
        - Easier to combine with other digital signals
        - Lack of degradation over time
        - Compression
    - Devices such as cell phones, digital cameras, and MP3 players use digital circuits to convert analog signals to digital signals
- Digital circuits found in applications that are not computers are called **embedded systems**
- Analog to digital conversion is called **digitization**
- Digital to analog conversion is called **digital to analog conversion**
### Digital Encodings and Binary Numbers - 0s and 1s
#### Encoding analog phenomena
- A **sensor** measure analog physical phenomena and converts it to an electrical signal
- An **analog to digital converter** converts the electrical signal from sensors to a digital signal
- A **digital to analog converter** converts a digital signal to an electrical signal
- An **actuator** converts an electrical signal to an analog physical phenomena
- Sensors and actuators together are called **transducers**--devices that convert one form of energy to another
#### Encoding Digital Phenomena
- Some phenomena are inherently digital
    - Example: a switch is either on or off
- Digital phenomena can be encoded using binary numbers
    - Example: 0 = off, 1 = on
    - Example: ASCII encoding for characters
#### Encoding Numbers as Binary Numbers
- Binary works where each digit is a power of 2
- The **weight** of a digit is the power of 2 that it represents
- The **least significant bit** is the bit with the smallest weight, or the rightmost bit
- The **most significant bit** is the bit with the largest weight, or the leftmost bit
#### Converting from Binary to Decimal
- Just sum the weights of the bits that have a value of 1
- You can tell if a binary number is odd by looking at the least significant bit
#### Converting from Decimal to Binary Using the Addition Method
- Start with the largest power of 2 that is less than or equal to the number
- Populate the bits from left to right with the largest power of 2 that is less than or equal to the remaining number
#### Hexadecimal and Octal Numbers
- Hexadecimal is base 16
    - Also known as just **hex**
    - The numbers 0-9 are the same as in decimal
    - The numbers 10-15 are represented by the letters A-F
    - Hexadecimal is useful because it is easy to convert to and from binary
    - Each hex digit is 4 bits
- Octal is base 8
    - Octal numbers are also sometimes used as shorthand for binary numbers
#### Automatic Conversion from Decimal to Binary Using the Divide-by-2 Method
- Keep dividing the decimal number by 2 and the remainder at each step is the next bit
    - Example: 12 / 2 = 6 R 0, 6 / 2 = 3 R 0, 3 / 2 = 1 R 1, 1 / 2 = 0 R 1
    - So 12 in binary is 1100
- This method can be generalized to convert from decimal to any base
    - This is called **divide-by-n**, where n is the new base
    - In binary, n = 2
#### Bytes, Kilobytes, Megabytes, and More
- A **byte** is 8 bits
- *kilo* means 10<sup>3</sup>
- *mega* means 10<sup>6</sup>
- *giga* means 10<sup>9</sup>
- *tera* means 10<sup>12</sup>
## 1.3 Implementing Digital Systems: Microprocessors versus Digital Circuits
- A **microprocessor** is a digital circuit that can be programmed to perform a variety of tasks
- A **digital circuit** is a circuit that uses digital components to perform a specific task
### Software on Microprocessors: The Digital Workhorse
- A **microprocessor** is a digital circuit that can be programmed to perform a variety of tasks
- Microprocessors tend to be readily available and inexpensive
### Digital Design--When Microprocessors Aren't Good Enough
- Sometimes microprocessors are too slow
- Custom digital circuits can execute lots of instructions in parallel, where microprocessors can only execute one or a few instructions at a time
- A **circuit** is an interconnection of electric components