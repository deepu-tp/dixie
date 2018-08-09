def init_data():
    from collections import defaultdict
    import json
    words = defaultdict(list)
    small_list = defaultdict(list)
    with open('data/words.txt', 'r') as words_file:
        a = words_file.readlines()
        for each in a:
            each = each.strip(' \n\r\t')
            if each.isalpha():
                words[len(each)].append(each)
    with open('data/small_list.txt', 'r') as words_file:
        a = words_file.readlines()
        for each in a:
            each = each.strip(' \n\r\t')
            if each.isalpha():
                words[len(each)].append(each)
                small_list[len(each)].append(each)
    json.dump([words, small_list], open('data/words.json', 'w'))


def load_data():
    import json
    return json.load(open('data/words.json'))


def cal_score(a, b):
    from collections import deque
    em, pm = 0, 0
    new_a, new_b = "", ""
    for i, val in enumerate(a):
        if a[i] == b[i]:
            em += 1
        else:
            new_a += a[i]
            new_b += b[i]

    new_a = sorted(list(new_a))
    new_b = sorted(list(new_b))
    # print(new_a, new_b)
    while new_a and new_b:
        # print(new_a[0], new_b[0])
        if new_a[0] == new_b[0]:
            new_a.pop(0)
            new_b.pop(0)
            pm += 1
        elif new_a[0] < new_b[0]:
            new_a.pop(0)
        else:
            new_b.pop(0)

    return em, pm


def play(data):
    import random
    small_list = data[1]
    data = data[0]
    while True:
        try:
            n_of_chrs = int(input("Please enter number of chars [4-15]:"))
            if n_of_chrs < 4 or n_of_chrs > 15:
                continue
            break
        except ValueError:
            print("Please enter a valid number")

    while True:
        try:
            n_of_turns = int(input("Please enter number of turns [4-15]:"))
            if n_of_turns < 4 or n_of_turns > 15:
                continue
            break
        except ValueError:
            print("Please enter a valid number")

    main_word = random.choice(small_list[str(n_of_chrs)])
    # print(main_word)
    main_list = set(data[str(n_of_chrs)])
    current_turn = 0
    while current_turn < n_of_turns:
        print('{}) '.format(current_turn + 1), end='')
        this_turn = input()
        if len(this_turn) != len(main_word):
            print("Please enter a " + str(n_of_chrs) + " character word")
            continue
        if this_turn not in main_list:
            print("Please enter a valid dictionay word")
            continue
        if this_turn == main_word:
            print("You Won!!!!!!!")
            return
        em, pm = cal_score(main_word, this_turn)
        print("PM = {}, EM = {}".format(pm, em))
        current_turn += 1
    print("You Lost :((")
    print("The word was " + main_word)


if __name__ == '__main__':
    init_data()
    play(load_data())
    # print(cal_score("barit", "chill"))
