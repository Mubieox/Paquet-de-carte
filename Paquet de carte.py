import random


class Carte:
    def __init__(self, c, v):
        """Initialise Couleur (entre 1 à 4), et Valeur (entre 1 à 13)"""
        assert 1<=c<=4,"Couleur invalide !"
        assert 1<=v<=13,"Valeur invalide !"
        self.Couleur = c
        self.Valeur = v
    def getNom(self):
        """Renvoie le nom de la Carte As, 2, ... 10,Valet, Dame, Roi"""
        if ( self.Valeur > 1 and self.Valeur < 11):
            return str( self.Valeur)
        elif self.Valeur == 11:
            return "Valet"
        elif self.Valeur == 12:
            return "Dame"
        elif self.Valeur == 13:
            return "Roi"
        else:
            return "As"
    def getCouleur(self):
        """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle"""
        return ['pique', 'coeur', 'carreau', 'trefle' ][self.Couleur-1]
    def __repr__(self):
        return self.getNom()+" de "+self.getCouleur()
class PaquetDeCarte:
    def __init__(self):
        """ Initialise le contenu du paquet de cartes"""
        self.contenu = []
    def remplir(self):
        """Remplit le paquet avec toutes les cartes"""
        self.contenu=[Carte(c,v) for c in range(1,5) for v in range(1,14)]
        """for c in range(1,5):
            for v in range(1,14):
                self.contenu.append(Carte(c,v))"""
    def getCarteAt(self, pos):
        """Renvoie la Carte qui se trouve à la position donnée"""
        assert 1<=pos<=len(self.contenu),"Position invalide !"
        return self.contenu[pos-1]
    def enlever_carte(self,pos):
        assert 1<=pos<=len(self.contenu),"Position invalide !"
        """for valeur in range(pos,len(self.contenu)):
            temp=self.contenu[valeur-1]
            self.contenu[valeur-1]=self.contenu[valeur]
            self.contenu[valeur]=temp
        self.contenu.pop()"""
        del self.contenu[pos-1]
        """self.contenu.remove(self.contenu[pos-1])"""
    def melanger(self):
        random.shuffle(self.contenu)

unPaquet=PaquetDeCarte()
unPaquet.remplir()
uneCarte=unPaquet.getCarteAt(20)
print(repr(uneCarte))
unPaquet.melanger()
unPaquet.enlever_carte(5)
print(unPaquet.contenu)


