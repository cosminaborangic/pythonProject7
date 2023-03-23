
class Produs:
    def __init__(self, id, denumire, pret):
        """
        Initializam clasa Produs
        :param id: Id ul produsului(tip int)
        :param denumire: Denumirea produsului(tip str)
        :param pret: Pretul produsului(tip int)
        """
        self.__id=id
        self.__denumire=denumire
        self.__pret=pret
    def getId(self):
        """
        :return: Id ul Produsului
        """
        return self.__id
    def getDenumire(self):
        """

        :return: Denumirea Produsului
        """
        return self.__denumire
    def getPret(self):
        """

        :return: Pretul Produsului
        """
        return self.__pret
    def setId(self, value):
        self.__id=value
    def setDenumire(self, value):
        self.__denumire=value
    def setpret(self, value):
        self.__pret=value
    def __eq__(self,other):
        """
        Verifica egalitatea intre doua produse
        :param other: Celalalt parametru fata de care verificam egalitatea(tip Produs)
        :return: functia returneaza un bool, pentru adevarat True, pentru fal False
        """
        if self.__id==other.getId():
            return True
        return False
    def __str__(self):
        return "ID-ul produsului: "+str(self.__id)+" Denumirea produsului: "+self.__denumire+" Pretul produsului: "+self.__pret


def test_getters():

        p = Produs(127, 'sarmale', 8)
        assert (p.getId() == 127)
        assert (p.getDenumire() == 'sarmale')
        assert (p.getPret() == 8)
        p = Produs(281, 'mamaliga', 3)
        assert (p.getId() == 281)
        assert (p.getDenumire() == 'mamaliga')
        assert (p.getPret() == 3)
        p = Produs(2816, 'ciocolata', 46)
        assert (p.getId() == 2816)
        assert (p.getDenumire() == 'ciocolata')
        assert (p.getPret() == 46)
        p = Produs(2873, 'caramele', 10)
        assert (p.getId() == 2873)
        assert (p.getDenumire() == 'caramele')
        assert (p.getPret() == 10)
        p = Produs(32487, 'ardei', 10)
        assert (p.getId() == 32487)
        assert (p.getDenumire() == 'ardei')
        assert (p.getPret() == 10)
        p = Produs(2816, 'ciocolata', 46)
        assert (p.getId() == 2816)
        assert (p.getDenumire() == 'ciocolata')
        assert (p.getPret() == 46)
        p = Produs(2873, 'caramele', 10)
        assert (p.getId() == 2873)
        assert (p.getDenumire() == 'caramele')
        assert (p.getPret() == 10)
        p = Produs(32487, 'ardei', 10)
        assert (p.getId() == 32487)
        assert (p.getDenumire() == 'ardei')
        assert (p.getPret() == 10)

test_getters()

