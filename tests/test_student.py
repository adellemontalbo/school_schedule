from school_schedule.student import Student

def test_add_class_returns_classes():
    name = "Bob"
    grade = "Senior"
    classes = ["Coding"]

    bob = Student(name, grade, classes)
    result = bob.add_class("Math")

    assert result == ["Coding", "Math"]
    assert len(result) == 2
    assert "Math" in result

def test_empty_list_creates_empty_class_list():
    name = "Bob"
    grade = "Senior"
    classes = []

    bob = Student(name, grade, classes)

    assert len(bob.classes) == 0
    assert isinstance(bob.classes, list) == True

def test_num_classes_returns_correct_value():
    name = "Bob"
    grade = "Senior"
    classes = ["Coding", "Math", "Science"]

    bob = Student(name, grade, classes)
    result = bob.get_num_classes()

    assert result == 3
    assert result == len(bob.classes)
