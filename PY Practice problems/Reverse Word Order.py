# REVERSE WORD ORDER

'''
Write a program (using functions!) that asks the user for a long string 
containing multiple words. Print back to the user the same string, except 
with the words in backwards order. For example, say I type the string:

  My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.
'''

def rev_word_ordr():
  ask_usr = input('Enter a Sentence: ')

  split_sent = []
  split_sent = ask_usr.split(' ')
  rev_form = split_sent[::-1]

  print(*rev_form)

rev_word_ordr() 