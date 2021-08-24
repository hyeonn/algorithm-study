#include <stdio.h>
#include <stdbool.h>

int main()
{
    int n,cnt=0;
    bool isPrime = true;
    int num[101]={0};
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        scanf("%d",&num[i]);
    }

    for(int i=0;i<n;i++)
    {

        if(num[i]==1){
                continue;
        }
        for(int j=2;j<num[i];j++)
        {
            if(num[i]%j==0){
                isPrime=false;
                break;
            }

        }
        if(isPrime)
            cnt++;
        else
            isPrime = true;


    }
    printf("%d",cnt);
    return 0;
}