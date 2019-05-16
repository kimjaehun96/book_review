#include <stdio.h>

int strlen(char *s)
{
   int   n;
   for (n = 0; *s != '\0'; ++s)
      ++n;
   printf("%d\n", n);
   return n;
}

void print_str(char *s){
	int i, b;
	for (i=0; i < (b - 1); i++)
		printf("%c\n", s[i]);
}
	



int main(void)
{
	char *a
	scnaf("%s", &a); 
	// printf("%c\n", s[1]);
	strlen(s);
	print_str(s);
	printf("%d", sizeof(s));
	return 0;
}