def lists():
    """ Application Entry point """
    print("Main Started...")
    c=[-45, 6, 0, 72, 1543]
    d=['Mary', 'Smith', 3.57, 2022]

    c+= [5]

    print(c)

    a_list = []

    for number in range(1, 6):
        a_list+=[number]

    print(a_list)

    letters = []

    letters+='Python'

    print(letters)


    list1 = [10, 20, 30]

    list2 = [40, 50]

    list3 = list1 + list2 + list1

    for i in range(len(list3)):
        print(f'{i}: {list3[i]}')

    
    lista = [1, 2, 3]

    listb = [1, 2, 3]

    listc = [3, 4, 5]

    print(lista==listb)

    print(lista==listc)

def tuples():
    john='John', 'Green', 3.3

    print(john)

    mary='Mary', 'Red', 3.4

    mary+=('Blue',)

    print(mary)

    singleton=('red',)

    print(singleton)

    print(mary[1])

def tuples_and_lists():
    numbers=[1, 2, 3, 4, 5]

    numbers+=(6, 7)

    print(numbers)

def unpack():
    student_tuple=('Amanda', [98, 85, 87])

    first_name, grades = student_tuple

    print(first_name)

    print(grades)

    science, math, english = grades
    print(science)
    print(math)
    print(english)

    first, second = 'hi'

    first, second = second, first

    print(first, second)

    number1, number2, number3 = [2, 3, 5]
    print(number1)
    print(number2)
    print(number3)

    number99 = 99
    number22 = 22
    number44 = 44
    number55 = 55

    number99, number22, number44, number55 = number22, number99, number55, number44

    print(number99, number22, number44, number55)

def iterate():
    colors=['red', 'orange', 'yellow']
    print(list(enumerate(colors)))

    print(tuple(enumerate(colors)))

    

iterate()
