import math 

X0 = int (input ("Votre initiale ? (X) "))
Y0 = int (input ("Votre initiale ? (Y) "))
X1 = int (input ("Votre finale ? (X) "))
Y1 = int (input ("Votre finale ? (Y) "))
# calcul_cap
diff_x = X1 - X0
diff_y = Y1 - Y0


gauche = diff_x < 0
haut = diff_y > 0

distance_trajet = math.sqrt((X0-X1) ** 2 + (Y0-Y1) ** 2)
hypo = distance_trajet
cap = math.degrees(math.acos(abs(diff_x) / abs(hypo)))

if gauche and haut:
    cap += 270
elif not gauche and not haut:
    cap += 90
elif not gauche and haut:
    cap = 90 - cap
elif gauche and not haut:
    cap = 270 - cap

print("Le cap est le suivant : ", cap, "deg")