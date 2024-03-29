from adaptador import MeuTaxi
from datetime import datetime
import gym

env = gym.make("Taxi-v3").env

def test_1():
    state = env.reset()
    state = env.encode(3, 2, 1, 0)
    env.render()
    inicio = datetime.now()  
    result = MeuTaxi(env.desc, env.decode(state))
    fim = datetime.now()
    print(fim - inicio)
    assert result.path()[-1]==5

def test_2():
    state = env.reset()
    state = env.encode(3, 1, 2, 0)
    env.render()
    inicio = datetime.now()  
    result = MeuTaxi(env.desc, env.decode(state))
    fim = datetime.now()
    print(fim - inicio)
    assert result.path()[-1]==5

def test_3():
    state = env.reset()
    state = env.encode(3, 1, 3, 0)
    env.render()
    inicio = datetime.now()  
    result = MeuTaxi(env.desc, env.decode(state))
    fim = datetime.now()
    print(fim - inicio)
    assert result.path()[-1]==5

def test_4():
    state = env.reset()
    state = env.encode(3, 3, 0, 1)
    env.render()
    inicio = datetime.now()  
    result = MeuTaxi(env.desc, env.decode(state))
    fim = datetime.now()
    print(fim - inicio)
    assert result.path()[-1]==5

def test_5():
    state = env.reset()
    state = env.encode(3, 1, 1, 2)
    env.render()
    inicio = datetime.now()  
    result = MeuTaxi(env.desc, env.decode(state))
    fim = datetime.now()
    print(fim - inicio)
    assert result.path()[-1]==5

def test_6():
    state = env.reset()
    state = env.encode(3, 1, 3, 3)
    env.render()
    inicio = datetime.now()  
    result = MeuTaxi(env.desc, env.decode(state))
    fim = datetime.now()
    print(fim - inicio)
    assert result.path()[-1]==5