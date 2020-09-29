__all__ = ["ArmorGrades"]


class ArmorGrade:
    def __init__(self, grade_name):
        self.name = grade_name

    def __iter__(self):
        yield "Name", self.name,

    def __str__(self):
        return f"{dict(self)}"

    def __repr__(self):
        return f"GRD({self.name}"


class ArmorGrades:
    LIGHT = ArmorGrade("Light")
    STURDY = ArmorGrade("Sturdy")
    HEAVY = ArmorGrade("Heavy")
    UNKNOWN = ArmorGrade("Unknown")

    ALL = [
        LIGHT,
        STURDY,
        HEAVY,
        UNKNOWN,
    ]
