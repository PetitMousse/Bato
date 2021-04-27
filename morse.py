# Dictionaire de la charte du code morse
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ', ':'--..--', '.':'.-.-.-',
   '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-'}


# Fonction pour encoder un script selon la charte du morse
def encrypt(message):
   cipher = ''
   for letter in message:
      if letter != ' ':

         # Là ça regarde dans le dictionnaire le code morse correspondant
         # avec 1 espace pour séparer
         cipher += MORSE_CODE_DICT[letter] + ' '
      else:
         # 1 espace ça signifie une lettre différente
         # 2 espaces ça signnifie un mot différent
         cipher += ' '

   return cipher


# Fonction pour décoder un script du morse à l'anglais
def decrypt(message):

   message += ' '

   decipher = ''
   citext = ''
   for letter in message:

      # check les espaces
      if (letter != ' '):

         # compteur pour garder les espaces
         i = 0

         # stockage du code morse pour un caractère
         citext += letter

         # en cas d'espace
      else:
         # si i = 1 ça indique un nouveau carachtère
         i += 1

         # si i = 2 c'est un nouveau mot
         if i == 2:

            # ajoute un espace pour séparer les mots
            decipher += ' '
         else:

            decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
            citext = ''

   return decipher
