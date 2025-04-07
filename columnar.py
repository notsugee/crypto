import numpy as np 

key = 4312567
plaintext = "attack postponed until two am"

def rail_fence(key, plaintext):
    # prepping variables
    plaintext = plaintext.replace(" ", "")
    key_list = [int(i) for i in str(key)]
    sorted_key_list = sorted(key_list)

    remainder = len(plaintext) % len(key_list)
    if remainder != 0:
        number_of_extra_chars = len(key_list) - remainder
        for i in range(123-number_of_extra_chars, 123):
            plaintext += chr(i)
    
    print(plaintext)

    # encryption
    cols = len(key_list)
    rows = len(plaintext) // cols 
    rect = np.array([letter for letter in plaintext]).reshape(rows, cols)
    print(rect)
    
    ciphertext = ""
    for number in sorted_key_list:
        col_index = key_list.index(number)
        ciphertext += "".join(list(rect[:,col_index]))

    print(ciphertext)
    
    # decryption
    plaintext = ""
    rect2 = np.empty((rows, cols), dtype=str)
    index = 0
    for number in sorted_key_list:
        col_index = key_list.index(number)
        rect2[:, col_index] = list(ciphertext[index:index + rows])
        index += rows

    plaintext = "".join(rect2.flatten())
    print(rect2)
    
    print(plaintext[0:len(plaintext) - number_of_extra_chars])
def main():
    rail_fence(key, plaintext)

if __name__ == "__main__":
    main()
