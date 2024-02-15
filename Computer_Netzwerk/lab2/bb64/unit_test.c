#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "bb64.h"

void test_bb64_encode() {
    // Testfall 1: Eingabe mit einer Länge, die durch 3 teilbar ist
    char input1[] = "Hello, World!";
    char expected1[] = "I6LiR6yi85TlScna8G==";
    char* encoded1 = bb64_encode(input1);
    if (strcmp(encoded1, expected1) != 0) {
        printf("Testfall 1 fehlgeschlagen: Erwartet: %s, erhalten: %s\n", expected1, encoded1);
        free(encoded1);
        return;
                                          }
    free(encoded1);

    // Testfall 2: Eingabe mit einer Länge, die nicht durch 3 teilbar ist
    char input2[] = "Base64";
    char expected2[] = "Gc5pPJOq";
    char* encoded2 = bb64_encode(input2);
    if (strcmp(encoded2, expected2) != 0) {
        printf("Testfall 2 fehlgeschlagen: Erwartet: %s, erhalten: %s\n", expected2, encoded2);
        free(encoded2);
        return;
                                          }
    free(encoded2);

    // Weitere Testfälle können hier hinzugefügt werden...

    printf("Alle Unit-Tests erfolgreich durchgeführt.\n");
                        }

int main() {
    test_bb64_encode();
    return 0;
           }

