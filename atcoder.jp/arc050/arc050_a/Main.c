#include <stdio.h>
main(){
    char a;
    char b;
    scanf("%c %c", &a, &b);
    if (a + 32 == b){
        printf("Yes");
    }
    else{
        printf("No");
    }
}