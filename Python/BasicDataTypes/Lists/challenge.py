def read_input_commands(n):
    input_commands = []
    for i in range(0, n):
        input_commands.append(raw_input().strip())
    return input_commands


def parse_command(command):
    return command.split()


def execute_operation(l, operation):
    command = operation[0]
    if command == "insert":
        l.insert(int(operation[1]), int(operation[2]))
        return l
    elif command == "print":
        print l
    elif command == "remove":
        l.remove(int(operation[1]))
        return l
    elif command == "append":
        l.append(int(operation[1]))
        return l
    elif command == "sort":
        l.sort()
        return l
    elif command == "pop":
        l.pop()
        return l
    elif command == "reverse":
        l.reverse()
        return l

if __name__ == '__main__':
    N = int(raw_input())
    commands = read_input_commands(N)
    result = []
    for command in commands:
        execute_operation(result, parse_command(command))