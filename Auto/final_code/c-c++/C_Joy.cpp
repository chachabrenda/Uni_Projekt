#include <iostream>
#include <SDL2/SDL.h>
#include "MotorModule_new.h"

int main() {
    // Initialisiere SDL mit Joystick und Gamecontroller Unterstützung
    if (SDL_Init(SDL_INIT_JOYSTICK | SDL_INIT_GAMECONTROLLER) != 0) {
        std::cout << "Fehler beim Initialisieren von SDL: " << SDL_GetError() << std::endl;
        return 1;
    }

    // Initialisiere den Gamecontroller
    SDL_GameController* controller = nullptr;
    for (int i = 0; i < SDL_NumJoysticks(); i++) {
        if (SDL_IsGameController(i)) {
            controller = SDL_GameControllerOpen(i);
            if (controller != nullptr) {
                break;
            } else {
                std::cout << "Fehler beim Öffnen des Gamecontrollers: " << SDL_GetError() << std::endl;
                return 1;
            }
        }
    }

    // Initialisiere den Motor
    Motor motor(2, 3, 4, 17, 22, 27, 14, 15, 18);

    // Vorherige Joystick-Werte initialisieren
    float prevX = SDL_JoystickGetAxis(SDL_GameControllerGetJoystick(controller), 0) / 32767.0f;
    float prevY = SDL_JoystickGetAxis(SDL_GameControllerGetJoystick(controller), 1) / 32767.0f;

    // Hauptschleife
    while (true) {
        SDL_Event event;
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_JOYBUTTONDOWN) {
                if (event.jbutton.button == 0) {
                    std::cout << "Taste 0 gedrückt" << std::endl;
                    motor.move(0.6, 0, 0.1);
                } else if (event.jbutton.button == 1) {
                    std::cout << "Taste 1 gedrückt" << std::endl;
                    motor.move(-0.6, 0, 0.1);
                } else if (event.jbutton.button == 2) {
                    std::cout << "Taste 2 gedrückt" << std::endl;
                    motor.move(0, -0.8, 0.1);
                } else if (event.jbutton.button == 3) {
                    std::cout << "Taste 3 gedrückt" << std::endl;
                    motor.move(0, 0.8, 0.1);
                } else if (event.jbutton.button == 5) {
                    std::cout << "Taste 5 gedrückt" << std::endl;
                } else if (event.jbutton.button == 6) {
                    std::cout << "Taste 6 gedrückt" << std::endl;
                } else if (event.jbutton.button == 7) {
                    std::cout << "Taste 7 gedrückt" << std::endl;
                } else if (event.jbutton.button == 8) {
                    std::cout << "Taste 8 gedrückt" << std::endl;
                }
            }
        }

        // Aktuelle Joystick-Werte abfragen
        float x = SDL_JoystickGetAxis(SDL_GameControllerGetJoystick(controller), 0) / 32767.0f;
        float y = SDL_JoystickGetAxis(SDL_GameControllerGetJoystick(controller), 1) / 32767.0f;

        // Wenn sich die Joystick-Werte ändern, die Motoren bewegen und die vorherigen Werte aktualisieren
        if (x != prevX || y != prevY) {
            std::cout << "Joystick-Werte: x=" << x << ", y=" << y << std::endl;
            motor.move(y * 0.8, x * 0.6, 0.1);
            prevX = x;
            prevY = y;
        }
    }

    // Gamecontroller schließen und SDL beenden
    SDL_GameControllerClose(controller);
    SDL_Quit();

    return 0;
}

