def delete(self, id):
    self.__undo = self.__load_from_file()
    all = self.__load_from_file()
    for l in all:
        if l.getstudentid() == id:
            all.remove(l)
    self.__save_to_file(all)

    return all


def undo(self):
    self.__save_to_file(self.__undo)

