#!/usr/bin/env python
''' Farsi flashcards on the command line. '''

import sys


def main():
    '''
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
    # randomize list

    english = ['ellipsis']
    farsi = ['...']
    rosetta = zip(english, farsi)

    for english_text, farsi_text in rosetta:

        # ask question
        prompt = '>>> What is "{}" in english? '.format(farsi_text)

        while True:
            try:
                answer = raw_input(prompt)
            except (KeyboardInterrupt, EOFError):
                sys.exit('\n\nGoodbye.')

            if answer == 's':
                break
            elif answer != english_text:
                print('\nnope, try again')
                continue
            else:
                print('{}, correct!'.format(answer))
                break


if __name__ == '__main__':
    main()
