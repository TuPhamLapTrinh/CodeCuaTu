import pygame
from random import randint, uniform, choice
import math
import pygame.mixer
from win32api import GetSystemMetrics
vector2 = pygame.math.Vector2
trails = []
fade_p = []

# general
GRAVITY_FIREWORK = vector2(0, 0.3)
GRAVITY_PARTICLE = vector2(0, 0.07)
DISPLAY_WIDTH, DISPLAY_HEIGHT = (GetSystemMetrics(0), GetSystemMetrics(1)) 
BACKGROUND = pygame.image.load('background.jpg')
BACKGROUND = pygame.transform.scale(BACKGROUND, (DISPLAY_WIDTH, DISPLAY_HEIGHT))
# firework
FIREWORK_SPEED_MIN = 17
FIREWORK_SPEED_MAX = 20
FIREWORK_SIZE = 6
# particle
PARTICLE_LIFESPAN = 60
X_SPREAD = 0.8
Y_SPREAD = 0.8
PARTICLE_SIZE = 4
MIN_PARTICLES = 30 # chia biến ra 1 vùng khác của ổ
MAX_PARTICLES = 50 # Max==min(max/2) + n(n-1)
X_WIGGLE_SCALE = 20  # higher -> less wiggle
Y_WIGGLE_SCALE = 10 # less--> higher
EXPLOSION_RADIUS_MIN = 50
EXPLOSION_RADIUS_MAX = 100
COLORFUL = True
# trail
TRAIL_LIFESPAN = PARTICLE_LIFESPAN / 2
TRAIL_FREQUENCY = 10  # higher -> less trails
TRAILS = True
# music
pygame.mixer.init()
# add more channels to the mixer
pygame.mixer.set_num_channels(100)
pygame.mixer.Channel(0).play(pygame.mixer.Sound('firework-sound.mp3'), loops=-1)
#FADE_COLOURS = [(45, 45, 45), (60, 60, 60), (75, 75, 75), (125, 125, 125), (150, 150, 150)]

class Firework:
    def __init__(self):
        self.colour = tuple(randint(0, 255) for _ in range(3))
        self.colours = tuple(tuple(randint(0, 255) for _ in range(3)) for _ in range(3))
        # Creates the firework particle
        self.firework = Particle(randint(0, DISPLAY_WIDTH), DISPLAY_HEIGHT, True, self.colour)
        self.exploded = False
        self.particles = []

    def update(self, win: pygame.Surface) -> None:
        # method called every frame
        if not self.exploded:
            self.firework.apply_force(GRAVITY_FIREWORK)
            self.firework.update(True)
            self.show(win)
            if self.firework.vel.y >= 0:
                self.exploded = True
                self.explode()

        else:
            for particle in self.particles:
                particle.update()
                particle.show(win)

    def explode(self):
        # when the firework has entered a stand still, create the explosion particles
        amount = randint(MIN_PARTICLES, MAX_PARTICLES)
        if COLORFUL:
            self.particles = [Particle(self.firework.pos.x, self.firework.pos.y, False, self.colours[randint(0, 2)]) for _ in range(amount)]
        else:
            self.particles = [Particle(self.firework.pos.x, self.firework.pos.y, False, self.colour) for _ in range(amount)]
        pygame.mixer.find_channel().play(pygame.mixer.Sound('firework-sound.mp3'))
    def show(self, win: pygame.Surface) -> None:
        # draw the firework on the given surface
        x = int(self.firework.pos.x)
        y = int(self.firework.pos.y)
        pygame.draw.circle(win, self.colour, (x, y), self.firework.size)

    def remove(self) -> bool:
        if not self.exploded:
            return False

        for p in self.particles:
            if p.remove:
                self.particles.remove(p)

        # remove the firework object if all particles are gone
        return len(self.particles) == 0


class Particle(object):
    def __init__(self, x, y, firework, colour):
        self.firework = firework
        self.pos = vector2(x, y)
        self.origin = vector2(x, y)
        self.acc = vector2(0, 0)
        self.remove = False
        self.explosion_radius = randint(EXPLOSION_RADIUS_MIN, EXPLOSION_RADIUS_MAX)
        self.life = 0
        self.colour = colour
        self.trail_frequency = TRAIL_FREQUENCY + randint(-3, 3)

        if self.firework:
            self.vel = vector2(0, -randint(FIREWORK_SPEED_MIN, FIREWORK_SPEED_MAX))
            self.size = FIREWORK_SIZE
        else:
            # set random position of particle 
            self.vel = vector2(uniform(-1, 1), uniform(-1, 1))
            self.vel.x *= randint(7, self.explosion_radius + 2)
            self.vel.y *= randint(7, self.explosion_radius + 2)
            self.size = randint(PARTICLE_SIZE - 1, PARTICLE_SIZE + 1)
            # update pos and remove particle if outside radius
            self.move()
            self.outside_spawn_radius()

    def update(self, is_fireworks=False) -> None:
        # called every frame
        self.life += 1
        # add a new trail if life % x == 0
        if self.life % self.trail_frequency == 0:
            trails.append(Trail(self.pos.x, self.pos.y, is_fireworks, self.colour, self.size))
        # wiggle
        self.apply_force(vector2(uniform(-1, 1) / X_WIGGLE_SCALE, GRAVITY_PARTICLE.y + uniform(-1, 1) / Y_WIGGLE_SCALE))
        self.move()

    def apply_force(self, force: pygame.math.Vector2) -> None:
        self.acc += force

    def outside_spawn_radius(self) -> bool:
        # if the particle spawned is outside of the radius that creates the circular firework, remov it
        distance = math.sqrt((self.pos.x - self.origin.x) ** 2 + (self.pos.y - self.origin.y) ** 2)
        return distance > self.explosion_radius

    def move(self) -> None:
        # called every frame, moves the particle
        if not self.firework:
            self.vel.x *= X_SPREAD
            self.vel.y *= Y_SPREAD

        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0

        self.decay()

    def show(self, win: pygame.Surface, fireworks=False) -> None:
        # draw the particle on to the surface
        x = int(self.pos.x)
        y = int(self.pos.y)
        if not fireworks:
            pygame.draw.circle(win, self.colour, (x, y), self.size)
        else:
            # draw fireworks shape
            pass
    def decay(self) -> None:
        # random decay of the particles
        if self.life > PARTICLE_LIFESPAN:
            if randint(0, 30) == 0:
                self.remove = True
        # if too old, begone
        if not self.remove and self.life > PARTICLE_LIFESPAN * 1.5:
            self.remove = True


class Trail(Particle):
    def __init__(self, x, y, is_firework, colour, parent_size):
        Particle.__init__(self, x, y, is_firework, colour)
        self.size = parent_size - randint(2, 3) if is_firework else parent_size - randint(1, 2)
        self.is_firework = is_firework

    def decay(self) -> bool:
        # decay also changes the color on the trails
        # returns true if to be removed, else false
        self.life += 1
        if self.life % 100 == 0:
            self.size -= 1

        self.size = max(0, self.size)
        # static yellow-ish colour self.colour = (255, 255, 220)
        self.colour = (min(self.colour[0] + 5, 255), min(self.colour[1] + 5, 255), min(self.colour[2] + 5, 255))

        if self.life > TRAIL_LIFESPAN:
            ran = (randint(0, 30) if not self.is_firework else randint(0, 5))
            if ran == 0:
                return True
        # if too old, begone
        if not self.remove and self.life > TRAIL_LIFESPAN * 1.5:
            return True
        
        return False


def update(win: pygame.Surface, fireworks: list, trails: list) -> None:
    if TRAILS:
        for t in trails:
            t.show(win)
            if t.decay():
                trails.remove(t)

    for fw in fireworks:
        fw.update(win)
        if fw.remove():
            fireworks.remove(fw)

    pygame.display.update()


def main():
    pygame.init()
    pygame.display.set_caption("Happy New Year!!")
    win = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    clock = pygame.time.Clock()

    fireworks = [Firework() for i in range(1)]  # create the first fireworks
    running = True

    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    fireworks.append(Firework())
                elif event.key == pygame.K_2:
                    for i in range(randint(3,4)):
                        fireworks.append(Firework())
        # append background
        win.blit(BACKGROUND, (0, 0))

        if randint(0, 20) == 1:  # create new firework
            fireworks.append(Firework())
        update(win, fireworks, trails)
    pygame.quit()
    quit()


main()

# check
# left==right==> false
# check 1
#  left != right==> true
#     ==>>>>>> check===check-1-check++ uw                                                                    