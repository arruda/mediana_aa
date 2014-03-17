mediana_aa
==========

Código (Python) e pseudo código do calculo da mediana


Exemplo
-------

Neste exemplo temos os seguintes dados

    s = [1, 2, 13, 10, 4]
    k = 3

Aqui vai um possível caso (já que são aleatórios):

### iteracao: 1

     [s]: [1, 2, 13, 10, 4]
     k: 3
     s[i]: 2
     [s_menores],    [s_medianas],   [s_maiores]:
      [1]   [2]     [13, 10, 4]

### iteracao: 2

     [s]: [13, 10, 4]
     k: 1
     s[i]: 10
     [s_menores],    [s_medianas],   [s_maiores]:
      [4]   [10]    [13]

### iteracao: 3

     [s]: [4]
     k: 1
     s[i]: 4
     [s_menores],    [s_medianas],   [s_maiores]:
      []    [4]     []


Testes
------

Execute os testes com o comando:

    ./tests.sh



Licence
-------

Esse software é distribuido sob a licença MIT, veja o arquivo LICENSE para mais detalhes.
