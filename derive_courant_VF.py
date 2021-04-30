def derive_courant(derive_du_courant_vitesse, direction_du_courant, finale, init):
     finale_courant = [
        finale[0] - math.sin(math.radians(derive_du_courant_vitesse)) * derivee_du_courant * temps_h,
        finale[1] - math.cos(math.radians(derive_du_courant_vitesse)) * derivee_du_courant * temps_h,
    ]

    cap_init = math.atan((finale[1] - init[1])/(finale[0] - init[0]))
    cap_avec_courant = math.atan((finale_courant[1] - init[1])/(finale_courant[0] - init[0]))

    return math.degrees(cap_avec_courant - cap_init)