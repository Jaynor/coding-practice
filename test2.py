def sub_1(num, total):
    print(num)
    if num == 1:
        return total
    else:
        total = sub_1(num - 1, total)
        print(total)
        total = total + 1
    return total


def sub_2(num, total):
    if num - 1 != 0:
        sub_2(num - 1, total + 1)
    else:
        return total


def main():
    total = 0
    #total = sub_1(10, 1)
    #print("the result", total)
    total = sub_2(10, 0)
    print("the result", total)
main()