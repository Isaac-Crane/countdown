from english_words import get_english_words_set
import sys

web2lowerset = get_english_words_set(['web2'], lower=True)
letters = sys.argv[1].lower()

def check_all_combinations(remaining_letters, ordered_letters = ''):
    combo_list = []
    if len(remaining_letters) != 0:
        for i in range(len(remaining_letters)):
            added_letters = ordered_letters + remaining_letters[i]
            value = check_all_combinations(remove(remaining_letters, i), added_letters)
            combo_list = list(set(combo_list).union(set(value)))
        return combo_list
    else:
        if ordered_letters in web2lowerset:
            return [ordered_letters]
        else:
            return []

def remove_x_letters(letters, x, combo_list = []):
    if x == 0:
        value = check_all_combinations(letters)
        combo_list = list(set(combo_list).union(set(value)))
    else:
        for i in range(len(letters)):
            updated_letters = remove(letters, i)
            value = remove_x_letters(updated_letters, x-1)
            combo_list = list(set(combo_list).union(set(value)))
    return combo_list
def remove(s, indx):
    updated_string = ''
    for i in range(len(s)):
        if i != indx:
            updated_string = updated_string + s[i]
    return updated_string

def play_game(letters):
    not_found = True
    len_to_check = len(letters)
    while not_found is True:
        value = remove_x_letters(letters, len(letters)-len_to_check)
        if value != []:
            not_found = False
            print(len_to_check)
            print(value[0])
            print(value)
            back_up_value = []
            print(len_to_check)
            while back_up_value == []:
                len_to_check -= 1
                print(len_to_check)
                back_up_value = remove_x_letters(letters, len(letters)-len_to_check)
                if back_up_value != []:
                    print(back_up_value[0], 'is a shorter backup')
                    print(back_up_value)
        else:
            len_to_check -= 1
        if len_to_check == 0:
            print('cant')
            not_found = True
while '1' not in letters:
    play_game(letters)
    letters = input('Do you want to play again? If not include 1. If yes, type the letters.')