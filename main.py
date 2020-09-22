import tarantool


def main():

    connection = tarantool.connect("localhost", 3301)
    tester = connection.space('tester')
    tester1 = connection.space('tester1')

    print("\033[33mtester\033[0m:")
    print(tester.select(3))
    print("\033[33mtester\033[31m1\033[0m:")
    print(tester1.select(3))

    print("\033[33mtester\033[0m:")
    print(tester.select())
    print("\033[33mtester\033[31m1\033[0m:")
    print(tester1.select(),"\n")

    print(tester)
    print(tester1)


if __name__== "__main__":
    main()

