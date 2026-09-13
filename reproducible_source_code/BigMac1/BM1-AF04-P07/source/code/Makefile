CC ?= clang
CFLAGS ?= -O3 -std=c11 -Wall -Wextra -Wpedantic -Werror -Wno-deprecated-declarations

.PHONY: all clean test

all: builder_scan certifier_scan exact_max

builder_scan: builder_scan.c
	$(CC) $(CFLAGS) $< -o $@

certifier_scan: certifier_scan.c
	$(CC) $(CFLAGS) $< -o $@

exact_max: exact_max.c
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm -f builder_scan certifier_scan exact_max

test: all
	gentourng -q 9 | ./builder_scan 9 9
	gentourng -q 9 | ./certifier_scan 9 9
