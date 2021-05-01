'''
#// ---------------- DEBUT EN TETE -------------------------------------//
// NOM : tableau des valeurs du courant.                                //
// ALGO - REFERENCES :                                                  //
//                                                                      //
// AUTEURS : A.Bidault & T.Bonnel                                       //
// VERSION :    1.0         P.SCHOTT              décembre 2020         // 
//                                                                      //
// HISTORIQUE : Aucun                                                   //
//                                                                      //
// ENTREES :    temps de trajet; position finale souhaitée(x,y          //
//            position initiale(x,y)                                    //
//                                                                      //
// SORTIES : angle de dérivation induit par le vent.                    //
//                                                                      //
// MODIFIEES :                                                          //
//                                                                      //
// LOCALES :                                                            //
//                                                                      //
// FONCTIONS APPELEES :Trouver_pointB; Conversion_lat_x                 //
//                                                                      //
// ---------------- FIN EN TETE ----------------------------------------//
'''
import math


x2 = int(input("Quelle est la position de depard ? (X)"))
y2 = int(input("Quelle est la position de depard ? (Y)"))
    
xb = int(input("Quelle est la position de fin ? (X)"))
yb = int(input("Quelle est la position de fin ? (Y)"))

    
direction = int(input("Quelle est la direction du vent ? (deg "))
vitesse = float(input('La vitesse du vent ? (noeuds) ')) * 1.852  # km/h

distance_trajet = math.sqrt((x2-xb) ** 2 + (y2-yb) ** 2)

t = distance_trajet / vitesse

a = 1 # mettre 1 pour babord ou -1 pour tribord lors du test !

# calcul de la derive en fonction du temps de trajet et de la position du bateau

derive = direction
force = vitesse

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
derive_vent = math.degrees(A) * a
    
print (derive_vent)
