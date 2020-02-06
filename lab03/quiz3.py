# CINDY LU AND VIVIAN

def avg_best_3(a, b, c, d):
    # this name should be fixed
    num_list = [a, b, c, d]
    min_ = (min(num_list))
    num_list.remove(min_)
    avg_ = (num_list[0] + num_list[1] + num_list[2]) / 3
    return avg_  # we should not have this name


def search(sentence, substring):
    if substring in sentence:
        result = sentence.index(substring)
        return result
    else:
        result = -1
        return result


def main():
    num_1 = int(input("Please enter a integer grades between 0 and 100: "))
    num_2 = int(input("Please enter a integer grades between 0 and 100: "))
    num_3 = int(input("Please enter a integer grades between 0 and 100: "))
    num_4 = int(input("Please enter a integer grades between 0 and 100: "))
    print(avg_best_3(num_1, num_2, num_3, num_4))

    print(search("hello world", "world"))
    print(search("hello world", "yes"))

    final_list = [4353, 2314, 2956, 3382, 9362, 3900]
    final_list.remove(3382)
    print(final_list)
    final_list = [4353, 2314, 2956, 3382, 9362, 3900]
    print(final_list.index(9362))
    final_list = [4353, 2314, 2956, 3382, 9362, 3900]
    final_list.insert(5, 4499)
    print(final_list)
    final_list = [4353, 2314, 2956, 3382, 9362, 3900]
    final_list.extend([5566, 1830])
    print(final_list)
    final_list = [4353, 2314, 2956, 3382, 9362, 3900]
    final_list.reverse()
    print(final_list)
    final_list = [4353, 2314, 2956, 3382, 9362, 3900]
    final_list.sort()
    print(final_list)


if __name__ == "__main__":
    main()
