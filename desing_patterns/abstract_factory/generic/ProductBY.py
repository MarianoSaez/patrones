from ProductB import ProductB


class ProductBY(ProductB):
    def someMethodB(self) -> None:
        print(f"[ {type(self)} ]: Soy una clase concreta de ProductB")