if __name__ == '__main__':
    N = int(input())
    
    li = []
    for i in range(N):
        cmds = input().split()
        cmd = cmds[0]
        
        if cmd == 'insert':
            li.insert(int(cmds[1]), int(cmds[2]))
        elif cmd == 'print':
            print(li)
        elif cmd == 'remove':
            li.remove(int(cmds[1]))
        elif cmd == 'append':
            li.append(int(cmds[1]))
        elif cmd == 'sort':
            li.sort()
        elif cmd == 'pop':
            li.pop()
        elif cmd == 'reverse':
            li.reverse()
