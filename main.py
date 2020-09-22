import tarantool


def main():

    connection = tarantool.connect("localhost", 3301)
    tester = connection.space('tester')
    tester1 = connection.space('tester1')
