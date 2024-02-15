#include <iostream>
#include <SDL2/SDL.h>
#include "MotorModule_new.h"

int main() {
    if (SDL_Init(SDL_INIT_JOYSTICK | SDL_INIT_GAMECONTROLLER) != 0) {
        std::cout << "Failed to initialize SDL: " << SDL_GetError() << std::endl;
        return 1;
    }

    SDL_GameController* controller = nullptr;
    for (int i = 0; i < SDL_NumJoysticks(); i++) {
        if (SDL_IsGameController(i)) {
            controller = SDL_GameControllerOpen(i);
            if (controller != nullptr) {
                break;
            } else {
                std::cout << "Failed to open game controller: " << SDL_GetError() << std::endl;
                return 1;
            }
        }
    }

    Motor motor(2, 3, 4, 17, 22, 27, 14, 15, 18);
    float prevX = SDL_JoystickGetAxis(SDL_GameControllerGetJoystick(controller), 0) / 32767.0f;
    float prevY = SDL_JoystickGetAxis(SDL_GameControllerGetJoystick(controller), 1) / 32767.0f;

    // Main Loop
    while (true) {
        SDL_Event event;
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_JOYBUTTONDOWN) {
                if (event.jbutton.button == 0) {
                    std::cout << "button 0 down" << std::endl;
                    motor.move(0.6, 0, 0.1);
                } else if (event.jbutton.button == 1) {
                    std::cout << "button 1 down" << std::endl;
                    motor.move(-0.6, 0, 0.1);
                } else if (event.jbutton.button == 2) {
                    std::cout << "button 2 down" << std::endl;
                    motor.move(0, -0.8, 0.1);
                } else if (event.jbutton.button == 3) {
                    std::cout << "button 3 down" << std::endl;
                    motor.move(0, 0.8, 0.1);
                } else if (event.jbutton.button == 5) {
                    std::cout << "button 5 down" << std::endl;
                } else if (event.jbutton.button == 6) {
                    std::cout << "button 6 down" << std::endl;
                } else if (event.jbutton.button == 7) {
                    std::cout << "button 7 down" << std::endl;
                } else if (event.jbutton.button == 8) {
                    std::cout << "button 8 down" << std::endl;
                }
            }
        }

        float x = SDL_JoystickGetAxis(SDL_GameControllerGetJoystick(controller), 0) / 32767.0f;
        float y = SDL_JoystickGetAxis(SDL_GameControllerGetJoystick(controller), 1) / 32767.0f;
        if (x != prevX || y != prevY) {
            std::cout << "Joystick values: x=" << x << ", y=" << y << std::endl;
            motor.move(y * 0.8, x * 0.6, 0.1);
            prevX = x;
            prevY = y;
        }
    }

    SDL_GameControllerClose(controller);
    SDL_Quit();

    return 0;
}
