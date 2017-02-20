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
    return (reg >> (16 - n)) << (16 - 1);
}

void lfsr_calculate(uint16_t *reg) {
    uint16_t new_bit = (get_bit(*reg, 16) ^
                        get_bit(*reg, 14) ^
                        get_bit(*reg, 13) ^
                        get_bit(*reg, 11));

    *reg = (*reg >> 1) | new_bit;
}


int main(int argc, char **argv) {
    uint16_t reg = 0x1;
    for(int i=0; i < 0xffff + 8; i++)  {
        printf("%-8d %-8u ", i, reg);
        print_binary_16(reg);
        lfsr_calculate(&reg);
    }
}



