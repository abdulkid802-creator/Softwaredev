class Shipping:
    def __init__(self, weight, express=False, international=False):
        self.weight = weight
        self.express = express
        self.international = international
    def is_valid(self):
        return self.weight > 0
    def base_cost(self):
        if self.weight <= 5:
            return 8
        elif self.weight <= 20:
            return 15
        else:
            return 30
    def express_surcharge(self):
        if self.express:
            return 12
        return 0
    def international_surcharge(self):
        if self.international:
            return 20
        return 0
    def total_cost(self):
        if not self.is_valid():
            return None
        total = self.base_cost()
        total += self.express_surcharge()
        total += self.international_surcharge()
        return total
    def description(self):
        if not self.is_valid():
            return "Invalid shipment"
        description = "Standard shipping"
        if self.express:
            description += ", express delivery"
        if self.international:
            description += ", international destination"
        return description
