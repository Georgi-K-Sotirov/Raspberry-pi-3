import pygame
from evdev import InputDevice, list_devices
from select import select


# button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        action = False

        devices = [InputDevice(device) for device in list_devices()]
        for device in devices:
            if "touchscreen" in device.name.lower():
                for event in device.read():
                    if event.type == 1:  # EV_ABS
                        if event.code == 53:  # ABS_MT_POSITION_X
                            touch_x = (event.value - 150) / 10  # Adjust for touchscreen offset
                        elif event.code == 54:  # ABS_MT_POSITION_Y
                            touch_y = (event.value - 300) / 10  # Adjust for touchscreen offset

                            # Check if the touch is inside the button
                            if self.rect.collidepoint(touch_x, touch_y) and not self.clicked:
                                self.clicked = True
                                action = True

        # If there are no touches, reset the click state
        if self.clicked:
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

