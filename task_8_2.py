# # import line as line
#
# print(f'*'* 30, 'Вариант_1', '*'* 35)
#
# import re
#
# RE_NAME = re.compile(r'([\w\.\+\:\/]+)')
#
# def pars_log(str_line):
#     log_list = RE_NAME.findall(str_line)
#     print((log_list[0], log_list[1], log_list[2], log_list[3], log_list[4], log_list[5], log_list[6], log_list[7]))
#     print(log_list)
#
#
# with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
#     for line in f:
#         pars_log(line)
# print(f'*'* 30, 'Вариант_2', '*'* 35)

import re

check = re.compile(r'^(\b.+\b).*\[(.+)].*\"([A-Z]+) +(/.+?)\s.*?\" (\d+) (\d+) .*$|^$')

with open("nginx_logs.txt", encoding="utf-8") as f:
    for line in f:
        # print(re.findall(check, line))
        print(*re.findall(check, line))
