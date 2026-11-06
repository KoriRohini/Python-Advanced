class Computer:

    def __init__(self, cpu, ram, ssd):
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd

    def config(self):
        print("config :", self.cpu, self.ram, self.ssd)

com = Computer("i5", "16GB", "512GB")
com1 = Computer("i7", "32GB", "1TB")
com2 = Computer("Ryzen 7", "16GB", "512GB")

com.config()
com1.config()
com2.config()