class Person:

    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    if not people:
        return []
    list_person = [Person(human["name"], human["age"]) for human in people]
    for human in people:
        if human.get("wife"):
            Person.people[human["name"]].wife = Person.people[human["wife"]]
        elif human.get("husband"):
            Person.people[human["name"]].husband \
                = Person.people[human["husband"]]

    return list_person
