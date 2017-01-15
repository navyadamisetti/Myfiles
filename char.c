#include <stdio.h>
int main()
{
	char a[5],*p;
	p=&a[5];
	for(int i=0;i<5;i++)
		scanf("%s",a[i]);
	return 0;
}
//insertion of numbers/char/strings into array using pointer
//malloc
//calloc