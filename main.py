from student import Student, Professor


def main():
    sviat = Student('Sviatoslav', 'Pushak', 35, 'Lviv University', 'Progachimmer Faculty', 1, 60)
    jeka = Student('Jeka', 'Dobrii', 42, 'Lviv University', 'Progachimmer Faculty', 5, 75)
    dima = Professor('Jeka', 'Dobrii', 7, 'Lviv University', 'Progachimmer Faculty')
    sviat.request_help(jeka)
    sviat.request_help(jeka)
    sviat.request_help(jeka)
    sviat.request_help(jeka)
    sviat.request_help(jeka)
    print(sviat.grade)
    sviat.request_help(dima)
    print(sviat.grade)


if __name__ == '__main__':
    main()
