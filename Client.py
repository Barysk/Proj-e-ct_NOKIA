import pygame
import time


pygame.init()
pygame.joystick.init()


if pygame.joystick.get_count() < 1:
    print("No controller connected")
    exit()


controller = pygame.joystick.Joystick(0)
controller.init()

axis_positions = ["L3_X", "L3_Y", "L3_Z", "R3_X", "R3_Y", "R3_Z"]
button_states = ["Button L1", "Button R1", "Triangle", "Square", "Circle", "Cross", "Start", "Select", "UP/DOWN",
                 "LEFT/RIGHT"]


def translate_input(data):
    translated = []
    axis_data = data[0].split(',')
    button_data = data[1].split(',')

    for i in range(6):
        translated.append(f"{axis_positions[i]}: {axis_data[i]}")

    for i in range(10):
        translated.append(f"{button_states[i]}: {'Pressed' if button_data[i] != '0' else 'Released'}")

    return translated


def read_controller_input():
    while True:
        pygame.event.pump()


        axis_values = []
        for i in range(controller.get_numaxes()):
            axis_values.append(controller.get_axis(i))


        button_values = []
        for i in range(controller.get_numbuttons()):
            button_values.append(controller.get_button(i))

        axis_str = ','.join(map(str, axis_values))
        button_str = ','.join(map(str, button_values))

        controller_data = [axis_str, button_str]


        translated_data = translate_input(controller_data)
        for item in translated_data:
            print(item)

        time.sleep(0.5)



read_controller_input()
