
'''cette fonction sert a détecter un palindrome'''
def ispalindrome(p):
    '''fonction prend en argument une chaine de caractère et nous renvoie true or fase'''
    i = ''
    for k in p[::-1]:
        i+=k
    if i == p:
        return True
    return False

#### Fonction principale


def main():
    '''vos appels à la fonction secondaire ici'''
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()