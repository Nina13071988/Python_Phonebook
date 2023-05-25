
def storage(): #показать все контакты
    data_file = open("data_file.txt", "a")
    #data = data_file.read().split('\n')
    return data_file
    
def add_contact(contact): #добавить контакт
    return None
    # with open('data_file.txt', 'a',  encoding='utf8') as data_file:
    #     data_file.write(f'{contact}\n')

    #     return contact

def finder(contact): #найти контакт
    return None
    # command = input("Введите данные для поиска пользователя")
    # match command:
    #     case 1:
    #         name_finder = input("Введите ФИО пользователя: ")
    #         for values in data:
    #             if data[values] == name_finder:
    #                 print(data[values])
    #     case 2:
    #         phone_finder = input("Введите ФИО пользователя: ")
    #         for values in data:
    #             if data[values] == phone_finder:
    #                 print(data[values])

# if __name__ == "__main__":
#     storage()