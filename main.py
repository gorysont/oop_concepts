from parent import Parent, Child
from second import SecondChild


dad = Parent('Alex', 40) # dad is an object which call its class Parent()
kid = Child('Sergey', 5, "drawing", "something")
daugh = SecondChild("Anna", 12, "singing", "something")
dad.set_work("manager")

print(f"""
Dad's name is {dad.name}.
He's {dad.age} years old.
He works as a {dad.get_work()}.
        """)

print(f"""
Alex has two children.
His son's name is {kid.name}.
He's {kid.age} years old.
He likes {kid.hobby}. It's his hobby.
But he also has a work. Of course, this is {kid.get_work()}.
He helps his parents.
        """)

print(f"""
Alex's daughter name is {daugh.name}.
She's {daugh.age}.
She's hobby is {daugh.hobby}.
Usually she does {daugh.get_work()} after school.
""")

