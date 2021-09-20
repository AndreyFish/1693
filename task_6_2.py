import collections

with open("pars_logs.txt", "r", encoding="utf-8") as  f:
    my_dict = collections.Counter()

    for i in f:
        i = i.split()[0]
        my_dict[i] +=1

        ip, count = my_dict.most_common(1)[0][0], my_dict.most_common(1)[0][1]
        print(f"Spammer {ip} - {count} times")
