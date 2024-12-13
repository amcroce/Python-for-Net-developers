class Wizard:
    # def __init__(self, name, level):
    #     self.name = name
    #     self.level = level

    def __init__(self):
        self.name : str = "Gandalf"
        self.level : int = 0

    @classmethod
    def train_with_class_method(cls, baseLevel):
        return cls("Gandalf", baseLevel+1)

    @staticmethod
    def train(baseLevel: int) -> "Wizard":
        w = Wizard()
        w.level += baseLevel
        return w

## Types warning are basically an editor feature, not a runtime feature
def main():
    gandalf = Wizard.train(10)
    gandalf.level += 1
    print(f"The leve of the wizard {gandalf.name} is {gandalf.level}")

if __name__ == "__main__":
    main()