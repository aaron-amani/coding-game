import sys
import math

ZOMBIE_SPEED = 400
ASH_SPEED = 1000
ASH_RANGE = 2000

def dist(ax, ay, bx, by):
    return math.hypot(ax - bx, ay - by)

def choose_target(ash, humans, zombies):
    best = None
    best_score = float('inf')
    for zx, zy in zombies:
        # l'humain le plus proche de ce zombie = sa cible probable
        d_human = min(dist(zx, zy, hx, hy) for hx, hy in humans)
        turns_zombie = d_human / ZOMBIE_SPEED

        # tours nécessaires à Ash pour être à portée de tir
        d_ash = dist(ash[0], ash[1], zx, zy)
        turns_ash = max(0, d_ash - ASH_RANGE) / ASH_SPEED

        savable = turns_ash <= turns_zombie
        # les zombies non sauvables passent en dernier
        score = turns_zombie if savable else turns_zombie + 10000

        if score < best_score:
            best_score = score
            best = (zx, zy)
    return best

while True:
    x, y = [int(i) for i in input().split()]
    humans = []
    for _ in range(int(input())):
        _, hx, hy = [int(j) for j in input().split()]
        humans.append((hx, hy))
    zombies = []
    for _ in range(int(input())):
        _, zx, zy, zx_next, zy_next = [int(j) for j in input().split()]
        zombies.append((zx_next, zy_next))

    tx, ty = choose_target((x, y), humans, zombies)
    print(tx, ty)