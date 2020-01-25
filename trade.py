
#97 - 122


def merge_string(string_list):

    # Creating a dictionary(hash table) of lower case alphabet
    alpha_dic = {}
    for i in range(97, 123):
        alpha_dic[i] = 0

    # Going through the all the characters in the list ONLY once and update the dictionary.
    # This is the O(N) case when we assume N == number of characters in the list.
    for item in string_list:
        for letter in item:
            letter = ord(letter)
            if letter in alpha_dic:
               alpha_dic[letter] += 1

    # Check dictionary and creating a return string with value > 1
    return_string = ''
    for key, value in alpha_dic.items():
        if value > 0:
            for value_len in range(value):
                return_string += chr(key)

    return return_string


def main():
    string_list = ['asb', 'asdddf', 'gahj']
    merge_string((string_list))

main()