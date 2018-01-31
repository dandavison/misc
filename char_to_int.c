#include <stdio.h>
#include <stdlib.h>


int main(int argc, char **argv) {
  char a = 'a';
  char b = 'b';
  char c = 'c';

  unsigned int ai = 'a';
  unsigned int bi = 'b';
  unsigned int ci = 'c';

  printf("%d %c\n", ai, a);
  printf("%d %c\n", bi, b);
  printf("%d %c\n", ci, c);
  printf("%ld %ld %ld\n", sizeof(a), sizeof(b), sizeof(c));
  printf("%ld %ld %ld\n", sizeof(char), sizeof(unsigned int), sizeof(int));

  /* char *s = {'a', 'b', 'c'}; */
  /* unsigned int *si = (unsigned int *) s; */

  printf("%d %c\n", bi, b);
  printf("%d %c\n", ci, c);
  printf("%ld %ld %ld\n", sizeof(a), sizeof(b), sizeof(c));
  printf("%ld %ld %ld\n", sizeof(char), sizeof(unsigned int), sizeof(int));

  printf("%ld", 2 + 0xFFFFFFFF);
}
