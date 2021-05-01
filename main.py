
from prompt_toolkit.shortcuts import radiolist_dialog
from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit.shortcuts import message_dialog
from hauteur_eau_VF import Hauteur_eau
from trouver_point_b import trouver_pointB
from derive_vent_VF import derive_vent
import math
import utm

from derive_courant_VF import derive_courant


def custom_input(title):
    return input_dialog(
        title='Bateau',
        text=title
    ).run()


result = radiolist_dialog(
    title="Que voulez-vous faire ?",
    values=[
        ("hauteur_eau", "Hauteur d'eau"),
        ("trouver_destination", "Trouver le cap pour une destination"),
    ],
    ok_text="Suivant",
    cancel_text="Fermer"
).run()

if result is "hauteur_eau":
    message_dialog(
        title='Bateau',
        text="Hauteur d'eau (m): "+str(Hauteur_eau(
            h_m=float(custom_input("Hauteur de la marée haute (m)")),
            b_m=float(custom_input("Hauteur de la basse mer (m)")),
            t_debut=[int(x) for x in custom_input(
                "Moment de début de la montée (HH:mm)").split(":")],
            t_fin=[int(x) for x in custom_input(
                "Moment de la fin de la montée (HH:mm)").split(":")],
            t_souhaitee=[int(x) for x in custom_input(
                "Moment souhaité (HH:mm)").split(":")],
        ))
    ).run()
elif result is "trouver_destination":
    radio_resp = radiolist_dialog(
        title="Bateau",
        text="Comment rentrer la position initiale ?",
        values=[
            ("cart", "Carthésien (x, y)"),
            ("pol", "Polaire (lat, long)"),
        ]
    ).run()
    if radio_resp == "cart":
        init = [float(custom_input("Position initiale (x) en km")),
                float(custom_input("Position initiale (y) en km"))]
    else:
        init = utm.from_latlon(float(custom_input("Position initiale (lat) en deg")),
                               float(custom_input("Position initiale (long) en deg")))
        print(init)

    radio_resp = radiolist_dialog(
        title="Bateau",
        text="Comment rentrer la position initiale ?",
        values=[
            ("cart", "Carthésien (x, y)"),
            ("pol", "Polaire (lat, long)"),
        ]
    ).run()
    if radio_resp == "cart":
        finale = [float(custom_input("Position finale (x) en km")),
                  float(custom_input("Position finale (y) en km"))]
    else:
        finale = utm.from_latlon(float(custom_input("Position finale (lat) en deg")),
                                 float(custom_input("Position finale (long) en deg")))

    vitesse = float(custom_input("Vitesse moyenne du bateau (km/h)"))

    distance_trajet = math.sqrt(
        (init[0]-finale[0]) ** 2 + (init[1]-finale[1]) ** 2)
    temps_h = distance_trajet / vitesse

    #Derive du courant

    derive_du_courant_vitesse = float(custom_input("Vitesse du courant (noeuds)")) * 1.852  # km/h
    direction_du_courant = float(custom_input("Direction du courant (deg)"))

    derive_du_courant = derive_courant(derive_du_courant_vitesse, direction_du_courant, finale, init)

    #Fin derive du courant

    derive_du_vent_vitesse = float(custom_input("Vitesse du vent (noeuds)")) * 1.852  # km/h
    direction_du_vent = float(custom_input("Direction du vent (deg)"))


    derive_du_vent = derive_vent(derive_du_vent_vitesse, direction_du_vent, finale, init)


    # calcul_cap
    diff_x = finale[0] - init[0]
    diff_y = finale[1] - init[1]
    hypo = distance_trajet

    gauche = diff_x < 0
    haut = diff_y > 0

    cap = math.degrees(math.acos(abs(diff_x) / abs(hypo)))

    if gauche and haut:
        cap += 270
    elif not gauche and not haut:
        cap += 90
    elif not gauche and haut:
        cap = 90 - cap
    elif gauche and not haut:
        cap = 270 - cap

    somme_derives_cap = derive_du_courant + derive_du_vent + cap

    derive_magnetique = float(custom_input("Derive magnétique (deg)"))
    somme_derives_cap += derive_magnetique

    derive_compas = float(custom_input("Derive compas (deg)"))
    somme_derives_cap += derive_compas

    message_dialog(
        title='Bateau',
        text="Le cap a prendre est : "+str(somme_derives_cap % 360)
    ).run()

print(result)
