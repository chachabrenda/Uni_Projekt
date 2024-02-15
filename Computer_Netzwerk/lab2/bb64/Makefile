.PHONY: all clean

CFLAGS = -Wall

all: bb64 unit_test integration_test

bb64: main.c bb64.c
	gcc $(make) -o $@ $^
	
unit_test: unit_test.c bb64.c
	gcc $(make) -o $@ $^
	
integration_test:
	python3 integration_test.py

clean:
	rm -f bb64 unit_test

