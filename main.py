for i in range(1,10):
    for j in range(i,10):
        print('{}*{}={:<2}'.format(i,j,i*j),end='\t')
    print('\n','\t'*i,end='')

