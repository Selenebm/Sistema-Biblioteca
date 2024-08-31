from subject import Subject

class Articulo(Subject):
    def __init__(self, ID, titulo, autor, fechaPublicacion, editorial, isbn, categoria, numEjemplares):
        super().__init__()
        self.ID = ID
        self.titulo = titulo
        self.autor = autor
        self.fechaPublicacion = fechaPublicacion
        self.editorial = editorial
        self.isbn = isbn
        self.categoria = categoria
        self.numEjemplares = numEjemplares

    def actualizarDatosArticulo(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        print(f"Datos del artículo {self.ID} actualizados con éxito.")
        self.notify_observers(f"El artículo {self.titulo} ha sido actualizado.")

    def to_dict(self):
        return {
            'ID': self.ID,
            'titulo': self.titulo,
            'autor': self.autor,
            'fechaPublicacion': self.fechaPublicacion,
            'editorial': self.editorial,
            'isbn': self.isbn,
            'categoria': self.categoria,
            'numEjemplares': self.numEjemplares
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            ID=data['ID'],
            titulo=data['titulo'],
            autor=data['autor'],
            fechaPublicacion=data['fechaPublicacion'],
            editorial=data['editorial'],
            isbn=data['isbn'],
            categoria=data['categoria'],
            numEjemplares=data['numEjemplares']
        )