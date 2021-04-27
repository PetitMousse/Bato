#// ---------------- DEBUT EN TETE -------------------------------------//
// NOM : Conversion cartesien en long/lat                               //
// ALGO - REFERENCES :                                                  //
//                                                                      //
// AUTEURS : Q.forest                                                   //
// VERSION :    1.0         P.SCHOTT              novembre 2020         // 
//                                                                      //
// HISTORIQUE : Aucun                                                   //
//                                                                      //
// ENTREES :  (x,y)                                                     //
//                                                                      //
// SORTIES : Position en valeurs cartesiennes                           //
//                                                                      //
// MODIFIEES :                                                          //
//                                                                      //
// LOCALES :                                                            //
//                                                                      //
// FONCTIONS APPELEES : Proj, transform                                 //
//                                                                      //
// ---------------- FIN EN TETE ----------------------------------------//
'''
def convertion2(X, Y):

    from pyproj import Proj, transform

    outProj = Proj(init='epsg:3857')
    inProj = Proj(init='epsg:4326')
    x1, y1 = X, Y
    x2, y2 = transform(inProj, outProj, x1, y1)
    print x2, y2
    return convertion2()
