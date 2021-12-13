import pandas
from more_itertools import unique_everseen

def main():
    names = []
    source = pandas.read_excel('SOURCE.xlsx')
    for _ in range(len(source)):
        names.append(source['Name'][_])
    names = list(unique_everseen(names))
    for _ in range(len(names)):
        name = names[_]
        count = 0
        listi = [['Account'], ['Campaign'], ['Clicks']]
        a = 2
        while a <= len(source)+1:
            if source.loc[count, 'Name'] == name:
                listi[0].append(source.loc[count, 'Account'])
                listi[1].append(source.loc[count, 'Campaign'])
                listi[2].append(source.loc[count, 'Clicks'])
            a += 1
            count += 1
        d = {x[0]: x[1:] for x in listi}
        df = pandas.DataFrame(d)
        df.to_excel('excels/{}.xlsx'.format(name), index=False)

if __name__ == '__main__':
    try:
        main()
        print('Successful')
    except:
        print('Something gone wrong. Please check if all excel files saved.')