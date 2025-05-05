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

    t = ((1.5 * Tp) + 5)/(1 - sum(yi))

    return t

def EffectiveGreenTime(tc,Tp,yi):
    """
    .
    """

    teg = tc-Tp
    syi = sum(yi)
    t = [teg*(i/syi) for i in yi]

    return t

if __name__=="__main__":
    Tp = 3*InterGreensVeicularSignalTime(14+5+5,speed=40)
    D = [100,300,300]
    C = [1800,1800,1800]
    # D = [500,500,175,175]
    # C = [1800,1800,1800,1800]
    yi = [1.192*i/j for i,j in zip(D,C)]
    tc = WebsterMethod(Tp,yi)
    print(tc,EffectiveGreenTime(tc,Tp,yi))

    print(RedClearanceVeicularSignaTime(30,speed=40))

    # result = YellowVeicularSignalTime(speed=80)
    # print(result)