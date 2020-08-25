from googlesearch import search
ask=str(input('Enter(sitename): '))
for i in search(ask,tld='com',num=10, stop=10,pause=2):
 print(i)
