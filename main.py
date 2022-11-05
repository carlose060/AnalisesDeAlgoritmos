import matplotlib.pyplot as plt


if __name__ == '__main__':

    MODE = ['Cauda', 'Recursivo', 'For']
    LINGUAGEM = ['c', 'haskell', 'python']
    
    tempos = {   
        'Cauda' : {
            'c' : [],
            'python' : [],
            'haskell' : []
        },
        'Recursivo': {
            'c' : [],
            'python' : [],
            'haskell' : [] 
        },
        'For' : {
            'c' : [],
            'python' : [],
        }
    }
    for tipo in MODE:
        for linguagem in LINGUAGEM:
            if tipo == 'For' and linguagem == 'haskell': continue
            # Como haskell não ha repetição por laço...
            for i in range(10, 990, 10):
                if tipo == 'Recursivo' and i > 50: break
                # Recursivo foi restringido ate 50.
                full_path = f'tempos/{linguagem}/{tipo}/{i}.txt'
                # Caminho por todos os arquivos criados
                with open(full_path,'r') as file:
                    file.readline()
                
                    tempo = file.readline()
                    tempo = tempo.replace(',','.')
                    tempo = tempo[5:-2]
                    l = tempo.split('m')
                    min_for_sec = int(l[0]) * 60
                    # Normalização de minutos para segundos
                    sec = float(l[1]) + min_for_sec
                    tempos[tipo][linguagem].append(sec)
                    # Separo em dicionarios as linguagens e as estruturas

    eixo_x = [x for x in range(10, 990, 10)]
    # Eixo com os valores do fib N, relacionando com o tempo no eixo y

    plt.plot(eixo_x,tempos['For']['c'], label='C')
    plt.plot(eixo_x,tempos['For']['python'], label= 'Python')
    plt.ylim(bottom =0.000,top=0.02)
    plt.xlim(left=0,right=1000)
    plt.xlabel("Execuções")
    plt.ylabel("Tempo de execução")
    plt.legend(loc='best')
    plt.title('Looping')
    plt.savefig('loopgrafico.png')
    plt.close()


    plt.plot(eixo_x,tempos['Cauda']['c'], label='C')
    plt.plot(eixo_x,tempos['Cauda']['python'], label= 'Python')
    plt.plot(eixo_x, tempos['Cauda']['haskell'], label = "Haskell")
    plt.ylim(bottom =0.000,top=0.02)
    plt.xlim(left=0,right=1000)
    plt.xlabel("Execuções")
    plt.ylabel("Tempo de execução")
    plt.legend(loc='best')
    plt.title('Recursão em cauda')
    plt.savefig('caudagrafico.png')
    plt.close()

    eixo_x = [x for x in range(10, 60, 10)]
    # Para recursivo o intervalo usado foi 10--50

    plt.plot(eixo_x,tempos['Recursivo']['c'], label='C')
    plt.plot(eixo_x,tempos['Recursivo']['python'], label= 'Python')
    plt.plot(eixo_x, tempos['Recursivo']['haskell'], label = "Haskell")
    plt.ylim(bottom =0.000,top=0.2)
    plt.xlim(left=10,right=50)
    plt.xlabel("Execuções")
    plt.ylabel("Tempo de execução")
    plt.legend(loc='best')
    plt.title('Recursão padrão')
    plt.savefig('recursivografico.png')
    plt.close
