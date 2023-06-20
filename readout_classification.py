import pandas as pd
import re

df = pd.read_excel('C:/Users/andlabkbs/Desktop/meddataset/202cases/brain_hemo_214.xlsx', skiprows=5, usecols=['readout'])
# df['readout'] = df['readout'].str.replace(pat=r'[^\w]', repl=r' ', regex=True)
df = df.dropna()
df.reset_index(drop=False, inplace=True)
# print(df['readout'][0])

wordlist = []
wordoutlist = ['ct']

df2 = pd.read_excel('C:/Users/andlabkbs/Desktop/meddataset/term.xlsx', usecols=['hemo'])
df2['hemo'] = df2['hemo'].str.replace(pat=r'[^\w]', repl=r' ', regex=True)
df2 = df2.dropna()
df2.reset_index(drop=False, inplace=True)

df3 = pd.read_excel('C:/Users/andlabkbs/Desktop/meddataset/term.xlsx', usecols=['Key Brain Terms Glossary'])
df3['Key Brain Terms Glossary'] = df3['Key Brain Terms Glossary'].str.replace(pat=r'[^\w]', repl=r' ', regex=True)
df3 = df3.dropna()
df3.reset_index(drop=False, inplace=True)

df4 = pd.read_excel('C:/Users/andlabkbs/Desktop/meddataset/term.xlsx', usecols=['paterehab'])
df4['paterehab'] = df4['paterehab'].str.replace(pat=r'[^\w]', repl=r' ', regex=True)
df4 = df4.dropna()
df4.reset_index(drop=False, inplace=True)

for i in range(len(df2)):
    x = df2['hemo'][i].split()
    for j in range(len(x)):
        if x[j] not in wordlist:
            wordlist.append(x[j].lower())

# for i in range(len(df3)):
#     x = df3['Key Brain Terms Glossary'][i].split()
#     for j in range(len(x)):
#         if x[j] not in wordlist:
#             wordlist.append(x[j])

for i in range(len(df4)):
    x = df4['paterehab'][i].split()
    for j in range(len(x)):
        if x[j] not in wordlist:
            wordlist.append(x[j].lower())

# print(wordlist)


strlist = []
tflist = []

def check_date_format(input_date):
	regex = r'\d{4}-\d{2}-\d{2}'
	return  bool(re.findall(regex, input_date))

for i in range(len(df)):
    x = df['readout'][i].splitlines()
    tmplist = []
    for j in range(len(x)):
        num = 0
        if check_date_format(x[j]):
            continue
        no_special_str = re.sub(r'[^\w]', ' ', x[j])
        no_special_str = no_special_str.strip()
        check = 0
        for k in range(len(wordoutlist)):
            if wordoutlist[k] in no_special_str.lower():
                check = 1
        for k in range(len(wordlist)):
            if wordlist[k] in no_special_str.lower():
                num = num + 1
        if len(no_special_str) > 0 and no_special_str[0].isnumeric() :
            no_special_str = no_special_str[1:]
        if len(no_special_str) == 0:
            continue
        strlist.append(no_special_str)
        if num > 0 and check == 0:
            tflist.append(1)
        else:
            tflist.append(0)


# print(strlist, tflist)
#
#
# for i in range(len(strlist)):
#     newstr = ""
#     for j in range(len(strlist[i])):
#         newstr = newstr + strlist[i][j] + "\n"
#     strlist[i] = newstr

idlist = []
for i in range(len(tflist)):
    idlist.append(i)

extracted_str = pd.DataFrame({'id' : idlist, 'str' : strlist, 'tf' : tflist})
# extracted_str['str'] = extracted_str['str'].str.replace(pat=r'[^\w]', repl=r' ', regex=True)
print(extracted_str)
# print(extracted_str['str'])

extracted_str.to_csv('train.csv')

# df7 = pd.read_excel('./sample.xlsx', usecols=['str'])
# print(df7)