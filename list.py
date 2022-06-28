if __name__ == '__main__':
    lst = []
    steps = []
    dat = []
    N = int(input())
    for _ in range(N):
        inst, *data = input().split()
        steps.append(inst)
        dat.append(data)

    for i in range(len(steps)):
        if steps[i] == 'print':
            print(lst)
            continue
        elif steps[i] == 'insert':
            meth = 'insert({0},{1})'.format(dat[i][0], dat[i][1])
        elif steps[i] == 'remove' or steps[i] == 'append':
            meth = '{0}({1})'.format(steps[i], dat[i][0])
        elif steps[i] == 'sort' or steps[i] == 'pop' or steps[i] == 'reverse':
            meth = '{0}()'.format(steps[i])
        eval('lst.{}'.format(meth))
        #eval('lst.{0}({1},{2})'.format(steps[i], dat[i][0], dat[i][1]))
