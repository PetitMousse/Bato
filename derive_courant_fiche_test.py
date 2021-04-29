# IL faut absolument prendre pour se code les valeurs des listes direction [] et vitesse []
import math
direction = []
vitesse = []

print("\nEn vives eaux : \n")

v_0 = int(input("vitesse du courant a -6(=6heures avant la pleine mer"))
vitesse.append(v_0)
d_0 = int(input("direction du courant a -6(=6heures avant la pleine mer"))
direction.append(d_0)

print("\n----------------\n")


v_4 = int(input("vitesse du courant a -2(=2heures avant la pleine mer"))
vitesse.append(v_4)
d_4 = int(input("direction du courant a -2(=2heures avant la pleine mer"))
direction.append(d_4)

print("\n----------------\n")



v_6 = int(input("vitesse du courant a la pleine mer"))
vitesse.append(v_6)
d_6 = int(input("direction du courant a la pleine mer"))
direction.append(d_6)

print("\n----------------\n")

v_8 = int(input("vitesse du courant a 2(=2heures apres la pleine mer"))
vitesse.append(v_8)
d_8 = int(input("direction du courant a 2(=2heures apres la pleine mer"))
direction.append(d_8)

print("\n----------------\n")



v_12 = int(input("vitesse du courant a 6(=6heures apres la pleine mer"))
vitesse.append(v_12)
d_12 = int(input("direction du courant a 6(=6heures apres la pleine mer"))
direction.append(d_12)


print("\n\n\nEn mortes eaux : \n\n")

# EN MORTES EAUX
direction2 = []
vitesse2 = []

d_0_ = int(input("direction du courant a -6(=6heures avant la pleine mer"))
direction2.append(d_0)
v_0_ = int(input("vitesse du courant a -6(=6heures avant la pleine mer"))
vitesse2.append(v_0)

print("\n----------------\n")


v_4_ = int(input("vitesse du courant a -2(=2heures avant la pleine mer"))
vitesse2.append(v_4)
d_4_ = int(input("direction du courant a -2(=2heures avant la pleine mer"))
direction2.append(d_4)

print("\n----------------\n")

v_6_ = int(input("vitesse du courant a la pleine mer"))
vitesse2.append(v_6)
d_6_ = int(input("direction du courant a la pleine mer"))
direction2.append(d_6)

print("\n----------------\n")

v_8_ = int(input("vitesse du courant a 2(=2heures apres la pleine mer"))
vitesse2.append(v_8)
d_8_ = int(input("direction du courant a 2(=2heures apres la pleine mer"))
direction2.append(d_8)

print("\n----------------\n")


print("\n----------------\n")

v_12_ = int(input("vitesse du courant a 6(=6heures apres la pleine mer"))
vitesse2.append(v_12)
d_12_ = int(input("direction du courant a 6(=6heures apres la pleine mer"))
direction2.append(d_12)

x2 = int(input("Quellle est votre position initiale : x"))
y2 = int(input("Quellle est votre position initiale : y"))

xb = int(input("Quellle est votre position finale : x"))
yb = int(input("Quellle est votre position finale : x"))

temps_trajet = int(input("temps de trajet ?"))
heure_maree = int(input("heure marree ?"))

a = 1 

# calcul de la derive en fonction du temps de trajet et de la position du bateau
t = math.ceil(temps_trajet)
t_0 = math.floor(heure_maree)


d = direction[t_0:t_0 + t:]
print (d)
d_2 = sum(d)
derive = (d_2 / t)

v = vitesse[t_0:t_0 + t:]
b = sum(v)
force = (b / t)

x_f = force * math.cos(derive) * t
y_f = force * math.sin(derive) * t
x_f = xb + x_f
y_f = yb + y_f
# calcul des longueurs du triangle
L_d = ((x_f - xb) ** 2 + (y_f - yb) ** 2) ** 1 / 2
L_i = ((xb - x2) ** 2 + (yb - y2) ** 2) ** 1 / 2
L_r = ((x_f - x2) ** 2 + (y_f - y2) ** 2) ** 1 / 2
# angle de derive
A = (-L_d ** 2 + L_r ** 2 + L_i ** 2) / (2 * L_i * L_r)
A = math.radians(A)
A = math.acos(A)
A_derive = math.degrees(A) * a

print (A_derive)