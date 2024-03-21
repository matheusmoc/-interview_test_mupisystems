
class Counter:
    def __init__(self, dict) -> list:
        self.dicionario = dict


    def online_list(self):
        names_online = []
        for name, status in self.dicionario.items():
            if status == "online":
                names_online.append(name)
        return names_online

meu_dict = {
    "Paulo": "online",
    "Thiago": "offline",
    "Roberta": "online"
}

counter = Counter(meu_dict)

""" list persons online"""

online_persons = counter.online_list()
print(f"Total de pessoas: {len(online_persons)}")
print(f"Pessoas online: {', '.join(online_persons)}")

class Merges:
    def zip_merge(self, letter, num):
        result = []
        for i in range(min(len(letter), len(num))):
            result.append((letter[i], num[i]))
        return result


def run_merge(num_list, letter_list):
    merge_instance = Merges()
    result_merge = merge_instance.zip_merge(num_list, letter_list)
    return result_merge 


input_list1 = [0, 1, 2, 3] 
input_list2 = ["A", "B", "C", "D"]
print(run_merge(input_list1, input_list2))



class Conversor:
    def __init__(self, list: list) -> None:
        self.list = list
    
    def __str__(self) -> str:
        return str(list(str(num) for num in self.list))
    
obj = Conversor([0, 1, 2])
print(obj)

def minha_funcao(*args):
    return len(args)
print(minha_funcao())         
print(minha_funcao(0, 1, 2, 3)) 



def interpreter_list(lista_de_listas):
    return [item for sublist in lista_de_listas for item in sublist]

print(interpreter_list([[1, 2],[3, 4],[5, 6, 7]]))


def swapper_list(words):
    """ primeira operação com words separando as palavrar em listas separadas e em seguida outro for separando as letras das palavras"""
    return [[item for item in word] for word in words]

print(swapper_list(['mupi', 'python', 'website']))


def merge_lists_to_dict(produtos: str, cores: str):
    return {produto: cor for produto, cor in zip(produtos, cores)}

print(merge_lists_to_dict(['banana', 'uva', 'kiwi'],  ['amarela', 'verde', 'marrom']))