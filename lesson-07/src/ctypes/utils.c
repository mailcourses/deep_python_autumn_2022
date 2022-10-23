#include <stdlib.h>
#include <stdio.h>

int func1(int i)
{
    static int s = 0;
    s += i;
    return s;
}

void func2(char *text, int len)
{
    printf("String: [%s], len: [%d]\n", text, len);
}
