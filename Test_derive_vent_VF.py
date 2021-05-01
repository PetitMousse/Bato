import math

derive_du_vent_vitesse = float (input("Valeur de la vitesse du vent ? "))* 1.852
derivee_du_vent = int (input("Valeur de l'angle d'orientation du vent ? "))
temps_h = int(input("Temps de trajet :"))

x0 = float(input("Position initiale (x) en km"))
y0 = float(input("Position initiale (y) en km"))

x1 = float(input("Position finale (x) en km"))
y1 = float(input("Position finale (y) en km"))

distance_trajet = math.sqrt((x0-x1) ** 2 + (y0-y1) ** 2)

# calcul_cap
diff_x = x1 - x0
diff_y = y1 - y0
hypo = distance_trajet

gauche = diff_x < 0
haut = diff_y > 0

cap = math.degrees(math.acos(abs(diff_x) / abs(hypo)))

finale_vent = [
    x1 + math.sin(math.radians(derivee_du_vent)) * derive_du_vent_vitesse * temps_h,
    y1 + math.cos(math.radians(derivee_du_vent)) * derive_du_vent_vitesse * temps_h,
]

# calcul cap avec courant 
cap_avec_vent = math.degrees(math.atan(abs(finale_vent[1] - y0)/abs(finale_vent[0] - x0)))

result = cap - cap_avec_vent

if gauche and not haut : 
    resultat = -result
elif not gauche and haut : 
    resultat = - result 
else :
   resultat = result


print ("cap", cap)
print ("cap courant", cap_avec_vent)
print ("La derive en degré dû au vent pour ce trajet est de : ", resultat)
