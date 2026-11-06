class Computer:

    @staticmethod
    def gb_to_bytes(gb):
        return gb * (1024 ** 3)

print(Computer.gb_to_bytes(16))
