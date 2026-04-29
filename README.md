# Gerador de Números Pseudoaleatórios Xoroshiro128plus

Este repositório contém uma implementação em Python do algoritmo **xoroshiro128+** (Xor/rotate/shift/rotate), um gerador de números pseudoaleatórios (PRNG) de 64 bits projetado por David Blackman e Sebastiano Vigna.

## Visão Geral

O xoroshiro128+ é conhecido por sua alta performance e baixo uso de memória, sendo estatisticamente mais robusto que geradores tradicionais como o LCG (Linear Congruential Generator). Ele utiliza um estado de 128 bits, dividido em duas variáveis de 64 bits (`s0` e `s1`).

## Estrutura do Código

### Inicialização de Sementes
A função `seed_gen()` utiliza o módulo `os.urandom` para extrair entropia diretamente do sistema operacional. Isso garante que as sementes iniciais sejam imprevisíveis a cada execução, convertendo 8 bytes aleatórios em inteiros de 64 bits.

### Operação de Rotação (rotl)
Diferente de linguagens como C, o Python não possui um operador nativo para rotação de bits (*circular shift*). A função `rotl(x, k)` implementa essa operação manualmente:
* Desloca o número `k` posições para a esquerda.
* Realiza o preenchimento com os bits deslocados à direita.
* Aplica uma máscara de bits (`0xFFFFFFFFFFFFFFFF`) para manter o resultado dentro do limite de 64 bits.

### Função Principal (next_xorshiro)
Esta função executa o núcleo do algoritmo:
1. Calcula o resultado somando os estados atuais.
2. Aplica operações de XOR, Shift e Rotação para atualizar o estado interno.
3. Garante o comportamento de overflow de 64 bits em todas as etapas.

### Geração Uniforme (rand_uniform)
Para gerar um número de ponto flutuante no intervalo $[0, 1)$, o algoritmo:
1. Obtém um inteiro de 64 bits.
2. Desloca 11 bits para a direita (`>> 11`), restando 53 bits.
3. Divide o resultado por $2^{53}$ (`1 << 53`).

Esta técnica é utilizada porque o padrão IEEE 754 (Double Precision) possui exatamente 53 bits de mantissa, garantindo uma distribuição uniforme sem perdas de precisão por arredondamento.

## Requisitos
* Python 3.x
* Módulo `os` (nativo da biblioteca padrão)
