import numpy

def YellowVeicularSignalTime(speed=60,aad=3,tr=1,i=0,g=9.8):
    """
    Calcula o tempo de amarelo necessário para o semáforo (mínimo)
    Referência: 6.7.1 Entreverdes para os veículos - Manual Brasileiro de Sinalização de Trânsito (Volume V)
    """

    t = tr + ((speed/3.6)/(2*(aad+(i*g))))

    return t

def RedClearanceVeicularSignaTime(d2,c=12,speed=60):
    """
    Calcula o tempo de vermelo geral necessário para o semáforo (mínimo)
    Referência: 6.7.1 Entreverdes para os veículos - Manual Brasileiro de Sinalização de Trânsito (Volume V)
    """

    t = (d2 + c)/(speed/3.6)

    return t

def InterGreensVeicularSignalTime(d2,speed=60,aad=3,tr=1,i=0,g=9.8,c=12):
    """
    Calcula o tempo de amarelo necessário para o semáforo (mínimo)
    Referência: 6.7.1 Entreverdes para os veículos - Manual Brasileiro de Sinalização de Trânsito (Volume V)
    """

    tys = YellowVeicularSignalTime(speed,aad,tr,i,g)
    trcs = RedClearanceVeicularSignaTime(d2,c,speed)

    tig = tys + trcs

    return tig

def WebsterMethod(Tp,yi):
    """
    Calcular o tempo de ciclo ótimo pelo Método de Webster
    Referência: 6.9.2 Método de Webster - Manual Brasileiro de Sinalização de Trânsito (Volume V)
    """

    to = ((1.5 * Tp) + 5)/(1 - sum(yi))

    return to

if __name__=="__main__":
    Tp = 2*InterGreensVeicularSignalTime(15+5+5,speed=40)
    yi = [i/1800 for i in [550,550,200,200]]

    print(WebsterMethod(Tp,yi))