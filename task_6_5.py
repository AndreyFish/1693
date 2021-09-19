from sys import argv
from itertools import zip_longest

us, h, out_f = argv[1:]

with open(us, "r", encoding="utf-8") as users:
    with open(h, "r", encoding="utf-8") as hobby:
        all_list = zip_longest((" ".join(us.split(",")) for us in users), hobby, fillvalue=None)

        with open(out_f, "w", encoding="utf-8") as f:
            for i in all_list:
                print(f"{str(i[0]).strip()}: {str(i[1]).strip()}", file=f)