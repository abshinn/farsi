#!/usr/bin/env python
''' Farsi flashcards on the command line. '''

import sys
import codecs


def main():
    '''
    Take a map of english and farsi phrases, and prompt the user to enter a
    given farsi phrase in english.
    '''

    ground_rules = '''
        Farsi Flashcards!

        Keyboard Shortcuts
        ------------------
            use ctrl-c to exit
            use s to skip phrase
        '''

    print(ground_rules)

    # load farsi/english items
    with open('english_library_short.txt') as english_file:
        english = english_file.readlines()
    english = [word.strip() for word in english]

    with codecs.open('farsi_library_short.txt', encoding='utf-8') as farsi_file:
        farsi = farsi_file.readlines()
    farsi = [word.strip() for word in farsi]

    rosetta = zip(english, farsi)

    # randomize list


    for english_phrase, farsi_phrase in rosetta:

        # ask question
        prompt = '>>> What is "{}" in english? '.format(farsi_phrase)

        while True:
            try:
                answer = raw_input(prompt)
            except (KeyboardInterrupt, EOFError):
                sys.exit('\n\nGoodbye.')

            if answer == 's':
                break
            elif answer != english_phrase:
                print('\nnope, try again')
                continue
            else:
                print('{}, correct!'.format(answer))
                break


if __name__ == '__main__':
    main()
