import pygame
import sys
import getPixel

def draw_coordinates(screen, coordinates, point_size=1):
    # Draw a small rectangle or circle at each coordinate
    for (x, y) in coordinates:
        pygame.draw.circle(screen, (0, 0, 0), (x, y), point_size)

def main(coordinates):
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen_width, screen_height = 500, 500
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Black Pixel Coordinates")

    # Main loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw the coordinates
        draw_coordinates(screen, coordinates)

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()

# Example list of coordinates
image_path = "C:\\Users\\piyus\\OneDrive\\Desktop\\MiniProject\\database\\alphabets_config\\alphabets.jpg"  # Path to your input image
left = 50  # x-coordinate of the left side of the box
top = 50  # y-coordinate of the top side of the box
right = 300  # x-coordinate of the right side of the box
bottom = 330  # y-coordinate of the bottom side of the box

coordinates = getPixel.get_black_pixels_in_portion(image_path, left, top, right, bottom)
print(coordinates)

if __name__ == "__main__":
    main(coordinates)
