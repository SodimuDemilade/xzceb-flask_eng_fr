from translator import english_to_french, french_to_english
test3 = english_to_french("Hello")
print(test3['translations'][0]['translation'])
test4 = french_to_english('Bonjour')
print(test4['translations'][0]['translation'])
test5 = english_to_french("How are you")
print(test5['translations'][0]['translation'])
test6 = french_to_english("je t'aime")
print(test6['translations'][0]['translation'])
test1 = english_to_french()
test2 = french_to_english()