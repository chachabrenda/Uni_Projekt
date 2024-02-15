#include "bb64.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LINE_LENGTH 68

int main(int argc, char* argv[]) {
    FILE* file = NULL;
    if (argc > 1) {
        // Dateiname als Argument übergeben
        file = fopen(argv[1], "r");
    if (file == NULL) {
            fprintf(stderr, "Fehler: Datei %s konnte nicht geöffnet werden.\n", argv[1]);
            return 1;
                      }
                  }
    else {
        // Datei über stdin einlesen
        file = stdin;
         }

    // Daten aus der Datei einlesen und bb64-kodieren
    char buffer[3];
    size_t data_length = 0;
    char* encoded_data = NULL;

    while ((data_length = fread(buffer, sizeof(char), sizeof(buffer), file)) > 0) {
        // bb64-Kodierung durchführen
        char* encoded_chunk = bb64_encode(buffer);

        // Ergebnis ausgeben und auf Zeilenlänge achten
        size_t encoded_length = strlen(encoded_chunk);
        size_t line_length = 0;

        for (size_t i = 0; i < encoded_length; i++) {
            putchar(encoded_chunk[i]);
            line_length++;

            if (line_length == MAX_LINE_LENGTH) {
                putchar('\n');
                line_length = 0;
                                                }
                                                    }

        // Speicher freigeben
        free(encoded_chunk);
                                                                                  }

    // Zeilenumbruch, falls notwendig
    if (data_length == 0 && encoded_data != NULL && encoded_data[0] != '\0' && encoded_data[strlen(encoded_data) - 1] != '\n') {
        putchar('\n');
                                                }

    // Datei schließen, falls geöffnet
    if (file != stdin) {
        fclose(file);
                       }

    return 0;
                                 }
