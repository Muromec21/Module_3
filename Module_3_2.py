def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    list_ = ['@']
    list_2 = ['.com', '.ru', '.net']
    for i in list_:
        if i not in sender:
            print('Невозможно отправить письмо с адреса <', sender, '> на адрес <', recipient, '>')
            break
        else:
            for j in list_2:
                if j in sender:
                    break
            else:
                print('Невозможно отправить письмо с адреса <', sender, '> на адрес <', recipient, '>')
                break

        for i in list_:
            if i not in recipient:
                print('Невозможно отправить письмо с адреса <', sender, '> на адрес <', recipient, '>')
                break
            else:
                for j in list_2:
                    if j in recipient:
                        break
                else:
                    print('Невозможно отправить письмо с адреса <', sender, '> на адрес <', recipient, '>')
        if sender == recipient:
            print('Нельзя отправить письмо самому себе!')
        else:
            if sender == 'university.help@gmail.com':
                print('Письмо успешно отправлено с адреса <', sender, '> на адрес <', recipient, '>.')
            else:
                print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <', sender, '> на адрес <', recipient, '>.')

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')