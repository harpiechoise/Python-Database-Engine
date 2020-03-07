from Schema.Table import Cliente
if __name__ == "__main__":
    a = Cliente()
    a.nombre.value = "Jaime"
    a.edad.value = 21
    a.save()
    a.nombre.value = "Norma"
    a.edad.value = 60
    a.save()
    a.nombre.value = "Tomy"
    a.edad.value = 40
    a.save()
    a.nombre.value = "Seba"
    a.edad.value = 25
    a.save()
    a.nombre.value = "Zuilt"
    a.nombre.edad = 1500
    a.save()
    a.migrate()
