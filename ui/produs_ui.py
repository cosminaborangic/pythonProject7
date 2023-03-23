from domain.entities import Produs
class ProdusController:
    def __init__(self, repo):
        self.__repo=repo
    def adaugare(self, prod):
        self.__repo.add(prod)
    def stergere(self,cif):
        ct=self.__repo.delete(cif)
        return ct
    def undo_produs(self):
        self.__repo.undo()
    def filtrare_produse(self,text,numar):
        self.__repo.filtrare(text,numar)
class ProdusUi:
    def __init__(self, c):
        self.__c=c
    def __adaugare_produs(self):
        id=input('Introduceti ID-ul produsului: ')
        denumire = input('Introduceti denumirea produsului: ')
        pret=input('Introduceti pretul produsului: ')
        p=Produs(id,denumire,pret)
        self.__c.adaugare(p)
    def __stergere_produs(self):
        cif=input('Introduceti cifra: ')
        ct=self.__c.stergere(int(cif))
        print("Au fost sterse "+str(ct)+" produse din fisier")
    def __undo_op_stergere(self):
        self.__c.undo_produs()
    def __filtrare_utiliz(self):
        text=input("Introduceti un text:")
        numar=input("Introduceti un numar: ")
        self.__c.filtrare_produse(str(text),int(numar))
    def run(self):
        while True:
            cmd=input("Introduceti comanda (comenzi disponibile: adaugare, stergere, undo, filtrare): ")
            cmd=cmd.lower().strip()
            if cmd=="adaugare":
                self.__adaugare_produs()
            if cmd=="stergere":
                self.__stergere_produs()
            if cmd=="undo":
                self.__undo_op_stergere()
            if cmd=="filtrare":
                self.__filtrare_utiliz()
def test_controller():
    p = Produs(127, 'sarmale', 8)
    assert (p.getId() == 127)
    assert (p.getDenumire() == 'sarmale')
    assert (p.getPret() == 8)
    p= Produs (281, 'mamaliga',3)
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
test_controller()

