'''
База пользоватеелей (login; surname; name; description(1-teacher, 2-student))
База успеваемости (login; subject name; score; data)
База ДЗ (subject name; homework; data)
'''
import data_processing as dp

level_0 = ''
level_1_1 = ''
level_1_2 = ''
db_users = 'HW08_db_users'
db_scores = 'HW08_db_scores'
db_homework = 'HW08_homework'

while level_0 != 2:
    level_0 = input('\nГлавное меню:\n1 - Ввод логина\n2 - Выход\n')
    if level_0 == '1':
        user_login = input('Введите ваш логин: ')
        user_info = dp.read_data(db_users, user_login)
        if user_info[3] == '1':
            while level_1_1 != '3':
                level_1_1 = input('\nМеню преподавателя:\n1 - Установка ДЗ\n2 - Установка оценок\n3 - Выход\n')
                if level_1_1 == '1':
                    dp.write_data(db_homework, 'Введите предмет: ', 'Введите ДЗ: ', '')
                if level_1_1 == '2':
                    dp.write_data(db_scores, 'Введите студента: ', 'Введите предмет: ', 'Введите оценку: ')
                if level_1_1 == '3':
                    break
        elif user_info[3] == '2':
            while level_1_2 != '3':
                level_1_2 = input('\nМеню студента:\n1 - Просмотр ДЗ\n2 - Просмотр успеваемости\n3 - Выход\n')
                if level_1_2 == '1':
                    russian = dp.read_data(db_homework, 'русский язык')
                    technology = dp.read_data(db_homework, 'информатика')
                    print(" - ".join(russian))
                    print(" - ".join(technology))
                if level_1_2 == '2':
                    user_scores = dp.read_data(db_scores, user_login)
                    print(" - ".join(user_scores))
                if level_1_2 == '3':
                    break
    elif level_0 == '2':
        break
