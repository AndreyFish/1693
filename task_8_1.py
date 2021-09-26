

import re


def email_parse(email_adress):
    re_email = re.compile(r'(?P<username>([\w]+))@(?P<domain>[^&]+\.\w+)', re.IGNORECASE)
    if not  re_email.match(email_adress):
        raise ValueError(f'wrong email: {email_adress}')
    print(re_email.match(email_adress).groupdict())


for i in ['someone@geekbrains.ru', 'some&one@geekbrainsru', 'someone@geekbrainsru']:
    try:
        email_parse(i)
    except ValueError as err:
        print(err)