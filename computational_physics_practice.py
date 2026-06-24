from vpython import *


ground = box(
    pos=vector(0, -0.1, 0),
    size=vector(5, 0.2, 2),
    color=color.green
)


ball = sphere(
    pos=vector(0, 1, 0),
    radius=0.1,
    color=color.blue
)


g = vector(0, -9.8, 0)

ball.m = 0.05

v0 = 3.5
ball.v = vector(0, v0, 0)

t = 0
dt = 0.01

while t < 1:

    rate(100)

    F = ball.m * g
    a = F / ball.m

    ball.v = ball.v + a * dt
    ball.pos = ball.pos + ball.v * dt

    t = t + dt

while True:
    rate(60)