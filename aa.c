#include<stdio.h>
void main()
{
   long int k,j,b[100];
   scanf("%d",&j);
   if(k>=2&&k<=100000)
   {
      for(j=0;j<k;j++)
      {
         scanf("%d",&b[j]);
      }
      if(k%2==1)
      printf("yes");
      else
      printf("no");
   }
   else
   printf("Invalid input");
