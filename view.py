import model
def greetings():
   return print("Добрый день, уважаемый пользователь!")

def menu():
   print("Далее Вам будет предложен выбор категории спраочника:" '\n'
         '1 - Показать все контакты\n'
         '2 - Добавить контакт\n'
         '3 - Найти контакта\n'
         '4 - Изменить данные контакта\n'
         '5 - Удалить данные контакта\n'
         '6 - Выход')
   
def show_contacts(data): # показать все контакты
    data = open("data_file.txt", "a+")
    file_content = data.read()
    print(file_content)

def success(res): # показать найденный контакт
   return None

def not_success(res): # показать , что контакт не найден/отсутствует
   return None

def ciao():
    print("До свидания!")

def error():
   return print("Упс, что-то пошло не так")

   

# if __name__ == "__main__":
#    greetings()
#    menu()
#    show_contacts()

