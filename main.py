def binary_search(vet,n,k):
    if k not in lista:
        return f'O número {k} não se encontra na lista.'
    l = 0
    h = n
    mid = (l+h)//2
    while True:
        if k == vet[mid]:
            return f'O número {k} se encontra na posição {mid+1} da lista.'
        elif k > vet[mid]:
            l = mid+1
        elif k < vet[mid]:
            h = mid-1
        mid = (l + h) // 2

lista = [3, 6, 8, 12, 14, 17, 25, 29, 31, 36, 42, 47, 53, 55, 62]
lista = sorted(lista) #para que a busca binaria ocorra de forma correta devemos ter certeza que a lista inicial está ordenada.
num = int(input('Digite o número que deseja buscar: '))
print(binary_search(lista, len(lista), num))






















"""from googletrans import Translator

trans = Translator()
trans.translate("The book is on the table", dest="pt").origin
"""