from ArrayListClass import ArrayList

list = ArrayList()

while True:
    command = input("[메뉴선택] i-입력, d-삭제, r-변경, p-출력, l-파일읽기, s-저장, q-종료 : ")

    if command == 'i':
        pos = int(input("입력행번호: "))
        str = input("입력행내용: ")
        list.insert(pos, str)

    elif command == 'd':
        pos = int(input("입력행번호: "))
        list.delete(pos)

    elif command == 'r':
        pos = int(input("변경행번호: "))
        str = input("변경행내용: ")
        list.replace(pos, str)

    elif command == 'p':
        print('Line Editor')
        for line in range(list.size):
            print('[%d] ' %line, end = ' ')
            print(list.getEntry(line))

    elif command == 'l':
        filename = 'test.txt'
        infile = open(filename, 'r')
        lines = infile.readlines()
        for line in lines:
            list.insert(list.size, line.rstrip('\n'))
        infile.close()

    elif command == 's':
        filename = 'test.txt'
        outfile = open(filename, 'w')
        len = list.size
        for i in range(len):
            outfile.write(list.getEntry(i) + '\n')
        outfile.close()

    elif command == 'q':
        exit()
