#include <iostream>
#include <SDL2/SDL.h>

// Die Funktion init initialisiert SDL, ein Fenster und einen Renderer.
void init() {
    SDL_Init(SDL_INIT_VIDEO);

    // Ein einfaches SDL-Fenster erstellen
    SDL_Window* win = SDL_CreateWindow("Fenster", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 100, 100, SDL_WINDOW_SHOWN);

    // Einen Renderer erstellen, um auf das Fenster zu zeichnen
    SDL_Renderer* renderer = SDL_CreateRenderer(win, -1, 0);
}

// Die Funktion getKey überprüft, ob eine bestimmte Taste gedrückt wurde.
bool getKey(const std::string& keyName) {
    bool ans = false;
    SDL_Event event;

    // SDL-Ereignisse abfragen, um Tastatureingaben zu überprüfen
    while (SDL_PollEvent(&event)) {
        if (event.type == SDL_KEYDOWN) {
            std::string keyString = SDL_GetKeyName(event.key.keysym.sym);

            // Wenn die gedrückte Taste mit der angegebenen Taste übereinstimmt, wird ans auf true gesetzt.
            if (keyString == keyName) {
                ans = true;
                break;
            }
        }
    }

    // Den Renderer aktualisieren (dies ist hier möglicherweise nicht erforderlich)
    SDL_RenderPresent(SDL_GetRenderer(SDL_GetWindowFromID(1)));

    return ans;
}

int main() {
    init();

    while (true) {
        if (getKey("LEFT")) {
            std::cout << "Taste Left wurde gedrückt" << std::endl;
        }

        if (getKey("RIGHT")) {
            std::cout << "Taste Right wurde gedrückt" << std.endl;
        }
    }

    return 0;
}

