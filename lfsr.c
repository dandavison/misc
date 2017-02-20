#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>


void print_binary_16(uint16_t n) {
   uint16_t flag = 0x8000;
   for(int i = 0; i < 16; i++) {
       if (!(i % 4))
           printf(" ");
       if (n & flag)
           printf("1");
       else
           printf("0");

       n <<= 1;
   }
   printf("\n");
}


uint16_t get_bit(uint16_t reg, uint16_t n) {
    uint16_t ans = (reg >> (16 - n)) << (16 - 1);
    /* printf("get bit %-6d\n", n); */
    /* printf("\n%-14s", "reg >> (16-n)"); */
    /* print_binary_16(reg >> (16 - n)); */
    /* printf("get bit %-6d", n); */
    /* print_binary_16(ans); */
    return ans;
}

/* starting reg:  0000 0100 0000 0000 */
/* get bit 11 */

/* reg >> (16-n)  0000 0000 0010 0000 */
/* get bit 11     1000 0000 0000 0000 */

void lfsr_calculate(uint16_t *reg) {
    uint16_t new_bit = (((get_bit(*reg, 16) ^
                          get_bit(*reg, 14)) ^
                         get_bit(*reg, 13)) ^
                        get_bit(*reg, 11));

    *reg = (*reg >> 1) | new_bit;
}


int main(int argc, char **argv) {
    uint16_t reg = 0x1;

    /* reg = 1024; */
    /* printf("starting reg: "); */
    /* print_binary_16(reg); */
    /* get_bit(reg, 11); */
    // lfsr_calculate(&reg);

    for(int i=0; i < 0xffff + 8; i++)  {
        printf("%-8d %-8u ", i, reg);
        print_binary_16(reg);
        lfsr_calculate(&reg);
    }
}



