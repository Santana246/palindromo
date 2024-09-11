def palindromo():
    string = str(input("Insira aqui a sua string: "))
    string = string.replace(' ', '')
    string = string.translate(str.maketrans('', '', '␠!"#$%&()*+,-./:;<=>?@[\\]^_`{|}~'))
    string = string.lower()
    stringInv = string[::-1]
    if stringInv == string:
        print(f'A string {string} <-> {stringInv} é um palíndromo.')
        return True
    else:
        print(f'A string {string} <-> {stringInv} NÃO é um palíndromo.')
        return False
    
palindromo()