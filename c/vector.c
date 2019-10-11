#include "vector.h"
#include <stdio.h>

vector4 *transform(matrix4x4 *m,vector4 *vin,vector4 *vout)
{
    int i;
    vout->x = 0;
    vout->y = 0;
    vout->z = 0;
    vout->w = 0;
    for(i=0;i<4;i++)
    {
        vout->x += vin->v[i]*m->x[i];
        vout->y += vin->v[i]*m->y[i];
        vout->z += vin->v[i]*m->z[i];
        vout->w += vin->v[i]*m->w[i];
    }
    return vout;
}

vector4 *project(vector4 *vin)
{
    vin->x/=vin->z;
    vin->y/=vin->z;
    return vin;
}

void dump_vector(vector4 *vin)
{
    int i;
    printf("VECTOR: %f %f %f %f\n",vin->x,vin->y,vin->z,vin->w);
}

void dump_matrix(matrix4x4 *m)
{
    int i;
    printf("MATRIX:\n");
    for(i=0;i<4;i++)
    {
        printf("%f ",m->x[i]);
    }
    printf("\n");
    for(i=0;i<4;i++)
    {
        printf("%f ",m->y[i]);
    }
    printf("\n");
    for(i=0;i<4;i++)
    {
        printf("%f ",m->z[i]);
    }
    printf("\n");
    for(i=0;i<4;i++)
    {
        printf("%f ",m->w[i]);
    }
    printf("\n");
}