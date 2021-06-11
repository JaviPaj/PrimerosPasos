import random


def hangman():
    with open("./secrets_words.txt","r", encoding="UTF-8") as w:
        target_word = random.choice(list(w)).strip().upper()
        word_hidden = ["_"] * len(target_word)

        print(target_word)
        print(word_hidden)

if __name__=="__main__":
    hangman()
  
