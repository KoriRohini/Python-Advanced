class Computer:

    brand = "Telusko"

    @classmethod
    def info(cls):
        print("brand is", cls.brand)

Computer.info()