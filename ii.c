#include<stdio.h>
#include<stdlib.h>
using namespace std;
 

bool checkPangram (string &str)
{
  
    vector<bool> mark(26, false);

    int index;
 
    for (int j=0; j<str.length(); j++)
    {
        if ('A' <= str[j] && str[j] <= 'Z')
            index = str[j] - 'A';
 
        else if('a' <= str[j] && str[j] <= 'z')
            index = str[j] - 'a';
 
       
        mark[index] = true;
    }
 
    
    for (int j=0; j<=25; j++)
        if (mark[j] == false)
            return (false);
 
    return (true);
}
 

int main()
{
    string str;
    printf("Enter the string");
    gets(str);
 
    if (checkPangram(str) == true)
        printf (""%s" is a pangram", str.c_str());
    else
        printf (""%s" is not a pangram", str.c_str());
 
    return(0);
}
