#include<stdio.h>
#include<conio.h>
void main()
{
char a[10],b[10];
int i,j,lm=0,cd=0,sum;
clrscr();
printf("enter two string:\n");
scanf("%s %s",&a,&b);
for(i=0;a[i]!='\0';i++)
{
l++;
}
printf("%d\n",l);
for(j=0;a[j]!='\0';j++)
{
cd++;
}
printf("%d\n",c);
for(i=0;i<l;i++)
{
for(j=0;j<c;j++)
{
if(i==j)
sum=a[i]+b[j];
}
sum=sum-96;
if(sum>122)
{
sum=sum-26;
}
printf("%c",sum);
}
getch();
}
