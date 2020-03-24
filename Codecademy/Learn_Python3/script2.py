def decode(message,offset):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuation = ".,?'! "
    translated_message = ""
    for letter in message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value + offset) % 26]
        else:
            translated_message += letter
    return translated_message

def code(message,offset):
    translated_message = ""
    for letter in message_for_v:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value - offset) % 26]
        else:
            translated_message += letter
    return translated_message

for i in range(26):
  print('The encrypted message is : \"'+ decode("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.",i) + '\". \nOffset:' + str(i) + '\n\n')