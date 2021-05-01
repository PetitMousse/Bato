def derive_courant(derive_du_courant_vitesse, direction_du_courant, finale, init):
     finale_courant = [
        finale[0] - math.sin(math.radians(derive_du_courant_vitesse)) * derivee_du_courant * temps_h,
        finale[1] - math.cos(math.radians(derive_du_courant_vitesse)) * derivee_du_courant * temps_h,
    ]
    
    distance_trajet = math.sqrt((init[0]-finale[0]) ** 2 + (init[1]-finale[1]) ** 2)

    # calcul_cap
    diff_x = finale[0] - init[0]
    diff_y = finale[1] - init[1]
    hypo = distance_trajet

    gauche = diff_x < 0
    haut = diff_y > 0

    cap = math.degrees(math.acos(abs(diff_x) / abs(hypo)))

    finale_courant = [
        x1 + math.sin(math.radians(derivee_du_courant)) * derive_du_courant_vitesse * temps_h,
        y1 + math.cos(math.radians(derivee_du_courant)) * derive_du_courant_vitesse * temps_h,
    ]

    # calcul cap avec courant 
    cap_avec_courant = math.degrees(math.atan(abs(finale_courant[1] - init[1])/abs(finale_courant[0] - init[0])))

    result = cap - cap_avec_courant

    if gauche and not haut : 
        resultat = - result
    elif not gauche and haut : 
        resultat = - result 
    else :
        resultat = result

    return resultat