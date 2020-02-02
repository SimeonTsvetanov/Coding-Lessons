def age_assignment(*args, **kwargs):
    """This is the solution from work in class"""
    results = {}
    for person in args:
        results[person] = kwargs[person[0]]
    return results


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
