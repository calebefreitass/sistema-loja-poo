class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

class Carrinho:
    def __init__(self):
        self.produtos = []
    
    def adcionar_produto(self, produto: Produto):
        self.produtos.append(produto)
        print(f"'{produto.nome}' ADCIONADO AO CARRINHO.")

    def calcular_valor_total_carrinho(self) -> float:
        total = 0
        for prod in self.produtos:
            total += prod.preco
        return total

class Descontos:
    def calcular(self, total: float):
        pass

class DescontoFixo(Descontos):
    def __init__(self, valor_fixo: float):
        self.valor_fixo = valor_fixo

    def calcular(self, total):
        return total - self.valor_fixo
    
class DescontoPorcentagem(Descontos):
    def __init__(self, porcentagem: int):
        self.porcentagem = porcentagem / 100
    def calcular(self, total):
        porcentagem_de_desconto = total * self.porcentagem
        return total - porcentagem_de_desconto

class Pedido:
    def __init__(self, carrinho: Carrinho, desconto: None): 
        self.carrinho = carrinho
        self.desconto = desconto

    def calcular_valor_total_do_pedido(self):
        total_bruto = self.carrinho.calcular_valor_total_carrinho()
        total_pedido = self.desconto.calcular(total_bruto)
        print(f"TOTAL DO PEDIDO: {total_pedido}")

#--------ENTRADAS--------#         
    
prod1 = Produto("Ps5 Pro", 5000.00)
prod2 = Produto("GTA VI", 300.00)

carrinho1 = Carrinho()
carrinho1.adcionar_produto(prod1)
carrinho1.adcionar_produto(prod2)
desconto = DescontoPorcentagem(20)
pedido = Pedido(carrinho1, desconto)
pedido.calcular_valor_total_do_pedido()

prod3 = Produto("Puma Suede XL", 600.00)
prod4 = Produto("IPhone 13", 3200.00)

carrinho2 = Carrinho()
carrinho2.adcionar_produto(prod1)
carrinho2.adcionar_produto(prod2)
desconto = DescontoFixo(100.00)
pedido = Pedido(carrinho2, desconto)
pedido.calcular_valor_total_do_pedido()