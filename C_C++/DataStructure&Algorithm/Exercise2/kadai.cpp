#include "avltree.h"
#include <stdio.h>

int ins[6] = {41,38,31,12,19,8};
int del[6] = {8,12,19,31,38,41};

int main( )
{
    AvlTree T;
    Position P;
    int i;
    int j = 0;

    T = MakeEmpty( NULL );
    for( i = 0; i < 6; i++){
        T = Insert( ins
    [i], T );
        Tprint(T);
        if( ( P = Find( ins
    [i], T ) ) == NULL || Retrieve( P ) != ins
    [i] )
            printf( "Error at %d\n", i );
    }

        return 0;
}
