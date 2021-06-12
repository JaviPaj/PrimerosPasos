import random
import os

def word_select():
    # This function will select a word from the list and make it capital letters & unaccented.
    with open("./secrets_words.txt","r", encoding="UTF-8") as w:
        selected_word = random.choice(list(w)).strip().upper()
        accents = selected_word.maketrans("ÁÉÍÓÚ","AEIOU")
        target_word = selected_word.translate(accents)
        
        letter_index_dict = {}
        for idx, letter in enumerate(target_word):
            if not letter_index_dict.get(letter): 
                letter_index_dict[letter] = []
            letter_index_dict[letter].append(idx)

        # Transform the word in undersores, like hidden!.     
        transf_to_underscore = ["_"] * len(target_word)

        while True:
            os.system("cls")
            print(f"¡Adivina la siguiente palabra de {len(target_word)} letras!")         
            print("\n")
            for element in transf_to_underscore:
                print(element + "  ", end="")
            print("\n")

            # Ask the letters to the gamer.
            letter = input("Digita una letra: ").upper()
            assert letter.isalpha(), "Solo puedes ingresar letras"

            if letter in letter_index_dict:
                for idx in letter_index_dict[letter]:
                    transf_to_underscore[idx] = letter

            if "_" not in transf_to_underscore:
                os.system("cls")
                print("\n")
                print("¡Ganaste! La palabra era", target_word)
                print("\n")
                break



if __name__=="__main__":
    word_select()
     
