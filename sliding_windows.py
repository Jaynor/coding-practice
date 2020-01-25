def sliding_windows_no_duplicate_in_pattern(my_string, my_set):
    if len(my_string) < len(my_set):
        print("No such pattern existed!")
        return 0
    best_score = float('inf')
    left_idx = 0
    right_idx = 0
    count = 0
    set_hash = {}
    str_hash = {}

    for item in my_set:
        set_hash[item] = 1

    while right_idx < len(my_string):
        if my_string[right_idx] not in str_hash:
            str_hash[my_string[right_idx]] = 1
        else:
            str_hash[my_string[right_idx]] += 1

        if my_string[right_idx] in set_hash and str_hash[my_string[right_idx]] == set_hash[my_string[right_idx]]:
            count += 1
        if count == len(my_set):

            while (my_string[left_idx] in set_hash and str_hash[my_string[left_idx]] > set_hash[my_string[left_idx]]) \
                    or my_string[left_idx] not in set_hash:
                if my_string[left_idx] in set_hash and str_hash[my_string[left_idx]] > set_hash[my_string[left_idx]]:
                    str_hash[my_string[left_idx]] -= 1
                left_idx += 1
            best_score = (right_idx - left_idx + 1)
            print(best_score)
        right_idx += 1
    if best_score == float('inf'):
        print("No such pattern existed!")
    return best_score

def main():
    my_string = 'abczzphabc'
    my_set = {'a', 'b', 'c', 'h', 'p'}
    print(sliding_windows_no_duplicate_in_pattern(my_string, my_set))

main()