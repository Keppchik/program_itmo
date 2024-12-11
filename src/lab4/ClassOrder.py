class Order:
    def __init__(self, data):
        self.number = data[0]
        self.products = data[1]
        self.compacted_products = {}
        self.customer = data[2]
        self.adress = data[3]
        self.phone = data[4]
        self.priority = data[5].strip()
        self.errors = []

        self.is_valid()
        self.compact_products()

    def is_valid(self):
        phone_split = self.phone.split("-")
        if len(phone_split) < 5 or self.phone[0] != "+" or len(phone_split[0]) != 2 or len(phone_split[1]) != 3 or len(
                phone_split[2]) != 3 or len(phone_split[3]) != 2 or len(phone_split[4]) != 2:
            if self.phone == "":
                self.errors.append((2, "no data"))
            else:
                self.errors.append((2, self.phone))

        if len(self.adress.split()) < 4:
            if self.adress == "":
                self.errors.append((1, "no data"))
            else:
                self.errors.append((1, self.adress))

    def compact_products(self):
        products_split = self.products.split(", ")
        for product in products_split:
            if product not in self.compacted_products:
                self.compacted_products[product] = 1
            else:
                self.compacted_products[product] += 1

    def __str__(self):
        return f"{self.number}, {self.products},{self.customer}, {self.adress}, {self.phone}, {self.priority}{self.errors}"
