no_of_chars = 256

def findSubString(string, pat):
    len1 = len(string)
    len2 = len(pat)

    # check if string's length is less than pattern's
    # length. If yes then no such window can exist
    if len1 < len2:
        print("No such window exists")
        return ""

    hash_pat = [0] * no_of_chars
    hash_str = [0] * no_of_chars

    # store occurrence ofs characters of pattern
    for i in range(0, len2):
        hash_pat[ord(pat[i])] += 1

    start, start_index, min_len = 0, -1, float('inf')

    # start traversing the string
    count = 0  # count of characters
    for j in range(0, len1):

        # count occurrence of characters of string
        hash_str[ord(string[j])] += 1
        if (hash_pat[ord(string[j])] != 0 and hash_str[ord(string[j])] <= hash_pat[ord(string[j])]):
            count += 1
        print(string[j], " " , hash_str[ord(string[j])])

        # if all the characters are matched
        if count == len2:
            while (hash_str[ord(string[start])] > hash_pat[ord(string[start])] or hash_pat[ord(string[start])] == 0):
                if (hash_str[ord(string[start])] > hash_pat[ord(string[start])]):
                    hash_str[ord(string[start])] -= 1
                start += 1

            # update window size
            len_window = j - start + 1
            if min_len > len_window:
                min_len = len_window
                start_index = start

                # If no window found
    if start_index == -1:
        print("No such window exists")
        return ""

        # Return substring starting from
    # start_index and length min_len
    return string[start_index: start_index + min_len]


if __name__ == "__main__":
    string = "this is a test string tits"
    pat = "tist"

    print("Smallest window is : ")
    print(findSubString(string, pat))



# filename_list = ['0000_Poodel.jpg', 'Poodle.jpg', 'Poodle_13344.jpg', '.asdfa.jpg' ]
#
# results_dic = {}
#
# for i in filename_list:
#         if i.startswith('.'):
#             continue
#         label = ''
#         if i not in results_dic:
#             temp_label = i.lower().split('_')
#             for word in temp_label:
#                 word = word.split('.')[0]
#                 if word.isalpha():
#                     label += word + " "
#             label = label.strip()
#             results_dic[i] = [label]
#
# print(results_dic)


# from typing import List
#
# mylist=[2, 3, 4, 5]
# print(range(len(mylist)))
#
# mycities = ["seoul", "tokyo", "la", "garden", "grove"]
# print(mycities)
#
# myciti_with_title = [city+"hm" for city in mycities]
#
# print(myciti_with_title)
#
# def simpleGeneratorFun():
#     yield 1
#     yield 2
#     yield 3
#
# print(simpleGeneratorFun())
# print(simpleGeneratorFun())
# print(simpleGeneratorFun())
#
# for x in simpleGeneratorFun():
#     print(x)
#
# sq_list = [x**2 for x in range(10)]  # this produces a list of squares
#
# sq_iterator = (x**2 for x in range(10))  # this produces an iterator
#
# print(sq_list)
# print(sq_iterator)
#
# if mycities[5] != "tokyo":
#     print (mycities[5])