from domain.entities import Produs

class RepositoryProdus:
    def __init__(self,filename):
        """
        Se initializeaza clasa
        :param filename: numele fisierului text(str)
        """
        self.__undo=[]
        self.__lista=[]
        #self.__lista_aux = []
        self.__filename=filename
    def __all_from_file(self):
        """
        :return: Continutul fisierului
        """
        try:
            f=open(self.__filename,'r')
        except IOError:
            return
        lines=f.readlines()
        all_prod=[]
        for line in lines:
            id, denumire, pret=[token.strip() for token in line.split(';')]
            l=Produs(int(id), denumire, int(pret))
            all_prod.append(l)
        f.close()
        return all_prod
    def __save_in_file(self,all_p):
        """
        :param all_p:continutul care se salveaza in fisierul text
        :return: -
        """
        with open(self.__filename,'w') as f:
            for l in all_p:
                l_string=str(l.getId())+';'+str(l.getDenumire())+';'+str(l.getPret())+'\n'
                f.write(l_string)
    def add(self, produs):
        """
        :param produs: produsul adaugat in fisier(tip Produs)
        :return: -
        """
        all_prod=self.__all_from_file()
        for p in all_prod:
            self.__lista.append(p)
        self.__lista.append(produs)
        self.__save_in_file(self.__lista)
    def delete(self,cifra):
        """
        :param cifra: cifra pe care trebuie sa o contina pretul unui Produs ca sa fie sters(int)
        :return: numarul de produse sterse(int)
        """
        self.__undo =self.__all_from_file()
        all_prod = self.__all_from_file()
        contor=0
        for p in all_prod:
            pret=p.getPret()
            while pret>0:
                if pret%10==cifra:
                    all_prod.remove(p)
                    contor=contor+1
                pret=pret//10
        self.__save_in_file(all_prod)
        return contor
    def undo(self):
        """
        Undo la ultimaq operatie
        :return: -
        """
        self.__save_in_file(self.__undo)
    def filtrare(self,text,numar):
        """
        Filtrare
        :param text: textul care trebuie continut in denumire
        :param numar: numarul fata de care pretul trebuie sa fie mai mic
        :return: Lista filtrata
        """
        all_prod = self.__all_from_file()
        if len(text)==0 and numar>-1:
            print("Filtrul aplicat este: produsele mai ieftine decat valoarea "+str(numar)+"\n")
            for p in all_prod:
                if p.getPret()<numar:
                    print("Id-ul produsului: "+str(p.getId())+" Denumirea produsului: "+str(p.getDenumire())+" Pretul produsului: "+str(p.getPret())+'\n')
        if numar==-1 and len(text)>0:
            print("Filtrul aplicat este: produsele care contin in denumire textul dat  "+str(text)+"\n")
            for p in all_prod:
                denumire=p.getDenumire()
                indice=0
                for i in range(0, len(denumire)-1):
                    for j in range (0,len(text)-1):
                         if denumire[i]==text[j]:
                               indice=indice+1
                               break
                if indice>=len(text):
                    print("Id-ul produsului: " + str(p.getId()) + " Denumirea produsului: " + str(
                        p.getDenumire()) + " Pretul produsului: " + str(p.getPret()) + '\n')

        if numar==-1 and len(text)==0:
            print("Nu se aplica niciun filtru"+"\n")
            for p in all_prod:
                print("Id-ul produsului: "+str(p.getId())+" Denumirea produsului: "+str(p.getDenumire())+" Pretul produsului: "+str(p.getPret())+'\n')
        if len(text) >0 and numar >-1:
            print("Filtrul aplicat este: produsele mai ieftine decat valoarea " + str(numar)+"Filtrul aplicat este: produsele care contin in denumire textul dat  "+str(text)+"\n")
            for p in all_prod:
                denumire = p.getDenumire()
                indice = 0
                for i in range(0, len(denumire) - 1):
                    for j in range(0, len(text) - 1):
                        if denumire[i] == text[j]:
                            indice = indice + 1
                            break
                if p.getPret()<numar and indice>=len(text):
                    print("Id-ul produsului: " + str(p.getId()) + " Denumirea produsului: " + str(
                        p.getDenumire()) + " Pretul produsului: " + str(p.getPret()) + '\n')

def test_repo():
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
test_repo()



