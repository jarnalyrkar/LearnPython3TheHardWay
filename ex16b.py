from sys import argv

script, filename = argv

target = open(filename, 'w')

target.write("""
Dette er tekst som skal dukke opp
i et tekstdokument ved navn som 
man oppgir i et kommandovindu.
""")

target = open(filename)
print(target.read())

target.close()

