import sys
import math

MAX_BOOST = 1
MAX_DISTANCE = 1400      # en dessous, on ralentit
MAX_POWER = 100
MAX_ANGLE = 90           # au-dela, on ne pousse plus (on tourne d'abord)
BOOST_MIN_DIST = 4000    # boost seulement sur une longue ligne droite
BOOST_MAX_ANGLE = 5
COLLISION_DIST = 1000
USE_COLLISION = False    # passe a True pour tenter de percuter l'adversaire


def distance(x1, y1, x2, y2):
    return math.hypot(x1 - x2, y1 - y2)


def est_proche(x1, y1, x2, y2):
    return distance(x1, y1, x2, y2) <= COLLISION_DIST


def ajust_power(next_checkpoint_dist):
    # entre 30 et 100 : jamais a l'arret, jamais plus de 100
    power = int(MAX_POWER * next_checkpoint_dist / MAX_DISTANCE)
    return max(30, min(MAX_POWER, power))


def angle_factor(angle):
    # 1 si on est bien aligne, 0 si on est a MAX_ANGLE ou plus
    return max(0.0, 1 - abs(angle) / MAX_ANGLE)


# game loop
nb_boost = 0
prev_x, prev_y = None, None
while True:
    x, y, next_checkpoint_x, next_checkpoint_y, next_checkpoint_dist, next_checkpoint_angle = [int(i) for i in input().split()]
    opponent_x, opponent_y = [int(i) for i in input().split()]

    # vitesse estimee (le pod glisse : on corrige la visee pour ne pas deriver)
    if prev_x is None:
        vx, vy = 0, 0
    else:
        vx, vy = x - prev_x, y - prev_y
    prev_x, prev_y = x, y

    target_x = next_checkpoint_x - 3 * vx
    target_y = next_checkpoint_y - 3 * vy

    # puissance
    if abs(next_checkpoint_angle) >= MAX_ANGLE:
        thrust = 0
    elif (next_checkpoint_dist > BOOST_MIN_DIST
          and abs(next_checkpoint_angle) < BOOST_MAX_ANGLE
          and nb_boost < MAX_BOOST):
        thrust = 'BOOST'
        nb_boost += 1
    else:
        if next_checkpoint_dist > MAX_DISTANCE:
            thrust = MAX_POWER
        else:
            thrust = ajust_power(next_checkpoint_dist)
        thrust = int(thrust * angle_factor(next_checkpoint_angle))

    # collision (optionnelle) : on vise l'adversaire s'il est tout proche
    if USE_COLLISION and thrust != 'BOOST' and est_proche(x, y, opponent_x, opponent_y):
        target_x, target_y = opponent_x, opponent_y

    print(int(target_x), int(target_y), thrust)