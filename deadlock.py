class Recurso:
    def __init__(self, nome):
        self.nome = nome
        self.lock = False

    def adquirir(self):
        if not self.lock:
            print(f"Recurso {self.nome} foi adquirido.")
            self.lock = True
            return True
        else:
            print(f"Recurso {self.nome} já está em uso.")
            return False

    def liberar(self):
        if self.lock:
            print(f"Recurso {self.nome} foi liberado.")
            self.lock = False

def adquirir_recursos_em_ordem(*recursos):
    for recurso in recursos:
        if not recurso.adquirir(): 
            print("Falha ao adquirir recursos. Desfazendo operações...")
            liberar_recursos_em_ordem(*recursos[:recursos.index(recurso)])
            return False
    return True

def liberar_recursos_em_ordem(*recursos):
    for recurso in reversed(recursos):
        recurso.liberar()

recurso1 = Recurso("1")
recurso2 = Recurso("2")
recurso3 = Recurso("3")

def tarefa():
    print("Tentando adquirir recursos na ordem correta...")
    if adquirir_recursos_em_ordem(recurso1, recurso2, recurso3):
        print("Todos os recursos adquiridos com sucesso. Executando tarefa...")
        print("Tarefa completa. Liberando recursos.")
        liberar_recursos_em_ordem(recurso1, recurso2, recurso3)
    else:
        print("Falha ao adquirir os recursos.")

tarefa()
