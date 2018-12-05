""" file to make a cipher text (and this is a docstring) """

###imports section
import string

###Constants Section
CHAR_SET = string.printable[:-5]
SUBSTITUTION_CHARS = CHAR_SET[-3:]+CHAR_SET[:-3]
# generate encryption dictionary from the character set and its subs
ENCRYPTION_DICT ={}
DECRYPTION_DICT ={}
for i, k in enumerate(CHAR_SET):
    v= SUBSTITUTION_CHARS[i]
    ENCRYPTION_DICT[k]=v
    DECRYPTION_DICT[v]=k
    
    
TEST_MESSAGE = "I like monty python. They are very funny."

###Functions section

def encrypt_msg(plaintext, encrypt_dict):
    ciphertext = []
    for k in plaintext:
            v = encrypt_dict[k]
            ciphertext.append(v)
            # you could just say
            #ciphertext.append(encrypt_dict[k])
            #I split it out so you could follow  it better
    return ' '.join(ciphertext)


def decrypt_msg(ciphertext, decrypt_dict):
    plaintext = []
    for k in ciphertext:
            v = decrypt_dict[k]
            plaintext.append(v)
    return ' '.join(plaintext)



 

"""Testing Section
test_message = TEST_MESSAGE
ciphertext = encrypt_msg(test_message, ENCRYPTION_DICT)
plaintext = decrypt_msg(ciphertext, DECRYPTION_DICT)

print(test_message)
print(ciphertext)
print(plaintext)
print(plaintext == test_message)

my_dictionary={'d':'a'}
my_dictionary['d']

#an empty dictionary
my_empty_dictionary = {}
#earlier example, dictionary with one item
my_dictionary={'d':'a'}
#dictionary with two items seperated by a comma
my_dictionary={'d':'a', 'e':'b'}

k= 'f'
v = 'c'
my_dictionary[k]= v #create a new item in the existing dictionary
my_dictionary
[x for x in enumerate ("Hello")]
for i, c in enumerate("Hello"):
    print(i,c)

a_string= " "
a_string
for i in list(range(10)):
    a_string= a_string +str(i) #add '0' then '1' and so on

accumulator = []
for i in list(range(10)):
          accumulator.append(str(i))

' '.join(accumulator)"""

message= input("Type the message to encrypt below:\n")
ciphertext= encrypt_msg(message, ENCRYPTION_DICT)
plaintext = decrypt_msg(message, DECRYPTION_DICT)

print("This message encrypts to")
print(ciphertext)
print #just a blank line for readability
print("This message decrypts to")
print(plaintext)



    
          


