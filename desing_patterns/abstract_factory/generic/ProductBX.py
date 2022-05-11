from ProductB import ProductB


class ProductBX(ProductB):
    def someMethodB(self) -> None:
        print(f"[ {type(self)} ]: Soy una clase concreta de ProductB")