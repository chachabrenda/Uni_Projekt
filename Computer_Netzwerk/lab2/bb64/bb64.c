#include "bb64.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

char* bb64_encode(const char* data) {
    // Anzahl der zu kodierenden Daten berechnen
    size_t data_length = strlen(data);

    // Länge des Ergebnis-Strings berechnen
    size_t result_length = (data_length / 3) * 4;
    if (data_length % 3 != 0) {
        result_length += 4;
                              }

    // Ergebnis-String erstellen
    char* result = malloc(result_length + 1);
    size_t result_index = 0;

    // Binärdaten in bb64-Format konvertieren
    for (size_t i = 0; i < data_length; i += 3) {
        int value = (data[i] << 16) | (data[i + 1] << 8) | data[i + 2];

        // Erste Stelle kodieren
        if (i < data_length - 2) {
            result[result_index++] = encode_char((value >> 18) & 0x3F);
            result[result_index++] = encode_char((value >> 12) & 0x3F);
            result[result_index++] = encode_char((value >> 6) & 0x3F);
            result[result_index++] = encode_char(value & 0x3F);
        } else if (i == data_length - 2) {
            result[result_index++] = encode_char((value >> 18) & 0x3F);
            result[result_index++] = encode_char((value >> 12) & 0x3F);
            result[result_index++] = encode_char((value >> 6) & 0x3F);
            result[result_index++] = '=';
        } else {  // i == data_length - 1
            result[result_index++] = encode_char((value >> 18) & 0x3F);
            result[result_index++] = encode_char((value >> 12) & 0x3F);
            result[result_index++] = '=';
            result[result_index++] = '=';
               }
                                                }

    result[result_length] = '\0';  // Nullterminierung hinzufügen

    return result;
                                    }

char encode_char(int value) {
    if (value >= 0 && value <= 9) {
        return value + '0';
    } else if (value >= 10 && value <= 35) {
        return value - 10 + 'A';
    } else if (value >= 36 && value <= 61) {
        return value - 36 + 'a';
    } else if (value == 62) {
        return '-';
    } else if (value == 63) {
        return '_';
    } else {
        // Unerwarteter Wert
        fprintf(stderr, "Fehler: Unerwarteter Wert bei der Kodierung.\n");
        exit(1);
    }
}
