import json


class Todos:
    def __init__(self):
        try:
            with open("todos.json", "r") as f:
                self.todos = json.load(f)
        except FileNotFoundError:
            self.todos = []

    # metoda zwraca listę todos[]
    def all(self):
        return self.todos

    # metoda zwraca wybrany przepis z listy
    def get(self, id):
        return self.todos[id]

    # matowa tworzy nowy element listy
    def create(self, data):
        data.pop("csrf_token")
        self.todos.append(data)

    # metoda zapisuje listę do pliku w formacie JSON
    def save_all(self):
        with open("todos.json", "w") as f:
            json.dump(self.todos, f)

    # metoda nadpisuje w liście przepis na pozycji id a następnie zapisuje do pliku w formacie JSON
    def update(self, id, data):
        data.pop("csrf_token")
        self.todos[id] = data
        self.save_all()


todos = Todos()
