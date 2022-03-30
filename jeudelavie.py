from random import randint
import time

class Cellule () :
    """Création de la classe cellule"""
    def __init__ (self) : #initialisation de la classe
        self.actuel = False
        self.futur = False
        self.celvoisine = []
        
    def est_vivant (self) : 
        """test si la celluleest vivante est vivante"""
        if self.actuel == False :
            return False
        return True
    
    def set_voisins (self, l) : 
        """définis les voisins de la cellule"""
        self.celvoisine.append (l)
        
    def get_voisins_ce (self) : 
        """retourne les voisins de la cellule"""
        return self.celvoisine
    
    def naitre (self) : 
        """Definis l'etat futur de la cellule comme True"""
        self.futur = True
        
    def mourir (self) : 
        """Definis l'etat futur de la cellule comme False"""
        self.futur = False
        
    def basculer (self) : 
        """Bascule l'état futur à l'état actuel"""
        self.actuel = self.futur

    #def aff (self) : #__str__ de base
     #   s = ""
      #  if self.actuel == False :
       #     s = "-"
       # else :
        #    s = 'X'
        #s = s + "#" + str( len( self.celvoisine) )
        #return s"""

    def __str__ (self) :
        """Affiche à l'écran l'état de la cellule"""
        if self.actuel == False :
            return '-'
        else :
            return "X"
    
    def calcul_etat_futur (self) : 
        """Calcule l'état futur d'une cellule"""
        vivant = 0
        for i in range (len(self.celvoisine)) :
            if self.celvoisine[i].actuel == True :
                vivant +=1
        if self.actuel == False :
            if vivant == 3 :
                self.futur = True
        elif self.actuel == True :
            if vivant == 2 or vivant == 3 :
                self.futur = True
            else :
                self.futur = False
    
class Grille () :
    """Creation de la classe grille"""
    def __init__(self, largeur, hauteur) :
        self.largeur = largeur
        self.hauteur = hauteur
        matrix = [[Cellule()for i in range(self.largeur)]for j in range (self.hauteur)]
        self.matrix  = matrix         
    
    def get_cellule(self, i, j) :
        """Retourne une cellule de la matrice en fonction de ses coordonées"""
        return self.matrix[i][j]
    
    def get_largeur (self) :
        """"Retourne la largeur de la grille"""
        return self.largeur
    
    def get_hauteur (self) :
        """Retourne la hauteur de la grille"""
        return self.hauteur
    
    def get_voisins_gr (self,x ,y) :
        """Obtiens les voisins d'une cellule de la grille en fonction de ses coordonées"""
        return self.matrix[x][y].get_voisins_ce()

    def aff (self) :
        for x in range (self.get_largeur()) :
            for y in range (self.get_hauteur()) :
                print (str(x) + "." + str(y))
                print ( self.matrix[x][y].aff() )
    
    def affecte_voisins (self) : 
        """Affecte les voisins à toutes les cellules"""
        for x in range (self.get_hauteur()):
            for y in range (self.get_largeur()) :

                lst = [ [x-1, y-1], 
                        [x-1, y] , 
                        [x-1, y+1],
                        [x, y-1],
                        [x, y+1],
                        [x+1, y-1],
                        [x+1, y],
                        [x+1, y+1] ]

                if x == 0 :
                     for i in range (3) :
                         lst[i][0] = self.get_hauteur() -1

                if y == 0 :
                    lst[0][1] = self.get_largeur() - 1
                    lst[3][1] = self.get_largeur() -1
                    lst[5][1] = self.get_largeur() -1

                
                if y == self.get_largeur() - 1 :
                    lst[2][1] = 0
                    lst[4][1] = 0
                    lst[7][1] = 0
                    
                if x == self.get_hauteur() - 1 :
                    lst[5][0] = 0
                    lst[6][0] = 0
                    lst[7][0] = 0
                
                for i in range (len(lst)) :
                    # print(str(x) + "." + str(y) + "-" + str(lst[i][0]) + "-" + str(lst[i][1])) 
                    self.get_cellule(x, y).set_voisins(self.get_cellule(lst[i][0], lst[i][1]))
    
    def __str__ (self) :
        """Affiche la grille"""
        for i in range (self.get_hauteur()) :
            for j in range (self.get_largeur()) :
                if j != self.get_hauteur() -1 :
                    print (self.matrix[i][j], end = "")

                else :
                    print (self.matrix[i][j])
        return ""

    def alea (self) :
        """Definis aléatoirement les cellules vivantes"""
        nb_h = randint (0, self.get_hauteur()-1)
        nb_l = randint(0, self.get_largeur()-1)
        if self.get_cellule(nb_h, nb_l).actuel == True :
            self.alea()
        else :
            self.get_cellule(nb_h, nb_l).actuel = True

    def remplir_alea (self, pourcen) :
        """Calcul le nombre de cellules vivantes"""
        nb_cel = self.get_largeur()* self.get_hauteur()
        calcul_vie = round(nb_cel * (pourcen/100))
        for i in range (calcul_vie) :
            self.alea()

    def jeu (self) :
        """Calcule tout les états futur et bascule tout les états futur en état actuel"""
        for i in range (self.get_hauteur()) :
            for j in range (self.get_largeur()) :
                self.matrix[i][j].calcul_etat_futur()
         
        for i in range (self.get_hauteur()) :
            for j in range (self.get_largeur()) :                   
                self.matrix[i][j].basculer()
    
    def actualise (self, grille) :
        """actualise la grille"""
        print (grille)
        


                            
if __name__ == '__main__':      
    """Execute le jeu si ce programme est lancé dans le terminal"""    
    pourcentage = int(input("Combien souhaitez vous en pourcentage de cellules vivantes ? : "))  
    f = Grille(20,20) #premier nombre largeur (x), hauteur = longueur (y)
    f.affecte_voisins()
    f.remplir_alea(pourcentage)
    print (f)
    while True :
        f.jeu()
        f.actualise(f)
        time.sleep(1)
        print("\u001B[H\u001B[J")

