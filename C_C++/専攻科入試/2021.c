#include<stdio.h>

#define M 7
#define N 5

int main(void){
    int a[10] = {2, 5, 7, 17, 19, 31, 37, 43};
    int b[10] = {3, 11, 13, 23, 29, 41, 47};
    int c[20];
    int i, j, k;
    i = j = k = 0;

    while(i<M && j<N){
        if(a[i]<=b[j]){
            c[k]=a[i];
            k++;
            i++;
        }
        else{
            c[k]=b[j];
            k++;
            j++;
        }
    }

// aとbの要素を順に並べたもの

    while(i<M){
        c[k]=a[i];
        k++;
        i++;
    }

    while(j<N){
        c[k]=b[j];
        k++;
        j++;
    }

    for(i=0; i<M+N; i++){
        printf("%d,",c[i]);
    }

    return 0;
}