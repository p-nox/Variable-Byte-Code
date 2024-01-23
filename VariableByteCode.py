from struct import pack, unpack

def encode_number(number):
    bytes_list = []
    while True:
        bytes_list.insert(0, number % 128)
        if number < 128:
            break
        number = number // 128 
    bytes_list[-1] += 128
    return (bytes_list)

def decode_vbc(bytestream):
    n = 0
    numbers = []
    bytestream = unpack('%dB' % len(bytestream), bytestream)
    for byte in bytestream:
        if byte < 128:
            n = 128 * n + byte
        else:
            n = 128 * n + (byte - 128)
            numbers.append(n)
            n = 0
    return numbers

##Conversion functions   
def bytelist_to_string(list): 
    str = ""
    for i in list:
        str += "".join(format(i, '08b'))
    return str

def bitstring_to_bytes(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, byteorder='big')

def main():  
   while True:
    try:
        inp = int(input("Enter 1-to encode, 2-to decode, 3-to exit:"))
        ##Encode
        if (inp == 1): 
           inp = int(input("Enter a number to encode: "))
           if (inp < 0 ):
               print("The input must be a possitive number")
           else :
                result = encode_number(inp)
                print("The Variable Byte Code of " + str(inp) + " is : " + bytelist_to_string(result))
        ##Decode        
        elif (inp == 2):
            inp = input("Enter the bitstring to decode: ")  
            l = int(len(inp) / 8)
            ##The input must be in packs of 8-bits each
            if(len(inp) % 8 != 0 ):
                 print('Wrong Variable Byte Code format -> Incorrect lenght')
            elif(len(inp) % 8 == 0 ):
                success = True
                ##Check the input for 0 or 1   
                for ch in inp:
                 if (ch != '1' and ch != '0'):   
                    print('Wrong Variable Byte Code format -> VBC contains only 0 or 1')
                    success = False
                    break
                ##If input is 1-byte must beggin with 1
                if(l == 1 and inp[0] != '1' and success):
                        print('Wrong format -> The first bit must be 1')
                        success = False
                ##else the first byte must start with 0 and the last with 1                  
                elif(l > 1 and success ):
                    if(inp[0] != '0' or inp[len(inp)-8] != '1' ):
                           print('Wrong format -> The first bit must be 0 and the last byte must start with 1')
                           success = False 
               ##If the test passed decode input
                if(success):
                  result = decode_vbc(bitstring_to_bytes(inp))
                  print("The Variable Byte Code of " + str(inp) + " is : " ,result)          
        elif (inp == 3):
           print("Exit...")
           break  
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
  
if __name__ == "__main__":
    main()
