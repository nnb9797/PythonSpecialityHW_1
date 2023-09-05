import argparse
from Matrix import Matrix
from Converter import convert_format

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Operation:")
    parser.add_argument('-m_1', type=list, action='append', default=[['1', '1', '1', ' ', '1', '1', '1', ' ', '1', '1',
                                                                      '1', ' ', '1', '1', '1']])
    parser.add_argument('-m_2', type=list, action='append', default=[['1', '1', '1', ' ', '1', '1', '1', ' ', '1', '1',
                                                                      '1', ' ', '1', '1', '1']])
    parser.add_argument('-operation', type=str, default='+')

    args = parser.parse_args()

    m_1 = convert_format(args.m_1)
    m_2 = convert_format(args.m_2)

    if args.operation == '+':
        print(f'Addition: \n{m_1} {args.operation} {m_2}:', f'\n{Matrix(m_1) + Matrix(m_2)}')
    elif args.operation == '*':
        print(f'Multiplication: \n{m_1} {args.operation} {m_2}:', f'\n{Matrix(m_1) * Matrix(m_2)}')
    elif args.operation == '=':
        print(f'Comparison: \n{m_1} {args.operation} {m_2}:', f'\n{Matrix(m_1) == Matrix(m_2)} ')
    else:
        print(f'No {args.operation} operation!')


# Terminal commands:

# python Terminal.py -m_1='123 456 789' -m_2='123 456 789' -operation='='
# python Terminal.py -m_1='123 456 789' -m_2='123 456 789' -operation='+'
# python Terminal.py -m_1='123 456 789' -m_2='123 456 789' -operation='*'
