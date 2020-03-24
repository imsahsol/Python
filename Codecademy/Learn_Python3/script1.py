def decode(message,keyword):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    punctuation = ".,?'! "
    m_len = len(message)
    k_len = len(keyword)
    index = 0
    crypto = ''
    for letter in message:
        if not letter in punctuation:
            k_index = alphabet.find(keyword[index%k_len])
            crypto += alphabet[k_index]
            index += 1
        else:
            crypto += letter
    index = 0
    translated_message = ''
    for letter in message:
        if not letter in punctuation:
            k_index = alphabet.find(message[index])
            i_index = alphabet.find(crypto[index])
            translated_message += alphabet[abs((k_index - i_index)%26)]
            index += 1
        else:
            translated_message += letter
            index += 1
    # print(crypto)
    return translated_message

# print('This is test sentence, Please test this out!')
# decode('This is test sentence, Please test this out','friends')
print(decode('dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!','friends'))