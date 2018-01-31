#include <stdio.h>


int main(int argc, char **argv) {
  for(unsigned int i = 0; i < 5; i++) {
    printf("%u ^ %u == %u\n", i, i, i ^ 0xFFFFFFFF);
    printf("~%u == %u\n", i, ~i);
  }

  // 0000 0000 0000 0000 0110 1101 0101 1110

  // int machine_code = 00000000000000000110110101011110;

  // int i = 0b00000000000000000110110101011110;

  // printf("%d\n", i);

}
