
from prompt_toolkit.shortcuts import radiolist_dialog
from prompt_toolkit.shortcuts import input_dialog
from prompt_toolkit.shortcuts import message_dialog
from hauteur_eau_VF import Hauteur_eau
from trouver_point_b import trouver_pointB
from tableau_du_courant import tableau_courant
from derive_courant import derive_courant
from derive_vent import derive_vent
import math
import utm


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

    vitesse = float(custom_input("Vitesse moyen du bateau (km/h)"))

    distance_trajet = math.sqrt(
        (init[0]-finale[0]) ** 2 + (init[1]-finale[1]) ** 2)
    temps_h = distance_trajet / vitesse

    directions_vitesses = tableau_courant()

    while True:
        heure_maree = float(custom_input("Heure de la marée (HH)"))

        if heure_maree > 12:
            print("Mauvaise heure")
        else:
            break

    coef_maree = float(custom_input("Coefficient de la marée"))

    while True:
        babord = custom_input("Le courant va-t-il vers babord ? (O/N)").lower()
        if babord == "o" or babord == "n":
            babord = babord == "o"
            break
        else:
            print("Mauvaise réponse, merci de répondre O ou N")

    vitesse = directions_vitesses[2 if coef_maree > 70 else 3]
    direction = directions_vitesses[0 if coef_maree > 70 else 1]

    derive_du_courant = derive_courant(
        temps_h, babord, heure_maree, init, finale, direction, vitesse)

    vitesse_vent = float(custom_input("Vitesse du vent (km/h)"))
    direction_vent = float(custom_input("Direction du vent (deg)"))

    while True:
        babord = custom_input("Le vent va-t-il vers babord ? (O/N)").lower()
        if babord == "o" or babord == "n":
            babord = babord == "o"
            break
        else:
            print("Mauvaise réponse, merci de répondre O ou N")

    derive_du_vent = derive_vent(
        temps_h, init, finale, vitesse_vent, direction_vent, babord)

    # calcul_cap
    diff_x = finale[0] - init[0]
    diff_y = finale[1] - init[1]
    hypo = distance_trajet

    gauche = diff_x < 0
    haut = diff_y > 0

    cap = math.acos(abs(diff_x) / abs(hypo))

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
        text="Le cap a prendre est: "+str(somme_derives_cap % 360)
    ).run()

print(result)
