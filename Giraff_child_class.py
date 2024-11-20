class Masai(Giraffe):
    def __init__(self, growth):
        super().__init__(growth)
        self.__endangered = "This is an endangered species."
        self.__species = "Giraffa tippelskirchi"
        self.__patterns = "It has distinctive jagged, irregular leaf-like blotches all over"
        self.__location = "Found in Kenya and Tanzania"
    def species(self):
        print(self.__endangered)
        print(self.__species)
        print(self.__patterns)
    def diet(self):
        self.__diet = "Leaves, twigs, bark, flowers and fruits from over 60 different species of plants."
        print(self.__diet)