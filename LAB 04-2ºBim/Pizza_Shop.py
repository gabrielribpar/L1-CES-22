
class PizzaComponent:
    """Componentes da Pizza"""
    def getDescription(self):
        return self.__class__.__name__

    def getTotalCost(self):
        return self.__class__.cost


class Platter(PizzaComponent):
    """Travessa para montar a Pizza"""
    cost = 0.0

class Decorator(PizzaComponent):
    """Decorador"""
    def __init__(self, pissacomponent):
        self.component = pissacomponent

    def getTotalCost(self):
        return self.component.getTotalCost() + PizzaComponent.getTotalCost(self)

    def getDescription(self):
        return self.component.getDescription() + ' ' +PizzaComponent.getDescription(self)

class Sweet_Pasta(Decorator):
    """Massa para Pizza Doce"""
    cost = 0.90
    def __init__(self, pissacomponent):
        Decorator.__init__(self, pissacomponent)

class Salty_Pasta(Decorator):
    """Massa para Pizza Salgada"""
    cost = 0.55
    def __init__(self, pissacomponent):
        Decorator.__init__(self, pissacomponent)


class Mozzarella(Decorator):
    """Compnente: Mussarela"""
    cost = 0.75
    def __init__(self, pissacomponent):
        Decorator.__init__(self, pissacomponent)


class Peperoni(Decorator):
    """Compnente: Peperoni"""
    cost = 0.85
    def __init__(self, pissacomponent):
        Decorator.__init__(self, pissacomponent)


class Tomate(Decorator):
    """Compnente: Tomate"""
    cost = 0.25
    def __init__(self, pissacomponent):
        Decorator.__init__(self, pissacomponent)



class Provolone(Decorator):
    """Compnente: Provolone"""
    cost = 0.95
    def __init__(self, pissacomponent):
        Decorator.__init__(self, pissacomponent)

class Chocolate(Decorator):
    """Compnente: Chocolate"""
    cost = 0.75
    def __init__(self, pissacomponent):
        Decorator.__init__(self, pissacomponent)

pizza_peproni = Salty_Pasta(Peperoni(Tomate((Mozzarella(Platter())))))
print(pizza_peproni.getDescription()+ ": $" + str(pizza_peproni.getTotalCost()))
pizza_chocolate = Sweet_Pasta(Chocolate(Platter()))
print(pizza_chocolate.getDescription()+ ": $" + str(pizza_chocolate.getTotalCost()))