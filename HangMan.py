import random
import os

def word_select():
    # This function will select a word from the list.
    with open("./secrets_words.txt","r", encoding="UTF-8") as w:
        target_word = random.choice(list(w)).strip().upper()
        # Aún esta el problema de quitar las tildes.

        letter_index_dict = {}
        for idx, letter in enumerate(target_word):
            if not letter_index_dict.get(letter): 
                letter_index_dict[letter] = []
            letter_index_dict[letter].append(idx)
    
        while True:
            # Transform the word in undersores, like hidden!.
            transf_to_underscore = ["_"] * len(target_word)
            os.system("cls")
            print(f"¡Adivina la siguiente palabra de {len(target_word)} letras!")         
            print("\n")
            for element in transf_to_underscore:
                print(element + "  ", end="")
            print("\n")
            print(target_word)

            # Ask the letters to the gamer.
            letter = input("Digita una letra: ").upper()
            assert letter.isalpha(), "Solo puedes ingresar letras"

            if letter in letter_index_dict:
                for idx in letter_index_dict[letter]:
                    transf_to_underscore[idx] = letter
                    print(transf_to_underscore)
                else:
                    continue


            if "_" not in transf_to_underscore:
                os.system("cls")
                print("¡Ganaste! La palabra era", target_word)
            break



if __name__=="__main__":
    word_select()
     
