n = int(input('Escolha um número para ver a tabuada: '))
soma = n + 1, n + 2, n + 3, n + 4, n + 5, n + 6, n + 7, n + 8, n + 9
sub = n - 1, n - 2, n - 3, n - 4, n - 5, n - 6, n - 7, n - 8, n - 9
mult = n * 1, n * 2, n * 3, n * 4, n * \
    5, n * 6, n * 7, n * 8, n * 9
d = n / 1, n / 2, n / 3, n / 4, n / 5, n / 6, n / 7, n / 8, n / 9
print('A de soma é:{}\nA de sub é{}\nA de multiplicação:{}\nE a de divisão:{}'.format(
    soma, sub, mult, d))
