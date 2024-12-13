def read_csv(path):
    message = {}
    with open(path, 'r') as file:
        lines = []
        for line in file.read().split('\n'):
            line = line.split(',')
            lines.append(line)
        for i in range(len(lines[0])):
            key = lines[0][i]
            message[key] = []
            for line in lines[1:]:
                message[key].append(line[i])
    return message

print(read_csv('message.csv'))