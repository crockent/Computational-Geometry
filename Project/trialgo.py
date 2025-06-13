from dcel import DCEL, Vertex, HalfEdge, Face 
from dceltest import build_irregular_decagon_dcel 




def print_first_and_last_vertex_by_x(self):
        if not self.vertices:
            return None
        sorted_vertices = sorted(self.vertices, key=lambda v: v.point.x)
        last = sorted_vertices[-1].point
        first = sorted_vertices[0].point
        
        
        return first, last 

def split_vertices_by_median_y(self):
        if not self.vertices:
            return [], []
        points = [v.point for v in self.vertices]
        n = len(points)
        ys = [p.y for p in points]

        def quickselect(arr, k):
            if len(arr) == 1:
                return arr[0]
            pivot = random.choice(arr)
            lows = [el for el in arr if el < pivot]
            highs = [el for el in arr if el > pivot]
            pivots = [el for el in arr if el == pivot]
            if k < len(lows):
                return quickselect(lows, k)
            elif k < len(lows) + len(pivots):
                return pivots[0]
            else:
                return quickselect(highs, k - len(lows) - len(pivots))

        median_index = n // 2
        median_y = quickselect(ys, median_index)

        upper = [p for p in points if p.y > median_y]
        lower = [p for p in points if p.y <= median_y]
        return upper, lower

""" This function would implement the triangulation algorithm
    1. pio dexia kai aristera simeia ( tik )
    
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







def triangulation(dcel):
    last,first = print_first_and_last_vertex_by_x(dcel) 
    print(f"First vertex by x: ({first.x}, {first.y})")
    print(f"Last vertex by x: ({last.x}, {last.y})")










if __name__ == "__main__":
     thegon  = build_irregular_decagon_dcel(); 
     triangulation(thegon);
     
    