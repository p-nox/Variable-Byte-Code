### General Info
This program implements the Variable Byte Code (VBC) algorithm in Python for encoding and decoding
integers. The VBC algorithm is used to compress integers into a series of bytes.

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

1. **Run the Python Script:** ```python vbc_encoder_decoder.py```

2. **Follow the Instructions:**
   
    Enter ```1``` to encode a positive integer.
   
    Enter ```2``` to decode a Variable Byte Code bitstring.
   
    Enter ```3``` to exit the script.
***   
### Examples

**Encode**

     Enter 1-to encode, 2-to decode, 3-to exit: 1
     
     Enter a number to encode: 42
     
     The Variable Byte Code of 42 is: 101010
     


**Decode**

     Enter 1-to encode, 2-to decode, 3-to exit: 2
     
     Enter the bitstring to decode: 101010
     
     The Variable Byte Code of 101010 is: [42]

***   
### Notes
 * The script ensures correct input formats during encoding and decoding.
 * Be sure to enter positive integers for encoding.
