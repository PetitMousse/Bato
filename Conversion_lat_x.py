

#// ---------------- DEBUT EN TETE -------------------------------------//
// NOM : Conversion lat/long en cartesien                               //
// ALGO - REFERENCES :                                                  //
//                                                                      //
// AUTEURS : Q.forest                                                   //
// VERSION :    1.0         P.SCHOTT              novembre 2020         // 
//                                                                      //
// HISTORIQUE : Aucun                                                   //
//                                                                      //
// ENTREES :  Long/lat valeurs position initiale                        //
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

def convertion1(long, lat):

    from pyproj import Proj, transform

    inProj = Proj(init='epsg:3857')
    outProj = Proj(init='epsg:4326')
    x1,y1 = long, lat
    x2,y2 = transform(inProj,outProj,x1,y1)
    print x2,y2
    return convertion1()
    
