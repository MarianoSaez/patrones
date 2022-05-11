from ProductA import ProductA


class ProductAX(ProductA):
    def someMethodA(self) -> None:
        print(f"[ {type(self)} ]: Soy una clase concreta de ProductA")