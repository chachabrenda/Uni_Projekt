#include <iostream>
#include <SDL2/SDL.h>

void init() {
    SDL_Init(SDL_INIT_VIDEO);
    SDL_Window* win = SDL_CreateWindow("Window", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 100, 100, SDL_WINDOW_SHOWN);
    SDL_Renderer* renderer = SDL_CreateRenderer(win, -1, 0);
}

bool getKey(const std::string& keyName) {
    bool ans = false;
    SDL_Event event;
    while (SDL_PollEvent(&event)) {
        if (event.type == SDL_KEYDOWN) {
            std::string keyString = SDL_GetKeyName(event.key.keysym.sym);
            if (keyString == keyName) {
                ans = true;
                break;
            }
        }
    }
    SDL_RenderPresent(SDL_GetRenderer(SDL_GetWindowFromID(1)));
    return ans;
}

// int main() {
//     init();
//     while (true) {
//         if (getKey("LEFT")) {
//             std::cout << "Key Left was pressed" << std::endl;
//         }
//         if (getKey("RIGHT")) {
//             std::cout << "Key Right was pressed" << std::endl;
//         }
//     }
//     return 0;
// }
