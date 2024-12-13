class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    @classmethod
    def train(cls, baseLevel):
        return cls("Gandalf", baseLevel)

def main():
    gandalf = Wizard.train(10)
    gandalf.level += 1
    print(f"The leve of the wizard {gandalf.name} is {gandalf.level}")

if __name__ == "__main__":
    main()