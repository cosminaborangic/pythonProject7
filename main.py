from repo.repository_produs import RepositoryProdus
from ui.produs_ui import ProdusController, ProdusUi
repo_file_prod=RepositoryProdus('data/produse.txt')
c=ProdusController(repo_file_prod)
ui=ProdusUi(c)
ui.run()

