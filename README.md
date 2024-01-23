### General Info
This program implements the Variable Byte Code (VBC) algorithm in Python for encoding and decoding
integers. The VBC algorithm is used to compress integers into a series of bytes.
***
### Example
![Screenshot 2024-01-23 172417](https://github.com/pansk-p/Variable-byte-VB-encoding-/assets/139992839/c4d1f1df-9677-4829-884f-a4b0e1881a40)

***
## Here are the main functions and features of the program
1. **encode_number(number)**: Takes an integer as input and returns its Variable Byte
Code. The algorithm uses a 7-bit encoding method, where each byte consists of 7 data
bits, and the most significant bit (MSB) is a continuation flag.
2. **decode_vbc(bytestream)**: Takes a byte stream as input and decodes it into a list of
integers. It recognizes the continuation flag in the MSB to reconstruct the original
integers.
3. **bytelist_to_string(list)**: Converts a list of bytes to a binary string.
4. **bitstring_to_bytes(s)**: Converts a binary string to bytes.
5. **main()**: Provides a simple user interface for encoding and decoding integers using the
VBC algorithm.
***
### A little intro about how to use. 

The program continuously prompts the user to choose between encoding, decoding, or exiting
the program. It performs input validation to ensure correct user input. The encoding and
decoding processes involve converting integers to/from their VBC representation and binary
strings.

**Run the Python script by entering ```python VariableByteCode.py```.**
