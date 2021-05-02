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

def derive_vent (derive_du_vent_vitesse, direction_du_vent, finale, init, temps_h):

    finale_vent = [
        finale[0] - math.sin(math.radians(direction_du_vent)) * derive_du_vent_vitesse * temps_h,
        finale[1] - math.cos(math.radians(direction_du_vent)) * derive_du_vent_vitesse * temps_h,
    ]
    
    distance_trajet = math.sqrt((init[0]-finale[0]) ** 2 + (init[1]-finale[1]) ** 2)

    # calcul_cap
    diff_x = finale[0] - init[0]
    diff_y = finale[1] - init[1]
    hypo = distance_trajet

    gauche = diff_x < 0
    haut = diff_y > 0

    cap = math.degrees(math.acos(abs(diff_x) / abs(hypo)))


    # calcul cap avec vent 
    cap_avec_vent = math.degrees(math.atan(abs(finale_vent[1] - init[1])/abs(finale_vent[0] - init[0])))

    result = cap - cap_avec_vent

    if gauche and not haut : 
        resultat = - result
    elif not gauche and haut : 
        resultat = - result 
    else :
        resultat = result
        
    return resultat
