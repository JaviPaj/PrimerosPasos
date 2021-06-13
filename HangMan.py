import random
import os

def word_select():
    # This function will select a word from the list and make it capital letters & unaccented.
    with open("./secrets_words.txt","r", encoding="UTF-8") as w:
        selected_word = random.choice(list(w)).strip().upper()
        accents = selected_word.maketrans("ÁÉÍÓÚ","AEIOU")
        target_word = selected_word.translate(accents)
        return target_word


def game():
    target_word = word_select()
    transf_to_underscore = ["_"] * len(target_word)
    test = len(target_word)
    letter_index_dict = {}

    for idx, letter in enumerate(target_word):
        if not letter_index_dict.get(letter): 
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx)
        
    while test > 0:
        os.system("cls")
        print(f"¡Adivina la siguiente palabra de {len(target_word)} letras!" + "\n" )
        for element in transf_to_underscore:
            print(element + "  ", end="")
        print(f"\n\nTienes {test} oportunidades\n\n")
        
        # Ask the letters to the gamer.
        letter = input("Digita una letra: ").upper()
        if letter in letter_index_dict:
            for idx in letter_index_dict[letter]:
                transf_to_underscore[idx] = letter
        else:
            test -= 1

        if test == 0:
            os.system("cls")
            print(f"\nLo siento no adivinaste, la palabra era {target_word} \n")
        elif "_" not in transf_to_underscore: 
            os.system("cls")
            print(f"\n¡Ganaste! Adivinaste la palabra {target_word}\n")
            break
if __name__ == "__main__":
    game()
