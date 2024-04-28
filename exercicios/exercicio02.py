#um program que pede uma palavra ao utilizador e substitua todas as vogais pelo caracter ?
word = input("Escreva uma palavra :")
final_word = word.replace("a","?")
final_word = final_word.replace("e","?")
final_word = final_word.replace("i","?")
final_word = final_word.replace("o","?")
final_word = final_word.replace("u","?")

print(word)
print(final_word)