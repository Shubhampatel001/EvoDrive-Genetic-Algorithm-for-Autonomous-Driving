import pygame
import os
import math
import sys
import neat

# Define colors for different elements
COLORS = {
    'TRACK_COLOR': (2, 105, 31, 255),         # Color of the track
    'COLLISION_COLOR': (0, 255, 255, 0),      # Color to indicate collisions
    'RADAR_COLOR': (255, 255, 255, 255),      # Color of the radar lines
    'RADAR_POINT_COLOR': (0, 255, 0, 0),       # Color of the radar detection points
    'TEXT_BG_COLOR': (255, 255, 255, 150),    # Background color for text
    'TEXT_COLOR': (0, 0, 0)                    # Text color
}

# Set up the dimensions of the game window
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Create game window
pygame.display.set_caption("NEAT Wheels")  # Set the window title

# Load track image
TRACK = pygame.image.load(os.path.join("Assets", "map.png"))

# Initialize Pygame font
pygame.font.init()
font = pygame.font.SysFont('Arial', 24)  # Create a font object for rendering text


class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Initialize the parent class (Sprite)
        self.original_image = pygame.image.load(os.path.join("Assets", "car.png"))
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(490, 530))  # Start position of the car
        self.vel_vector = pygame.math.Vector2(0.8, 0)  # Velocity vector for movement
        self.angle = 0  # Initial angle of the car
        self.rotation_vel = 5  # Rotation speed
        self.direction = 0  # Current direction of the car
        self.alive = True  # Car's status (alive or crashed)
        self.radars = []  # List to store radar data

    def update(self):
        self.radars.clear()  # Clear radar data for the current update
        self.drive()         # Move the car
        self.rotate()        # Rotate the car based on direction
        
        # Perform radar checks at specified angles
        for radar_angle in (-60, -30, 0, 30, 60):
            self.radar(radar_angle)
        
        self.collision()     # Check for collisions with the track
        self.data()          # Collect radar data

    def drive(self):
        # Update car position based on velocity
        self.rect.center += self.vel_vector * 4

    def collision(self):
        length = 40  # Distance for collision detection
        # Calculate collision points based on the current angle
        collision_point_right = [
            int(self.rect.center[0] + math.cos(math.radians(self.angle + 18)) * length),
            int(self.rect.center[1] - math.sin(math.radians(self.angle + 18)) * length)
        ]
        collision_point_left = [
            int(self.rect.center[0] + math.cos(math.radians(self.angle - 18)) * length),
            int(self.rect.center[1] - math.sin(math.radians(self.angle - 18)) * length)
        ]

        # Check if points are within screen bounds before checking for track color
        if (0 <= collision_point_right[0] < SCREEN_WIDTH and 0 <= collision_point_right[1] < SCREEN_HEIGHT) and \
           (0 <= collision_point_left[0] < SCREEN_WIDTH and 0 <= collision_point_left[1] < SCREEN_HEIGHT):
            
            # Determine if a collision occurs
            if SCREEN.get_at(collision_point_right) == COLORS['TRACK_COLOR'] or \
               SCREEN.get_at(collision_point_left) == COLORS['TRACK_COLOR']:
                self.alive = False  # Mark the car as not alive (crashed)
    
        # Draw visual indicators for collision points
        if 0 <= collision_point_right[0] < SCREEN_WIDTH and 0 <= collision_point_right[1] < SCREEN_HEIGHT:
            pygame.draw.circle(SCREEN, COLORS['COLLISION_COLOR'], collision_point_right, 4)
        if 0 <= collision_point_left[0] < SCREEN_WIDTH and 0 <= collision_point_left[1] < SCREEN_HEIGHT:
            pygame.draw.circle(SCREEN, COLORS['COLLISION_COLOR'], collision_point_left, 4)

    def rotate(self):
        # Rotate the car based on user input (direction)
        if self.direction == 1:  # Turn right
            self.angle -= self.rotation_vel
            self.vel_vector.rotate_ip(self.rotation_vel)  # Update velocity direction
        if self.direction == -1:  # Turn left
            self.angle += self.rotation_vel
            self.vel_vector.rotate_ip(-self.rotation_vel)  # Update velocity direction

        # Update the car image based on the current angle
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 0.1)
        self.rect = self.image.get_rect(center=self.rect.center)  # Update the rectangle for the rotated image

    def radar(self, radar_angle):
        length = 0  # Initialize radar length
        x = int(self.rect.center[0])
        y = int(self.rect.center[1])

        # Sweep the radar out to a maximum length
        while length < 200:
            # Calculate radar point based on angle and length
            x = int(self.rect.center[0] + math.cos(math.radians(self.angle + radar_angle)) * length)
            y = int(self.rect.center[1] - math.sin(math.radians(self.angle + radar_angle)) * length)

            # Check if radar point is within bounds
            if 0 <= x < SCREEN_WIDTH and 0 <= y < SCREEN_HEIGHT:
                if SCREEN.get_at((x, y)) == COLORS['TRACK_COLOR']:
                    break  # Stop if the radar hits the track (grass)
            else:
                break  # Exit if the radar goes out of bounds

            length += 1  # Increment radar length

        # Draw the radar line and point on the screen
        pygame.draw.line(SCREEN, COLORS['RADAR_COLOR'], self.rect.center, (x, y), 1)
        pygame.draw.circle(SCREEN, COLORS['RADAR_POINT_COLOR'], (x, y), 3)

        # Calculate and store the distance to the detected point
        dist = int(math.sqrt(math.pow(self.rect.center[0] - x, 2) + math.pow(self.rect.center[1] - y, 2)))
        self.radars.append([radar_angle, dist])  # Append radar data for neural network input

    def data(self):
        input_data = [0, 0, 0, 0, 0]  # Initialize radar data input
        for i, radar in enumerate(self.radars):
            input_data[i] = int(radar[1])  # Update input with radar distances
        return input_data  # Return radar data for neural network


def remove(index):
    # Remove a car from the simulation
    cars.pop(index)
    ge.pop(index)
    nets.pop(index)


def eval_genomes(genomes, config):
    global cars, ge, nets, generation

    cars = []  # List to hold all cars
    ge = []    # List to hold genome objects
    nets = []  # List to hold neural networks

    # Create cars and associated networks for each genome
    for genome_id, genome in genomes:
        cars.append(pygame.sprite.GroupSingle(Car()))  # Create a new car and add to the list
        ge.append(genome)                               # Add genome to the list
        net = neat.nn.FeedForwardNetwork.create(genome, config)  # Create neural network from genome
        nets.append(net)                               # Add neural network to the list
        genome.fitness = 0                            # Initialize fitness score

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # Exit game on quit
                sys.exit()

        SCREEN.blit(TRACK, (0, 0))  # Draw the track image on the screen

        if len(cars) == 0:  # If no cars are left, exit the loop
            generation += 1  # Increment the generation after each run
            break

        # Update fitness for alive cars
        for i, car in enumerate(cars):
            ge[i].fitness += 1  # Increment fitness for surviving
            if not car.sprite.alive:  # Check if car is alive
                remove(i)  # Remove the car if it is not alive

        # Activate the neural networks for each car and update their direction
        for i, car in enumerate(cars):
            output = nets[i].activate(car.sprite.data())  # Get output from the neural network
            if output[0] > 0.7:
                car.sprite.direction = 1  # Turn right
            elif output[1] > 0.7:
                car.sprite.direction = -1  # Turn left
            else:
                car.sprite.direction = 0  # Move straight

        # Update and draw all cars
        for car in cars:
            car.draw(SCREEN)  # Draw the car on the screen
            car.update()       # Update the car's position and state

        # Draw current generation and number of alive cars
        current_gen_text = f"Generation: {generation} | Alive: {len(cars)}"
        text_surface = font.render(current_gen_text, True, COLORS['TEXT_COLOR'])
        text_rect = text_surface.get_rect(topleft=(10, 10))

        # Draw background rectangle for text
        pygame.draw.rect(SCREEN, COLORS['TEXT_BG_COLOR'], text_rect.inflate(10, 10))  # Inflate for padding
        SCREEN.blit(text_surface, text_rect)  # Blit text surface onto the screen

        pygame.display.update()  # Refresh the screen


# Setup NEAT Neural Network
def run(config_path):
    global pop, generation
    generation = 0  # Initialize generation counter
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )

    pop = neat.Population(config)  # Initialize the population for NEAT

    # Reporters for logging
    pop.add_reporter(neat.StdOutReporter(True))  # Print NEAT output to the console
    stats = neat.StatisticsReporter()  # Collect statistics on the evolution process
    pop.add_reporter(stats)

    while True:
        # Run the NEAT evolution
        pop.run(eval_genomes, 50)  # Run the evolution process
        


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)  # Get the directory of the current script
    config_path = os.path.join(local_dir, 'config.txt')  # Path to the NEAT configuration file
    run(config_path)  # Start the NEAT evolution process
