#include "fab.h"

long fab_impl(long a)
{
    if(a<2)
    {
        return a;
    }
    return a*fab_impl(a-1);
}

void print_bytes(uint8_t *data, uint32_t len)
{
for(uint32_t i=0;i<len;i++)
{
printf("%u",data[i]);
}
printf("\n");
}