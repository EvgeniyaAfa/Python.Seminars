phone_book = []

def open_phone_book():
    with open('phones.txt', 'r', encoding= 'utf-8') as data:
        phone_book = data.readlines()
        return phone_book

def save_phone_book():
    with open('phones.txt', 'w', encoding= 'utf-8') as data:
        for i in phone_book:
            data.write(i)
           

def show_contacts():
    print(phone_book)
    if len(phone_book) == 0:
        print("Откройте файл")
    else:    
            for i in phone_book:
                print(' '.join(i.split(';')))

def add_contacts():
     if len(phone_book) == 0:
          print("Откройте файл")
     else:
         user_info = input("Введите данные: ")
         user_info = ';'.join(user_info.split())
         phone_book.append('\n' + user_info)  

def change_contacts():
    user_info = input("Введите ,что хотите изменить:  ")    
    for  i in range(len(phone_book)):
        if user_info in phone_book[i]:
            print(phone_book[i])
            print(i)
            new_user_info = input("Введите новые данные: ")
            phone_book[i] = phone_book[i].replace(user_info, new_user_info)     
def search_contacts():
    user_info = input("Введите данные, которые хотите найти: ")
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
            print(phone_book[i])

def delete_contacts():
    user_info= input("Введите номер, который надо удалить: ")
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
            print(phone_book[i])
            phone_book.pop(i)
            break
                                
             
phone_book = open_phone_book()
add_contacts()   
save_phone_book() 
show_contacts()
change_contacts()
delete_contacts()