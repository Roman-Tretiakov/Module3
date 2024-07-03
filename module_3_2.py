def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if ('@' not in recipient or '@' not in sender) or (not recipient.endswith(('.com', '.ru', '.net'))
                                                       and not sender.endswith(('.com', '.ru', '.net'))):
        print(f'Impossible to send email from address: {sender} to address: {recipient}')
        return

    if recipient == sender:
        print('Impossible to send email to yourself!')
        return

    if sender == 'university.help@gmail.com':
        print(f'The email is sent from address: {sender} to address: {recipient} successfully!')
    else:
        print(f'NOT STANDARD SENDER! The email is sent from address: {sender} to address: {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.uk', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
