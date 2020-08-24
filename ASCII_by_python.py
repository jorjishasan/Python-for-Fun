#to import in shell : pip3 install pyfiglet
import pyfiglet
inp= str(input('Enter: '))
result=pyfiglet.figlet_format(inp)
print(result)