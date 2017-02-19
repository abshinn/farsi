#!/usr/bin/env python
''' Farsi flashcards on the command line. '''

import sys
from random import shuffle

def main():
    '''
    Given files with a map of English and Farsi phrases, prompt user to answer
    in English for a corresponding Farsi phrase.
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
    with open('english_library.txt') as english_file:
        english = english_file.readlines()
    english = [word.strip() for word in english]

    with open('farsi_library.txt') as farsi_file:
        farsi = farsi_file.readlines()
    farsi = [word.strip() for word in farsi]

    rosetta = zip(english, farsi)

    # randomize list
    shuffle(rosetta)

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
	    elif answer == '?':
	 	print('{}\n'.format(english_phrase))
		break
            elif answer != english_phrase:
                print('\nnope, try again\n')
                continue
            else:
                print('{}, correct!\n'.format(answer))
                break


if __name__ == '__main__':
    main()
