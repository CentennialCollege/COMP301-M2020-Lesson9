from barplot import SixSidedDie_BarPlot as d6_plot

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

    someOtherList=[19, 3, 15, 7, 11]
    aNewList=someOtherList[1:3]
    endList=someOtherList[:2]

    print(endList)

    sentence="hello, my name is Tom"

    if "Tom" in sentence:
        print("Tom is in the sentence")
    else:
        print("Error: not in the sentence.")

    del(someOtherList[-1])

    print(someOtherList)

    someOtherList.clear()

    print(someOtherList)

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

def dictionaries():
    my_dictionary = {}
    my_dictionary[0]="0"
    my_dictionary["Tom"]="Tom"
    my_dictionary["Mark"]="Sensei"
    my_dictionary["Toronto"]="Hot"

    print(my_dictionary)

    another_one={'Tom': 'Tom', 'Mark': 'Sensei', 'Toronto': 'Hot'}

    if(my_dictionary == another_one):
        print("both dictionaries are the same!")

    print(dict(enumerate(another_one)))

    print(my_dictionary[0])

    print(list(my_dictionary.items()))

def is_odd(x):
    """Returns True only if x is odd."""
    return x % 2 !=0

def is_even(x):
    """Returns True only if x is even. """
    return x % 2 == 0

def counting():
    responses = [1, 2, 5, 4, 3, 5, 2, 1, 3, 3, 1, 4, 3, 3, 3, 2, 3, 3, 2, 2]

    for i in range(1, 6):
        print(f'{i} appears {responses.count(i)} times in responses')

    responses.reverse()

    print(responses)

    new_responses = responses.copy()

    new_responses.reverse()

    print(new_responses)

    print(list(filter(is_even, new_responses)))


d6_plot(60000)