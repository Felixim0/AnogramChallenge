#var1, var2 = input("Enter two strings to be compared:\n").split()
#print('Anograms Detected' if ( ''.join(sorted(str((var1.translate(dict.fromkeys(map(ord, '''!@#$.!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''), None))).upper()))) == ( ''.join(sorted(str((var2.translate(dict.fromkeys(map(ord, '''!@#$.!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''), None)))).upper())))) else 'No Anograms Detected')

print('Anograms Detected' if ( ''.join(sorted(str((str(input("Enter a string\n")).translate(dict.fromkeys(map(ord, '''!@#$.!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''), None))).upper()))) == ( ''.join(sorted(str((str(input("Enter a string\n")).translate(dict.fromkeys(map(ord, '''!@#$.!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'''), None)))).upper())))) else 'No Anograms Detected')
