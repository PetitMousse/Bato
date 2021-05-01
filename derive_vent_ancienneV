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

def derive_vent (temps_trajet, init, finale_souhaitee, vitesse_vent, direction_vent, babord):

    x2 = init[0]
    y2 = init[1]
    
    xb = finale_souhaitee[0]
    yb = finale_souhaitee[1]

    t = temps_trajet
    
    direction = direction_vent
    vitesse = vitesse_vent

    a = 1 if babord else -1

    # calcul de la derive en fonction du temps de trajet et de la position du bateau
    t = temps_trajet
    
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
    
    return derive_vent
