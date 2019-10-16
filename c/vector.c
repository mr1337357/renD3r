#include "vector.h"
#include <stdio.h>

#ifdef FIXED

#include "fixed.h"

void vector4_setx(vector4 *v,float f)
{
    f*=16384;
    v->x = f;
}

void vector4_sety(vector4 *v,float f)
{
    f*=16384;
    v->y = f;
}

void vector4_setz(vector4 *v,float f)
{
    f*=16384;
    v->z = f;
}

void vector4_setw(vector4 *v,float f)
{
    f*=16384;
    v->w = f;
}

float vector4_getx(vector4 *v)
{
    float f;
    f = v->x;
    return f/16384.0;
}

float vector4_gety(vector4 *v)
{
    float f;
    f = v->y;
    
    return f/16384.0;
} 

void matrix4x4_set(matrix4x4 *m,int i, int j,float f)
{
    f *= 16384;
    if(j==0)
    {
        m->x[i]=f;
    }
    if(j==1)
    {
        m->y[i]=f;
    }
    if(j==2)
    {
        m->z[i]=f;
    }
    if(j==3)
    {
        m->w[i]=f;
    }
}

vector4 *transform(matrix4x4 *m,vector4 *vin,vector4 *vout)
{
    int i;
    vout->x = 0;
    vout->y = 0;
    vout->z = 0;
    vout->w = 0;
    for(i=0;i<4;i++)
    {
        vout->x += FMUL(vin->v[i],m->x[i]);
        vout->y += FMUL(vin->v[i],m->y[i]);
        vout->z += FMUL(vin->v[i],m->z[i]);
        vout->w += FMUL(vin->v[i],m->w[i]);
    }
    return vout;
}

vector4 *project(vector4 *vin)
{
    vin->x = FDIV(vin->x,vin->z);
    vin->y = FDIV(vin->y,vin->z);
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
        printf("%d ",m->x[i]);
    }
    printf("\n");
    for(i=0;i<4;i++)
    {
        printf("%d ",m->y[i]);
    }
    printf("\n");
    for(i=0;i<4;i++)
    {
        printf("%d ",m->z[i]);
    }
    printf("\n");
    for(i=0;i<4;i++)
    {
        printf("%d ",m->w[i]);
    }
    printf("\n");
}

#else

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

void matrix4x4_set(matrix4x4 *m,int i, int j,float f)
{
    if(j==0)
    {
        m->x[i]=f;
    }
    if(j==1)
    {
        m->y[i]=f;
    }
    if(j==2)
    {
        m->z[i]=f;
    }
    if(j==3)
    {
        m->w[i]=f;
    }
}

void vector4_setx(vector4 *v,float f)
{
    v->x = f;
}

void vector4_sety(vector4 *v,float f)
{
    v->y = f;
}

void vector4_setz(vector4 *v,float f)
{
    v->z = f;
}

void vector4_setw(vector4 *v,float f)
{
    v->w = f;
}

float vector4_getx(vector4 *v)
{
    return v->x;
}

float vector4_gety(vector4 *v)
{
    return v->y;
} 

#endif