'''
#// ---------------- DEBUT EN TETE -------------------------------------//
// NOM : tableau des valeurs du courant.                                //
// ALGO - REFERENCES :                                                  //
//                                                                      //
// AUTEURS : A.Bidault                                                  //
// VERSION :    1.0         P.SCHOTT              décembre 2020         // 
//                                                                      //
// HISTORIQUE : Aucun                                                   //
//                                                                      //
// ENTREES :  heure de la marée; coefficient marée; temps de trajet;    //
//            position initiale(x,y); position finale souhaitée(x,y)    //
//            tableau des valeurs de direction et vitesse du courant    //
// SORTIES : angle de dérivation induit par le courant                  //
//                                                                      //
// MODIFIEES :                                                          //
//                                                                      //
// LOCALES :                                                            //
//                                                                      //
// FONCTIONS APPELEES :Trouver_pointB; Conversion_lat_x                 //
//                                                                      //
// ---------------- FIN EN TETE ----------------------------------------//
'''

# IL faut absolument prendre pour se code les valeurs des listes direction [] et vitesse []
import math

def derive_courant(temps_trajet, babord, heure_maree, init, finale_souhaitee, direction, vitesse):  # x2 y2 = initiale
    # rentrer les differentes valeurs de direction et de vitesse du courants en fonction de la position
    # EN VIVES EAUX

    x2 = init[0]
    y2 = init[1]

    xb = finale_souhaitee[0]
    yb = finale_souhaitee[1]

    a = 1 if babord else -1

    # calcul de la derive en fonction du temps de trajet et de la position du bateau
    t = math.ceil(temps_trajet)
    t_0 = math.floor(heure_maree)


    d = direction[t_0:t_0 + t:]
    a = sum(d)
    derive = (a / t)

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

    return A_derive
