#include <stdio.h>
#include <stdlib.h>
int main()
{
   char c;
   FILE *fp;
   fp=fopen("name.txt","w");
   while((c=getch())!='.')
   	fputc(c,fp);
   fclose(fp);
   fp=fopen("name.txt","r");
   while((c=fgetc(fp))!=EOF)
   	 printf("%c",c);
   	fclose(fp);
}