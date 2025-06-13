from dcel import DCEL, Vertex, HalfEdge, Face 
from dceltest import build_irregular_decagon_dcel 






def triangulation(dcel):
  """ This function would implement the triangulation algorithm
    1. pio dexia kai aristera simeia 
    1.5 koxe poligono stin mesi 
    2. 2 listes pano simia kato simia 
    3. sort os prox to x ola mazi 
    4. stack ta prota 2 simeia 
    5 kali tixei 
            5.1 gia kathe node 
                5.1.1 an to node anikei sto idio list me to ayto toy stack(pano pano stoixeio)
                bazoyme diagonio apo ayto to node 
                
                  Patates : se ola ta stack nodes poy einai orata mesa apo non reflex angles 
                  reflex angles : oxies gonies kato apo 180 mires    
                
                5.1.2 pop ta nodes apo to stack bale ayto poy koitas 
            
            5.2 an to node anoikei stin alli lista 
                5.2.1 bazeis diagonio se ola ta stack nodes pera apo to teleytaio 
        
                      krata to pano poylo ta alla 
    6. epistrefei to dcel me ta nees diagonies 

"""














if __name__ == "__main__":
     thegon  = build_irregular_decagon_dcel(); 
     triangulation(thegon);
     
    