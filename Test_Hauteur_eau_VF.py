h_m = float(input("Quelle est la valeur de la haute mer (mètre) ?"))
b_m = float(input("Celle de la basse mer (mètre) ? "))
t_debut = int(input("A quelle heure l'eau commence t elle à monter ?"))
t_debut2 = int(input("minutes ?"))
t_fin = int(input("À quelle heure est-t-elle terminée ?"))
t_fin2 = int(input("Minutes ?"))
t_heure = int(input("A quelle heure voulez vous connaitre la hauteur de l'eau ?"))
t_min = int(input("minutes ?"))

t_marree = (t_fin-t_debut)*60 + (t_fin2-t_debut2)
t_marree_marnage = round(t_marree / 6)
marnage = (h_m - b_m) / 12
t_minute = t_debut * 60 + t_debut2
t = t_heure * 60 + t_min

A = {1 * i for i in range(t_minute, t_minute + t_marree_marnage -1)}
B = {1 * j for j in range(t_minute + t_marree_marnage, t_minute + 2 * t_marree_marnage - 1)}
C = {1 * k for k in range(t_minute + t_marree_marnage, t_minute + 3 * t_marree_marnage - 1)}
D = {1 * k for k in range(t_minute + 3 * t_marree_marnage, t_minute + 4 * t_marree_marnage - 1)}
E = {1 * l for l in range(t_minute + 4 * t_marree_marnage, t_minute + 5 * t_marree_marnage - 1)}
F = {1 * m for m in range(t_minute + 5 * t_marree_marnage, t_minute + 6 * t_marree_marnage - 1)}

# cas pour une marrée montante

if t in A:
    t0 = t/60 - t_heure
    hauteur_t = b_m + 1 * marnage * t0
    print("La hauteur de l'eau pour cette heure est de 1:", hauteur_t)

elif t in B:
    t1 = t/60 - t_heure
    hauteur_t = b_m + 1 * marnage + 2 * marnage * t1
    print("La hauteur de l'eau pour cette heure est de 2:", hauteur_t)

elif t in C:
    t2 = t/60 - t_heure
    hauteur_t = b_m + 3 * marnage + 3 * marnage * t2
    print("La hauteur de l'eau pour cette heure est de 3:", hauteur_t)

elif t in D:
    t3 = t/60 - t_heure
    hauteur_t = b_m + 6 * marnage + (3 * marnage * t3)
    print("La hauteur de l'eau pour cette heure est de 4:", hauteur_t)

elif t in E:
    t4 = t/60 - t_heure
    hauteur_t = b_m + 9 * marnage + (2 * marnage * t4)
    print("La hauteur de l'eau pour cette heure est de 5:", hauteur_t)

elif t in F:
    t5 = t/60 - t_heure
    hauteur_t = b_m + 11 * marnage + (1 * marnage * t5)
    print("La hauteur de l'eau pour cette heure est de 6:", hauteur_t)

# cas pour une marree descendante

else:
    t6 = (t - t_fin*60 + t_fin2)/60
    hauteur_t = (6*t6)/(b_m - h_m) + h_m
    print("La hauteur de l'eau pour cette heure est de 7:", hauteur_t)
