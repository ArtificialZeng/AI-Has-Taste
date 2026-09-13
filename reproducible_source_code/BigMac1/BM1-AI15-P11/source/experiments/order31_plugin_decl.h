#ifndef ERDOS993_ORDER31_PLUGIN_DECL_H
#define ERDOS993_ORDER31_PLUGIN_DECL_H

#include <stdio.h>

void research_check_tree(FILE *out, int *parent, int n);
void research_check_summary(unsigned long long generated, double cpu_seconds);
void research_check_init(void);

#endif
