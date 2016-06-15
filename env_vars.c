#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv) {
  if(argv) printf("true\n") ;
  else printf("false\n");

  char **foo;

  if(foo) printf("true\n") ;
  else printf("false\n");

  if(getenv("MYVAR"))
    printf("MYVAR is set to '%s'\n", getenv("MYVAR"));
  else
    printf("MYVAR is unset: '%s'\n", getenv("MYVAR"));

  return 0;
}
