<h1><b>Hangman - CLI</b></h1>

<h2><b>Synopsis</b></h2>

This is a command line version of the popular [Hangman](https://en.wikipedia.org/wiki/Hangman_(game)) game, implemented in Python.

<h2><b>Requirements</b></h2>

Python version 2.6+

<h2><b>Usage</b></h2>

To play the game, simply run `python hangman.py` in the Terminal, from the directory of the extracted files.

<h2><b>How it works</b></h2>

The `wordlist.txt` file contains a list of words, from which a random word is chosen. According to the length of the word, corresponding dashes (`_`) are displayed on the terminal. The player has to guess the word, a letter at a time, entering in the terminal. If anything other than a letter is entered, an error is displayed. Also, the player is reminded if a letter is guessed more than once. The player is only allowed to wrongly guess a maximum of 5 letters, reaching which, the game ends with the word being revealed, and the player losing. If the player guesses the word correctly, the game ends with the player winning, and a choice to play again.

<h2><b>To add</b></h2>

1. High score of winning streak
2. Choice of categories for words

<h2><b>License</b></h2>

Please view LICENSE.md for details on the usage of code in this repository.
