# // ---------------- DEBUT EN TETE --------------------------------------//
# // NOM :Trouver_point B           PRINCIPAL_GUI_BATEAUX                 //
# // ALGO - REFERENCES :                                                  //
# //                                                                      //
# // AUTEURS : Q.delaforesdivonne                                         //
# // VERSION :    1.0         P.SCHOTT              novembre 2020         //
# //                  Création en Scilab d'après le programme de mélanges //
# // HISTORIQUE : Aucun                                                   //
# //                                                                      //
# // ENTREES : Position, Vitesse, Cap                                     //
# //                                                                      //
# // SORTIES : Position finale lat/long                                   //
# //                                                                      //
# // MODIFIEES :                                                          //
# //                                                                      //
# // LOCALES :                                                            //
# //                                                                      //
# // FONCTIONS APPELEES : math, cos, sin, degrees, radians,               //
# //                                                                      //
# // ----------------------- FIN EN TETE ---------------------------------//

def trouver_pointB(latitude_1, longitude_1, distance, cap_compas):
    import math

    # variable en float
    lat_1_d = float(latitude_1)
    long_1_d = float(longitude_1)
    d = float(distance)
    a_d = float(cap_compas)

    # conversion en radian
    a = math.radians(a_d)
    long_1 = math.radians(long_1_d)
    lat_1 = math.radians(lat_1_d)

    # Valeur du rayon de la terre
    r = 6371

    # Boucle pour que cos et sin de A prennent bien la valeur de 0 pour les multiples de pi
    c = math.cos(a)
    s = math.sin(a)
    if math.cos(a) - 0.0000001 < 0:
        c = 0
    if math.sin(a) - 0.0000001 < 0:
        s = 0

    # Calcule des coordonnées
    lat_2 = math.asin(math.sin(lat_1) * math.cos(d / r) + math.cos(lat_1) * math.sin(d / r) * c)
    long_2 = long_1 + math.atan2(s * math.sin(d / r) * math.cos(lat_1), math.cos(d / r) -
                                 math.sin(lat_1) * math.sin(lat_2))

    # On repasse en degré pour els coordonnées
    lat_2 = math.degrees(lat_2)
    long_2 = math.degrees(long_2)

    return lat_2, long_2
