from adaptador import MeuTaxi
import gym

env = gym.make("Taxi-v3").env
state = env.reset()
env.render()
taxi = MeuTaxi(env.desc, env.decode(state))
for a in taxi.path():
    state, reward, done, info = env.step(a)
    env.render()
if done:
    print("Chegou a Solução")
else:
    print("Não Chegou a Solução")