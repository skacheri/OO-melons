"""Classes for melon orders."""
class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""
    def __init__(self, species, qty, country_code=None):
        self.species = species
        self.qty = qty
        self.shipped = False
        if country_code:
            self.country_code = country_code

    def get_total(self):
        """Calculate price, including tax."""
        if self.species == "christmas melon":
            base_price = 5 * 1.5 
        else:
            base_price = 5
        if self.qty < 10 and self.tax == 0.17:
            total = (1 + self.tax) * self.qty * base_price + self.flat_fee
        else:
            total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    """Initialize domestic melon order attributes."""
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    """Initialize melon order attributes."""
    order_type = "international"
    tax = 0.17
    flat_fee = 3

    
    """
    Another way of doing lines 8, 9 and the last parameter in abstract class
    """
    # def __init__(self, species, qty, country_code):
    #     super().__init__(species, qty)
    #     self.country_code = country_code
    

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    passed_inspection = False
    tax = 0

    def mark_inspection(self, passed):
        if passed:
            self.passed_inspection = True
        else:
            self.passed_inspection = False