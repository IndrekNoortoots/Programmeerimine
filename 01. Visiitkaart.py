nimi = raw_input("Sisesta t2isnimi ")
name = nimi.capitalize()
ametinimi = raw_input("Sisesta oma ametinimi: ")
email = raw_input("Sisesta oma e-mail: ")
tel = raw_input("Sisesta oma telefoni nr: ")
tekst = "Business card"
tyhi = " "
joon = "="
print "|", tekst.center(60, "="), '|' #tyhi rida
print "|", tyhi.center(60, " "), '|'
print "|", nimi.center(60), "|"
print "|", ametinimi.center(60), "|"
print "|", email.center(60), "|"
print "|", tel.center(60), "|"
print "|", tyhi.center(60, " "), '|'#tyhi rida
print "|", joon.center(60, "="), '| \n'
