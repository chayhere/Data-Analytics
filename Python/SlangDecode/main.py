import pandas

data = pandas.read_csv("lingo.csv")
slang_dict = {row.slang: row.meaning for _,row in data.iterrows()}

smtg = True
while smtg:
    q = input("Yo, what slang you wanna decode: ").lower()
    if q == "bye":
        print("ok bye boi! 👋🏼️")
        smtg = False
    elif q in slang_dict:
        print(f"{q} → {slang_dict[q]}")
    else:
        print("idk too yaa!🥱")
