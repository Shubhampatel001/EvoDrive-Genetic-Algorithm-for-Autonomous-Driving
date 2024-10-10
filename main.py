import pygame
import os
import math
import sys
import neat

# Color definitions
COLORS = {
    'TRACK_COLOR': (2, 105, 31, 255),
    'COLLISION_COLOR': (0, 255, 255, 0),
    'RADAR_COLOR': (255, 255, 255, 255),
    'RADAR_POINT_COLOR': (0, 255, 0, 0)
}

# Screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.font.init()

# Load track image
TRACK = pygame.image.load(os.path.join("Assets", "track1.png"))


class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Load car image and initialize properties
        self.original_image = pygame.image.load(os.path.join("Assets", "car.png"))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(490, 530))
        self.vel_vector = pygame.math.Vector2(0.8, 0)
        self.angle = 0
        self.rotation_vel = 5
        self.direction = 0
        self.alive = True
        self.radars = []

    def update(self):
        self.radars.clear()
        self.drive()
        self.rotate()
        
        # Create radars at specified angles
        for radar_angle in (-60, -30, 0, 30, 60):
            self.radar(radar_angle)

        self.collision()
        self.data()

    def drive(self):
        # Move the car forward
        self.rect.center += self.vel_vector * 6

    def collision(self):
        length = 40
        # Calculate collision points for right and left sides
        collision_point_right = [
            int(self.rect.center[0] + math.cos(math.radians(self.angle + 18)) * length),
            int(self.rect.center[1] - math.sin(math.radians(self.angle + 18)) * length)
        ]
        collision_point_left = [
            int(self.rect.center[0] + math.cos(math.radians(self.angle - 18)) * length),
            int(self.rect.center[1] - math.sin(math.radians(self.angle - 18)) * length)
        ]

        # Check if the collision points are within the screen bounds
        if (0 <= collision_point_right[0] < SCREEN_WIDTH and 0 <= collision_point_right[1] < SCREEN_HEIGHT) and \
           (0 <= collision_point_left[0] < SCREEN_WIDTH and 0 <= collision_point_left[1] < SCREEN_HEIGHT):
        
            # Mark car as not alive if it collides with the track
            if SCREEN.get_at(collision_point_right) == COLORS['TRACK_COLOR'] \
                    or SCREEN.get_at(collision_point_left) == COLORS['TRACK_COLOR']:
                self.alive = False

        # Draw collision points for visual debugging
        pygame.draw.circle(SCREEN, COLORS['COLLISION_COLOR'], collision_point_right, 4)
        pygame.draw.circle(SCREEN, COLORS['COLLISION_COLOR'], collision_point_left, 4)

    def rotate(self):
        # Rotate car based on direction input
        if self.direction == 1:
            self.angle -= self.rotation_vel
            self.vel_vector.rotate_ip(self.rotation_vel)
        elif self.direction == -1:
            self.angle += self.rotation_vel
            self.vel_vector.rotate_ip(-self.rotation_vel)

        # Update car image based on the angle
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 0.1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def radar(self, radar_angle):
        length = 0
        x = int(self.rect.center[0])
        y = int(self.rect.center[1])

        while length < 200:
            # Calculate radar endpoint based on angle and length
            x = int(self.rect.center[0] + math.cos(math.radians(self.angle + radar_angle)) * length)
            y = int(self.rect.center[1] - math.sin(math.radians(self.angle + radar_angle)) * length)

            # Stop radar if it hits the track
            if 0 <= x < SCREEN_WIDTH and 0 <= y < SCREEN_HEIGHT:
                if SCREEN.get_at((x, y)) == COLORS['TRACK_COLOR']:
                    break  # Stop if we hit grass
            else:
                break  # Exit if we go out of bounds

            length += 1

        # Draw radar line and point
        pygame.draw.line(SCREEN, COLORS['RADAR_COLOR'], self.rect.center, (x, y), 1)
        pygame.draw.circle(SCREEN, COLORS['RADAR_POINT_COLOR'], (x, y), 3)

        # Calculate distance and store radar data
        dist = int(math.sqrt(math.pow(self.rect.center[0] - x, 2) +
                             math.pow(self.rect.center[1] - y, 2)))
        self.radars.append([radar_angle, dist])

    def data(self):
        # Prepare input data for the neural network
        input_data = [0, 0, 0, 0, 0]
        for i, radar in enumerate(self.radars):
            input_data[i] = int(radar[1])
        return input_data


# Global variable to track generations
generation = 0


def draw_stats(generation, alive):
    # Draw the current generation and number of alive cars on the screen
    font = pygame.font.Font(None, 50)
    text = f"Generation: {generation} | Alive: {alive}"
    text_surface = font.render(text, True, (255, 255, 255))  # White text
    text_rect = text_surface.get_rect(topleft=(10, 10))

    # Create a transparent background rectangle for better readability
    background_rect = pygame.Surface(text_rect.size)
    background_rect.fill((0, 0, 0))  # Fill with black
    background_rect.set_alpha(128)  # Set transparency
    SCREEN.blit(background_rect, text_rect.topleft)  # Draw background
    SCREEN.blit(text_surface, text_rect.topleft)  # Draw text


def remove(index):
    # Remove car and corresponding genome/network from the lists
    cars.pop(index)
    ge.pop(index)
    nets.pop(index)


def eval_genomes(genomes, config):
    global cars, ge, nets, generation

    cars = []
    ge = []
    nets = []

    for genome_id, genome in genomes:
        cars.append(pygame.sprite.GroupSingle(Car()))
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 0  # Initialize fitness

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.blit(TRACK, (0, 0))

        # Increment generation if no cars are left
        if len(cars) == 0:
            generation += 1
            break

        # Update fitness for alive cars
        for i, car in enumerate(cars):
            ge[i].fitness += 1
            if not car.sprite.alive:
                remove(i)

        draw_stats(generation, len(cars))

        # Activate neural network and set car direction
        for i, car in enumerate(cars):
            output = nets[i].activate(car.sprite.data())
            if output[0] > 0.7:
                car.sprite.direction = 1
            elif output[1] > 0.7:
                car.sprite.direction = -1
            else:
                car.sprite.direction = 0

        # Update car positions and render
        for car in cars:
            car.draw(SCREEN)
            car.update()
        pygame.display.update()


# Setup NEAT Neural Network
def run(config_path):
    global pop
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )

    pop = neat.Population(config)

    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)

    # Run NEAT for a specified number of generations
    pop.run(eval_genomes, 50)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)
