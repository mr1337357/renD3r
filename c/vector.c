#include "vector.h"

vector4 *transform(matrix4x4 *m,vector4 *vin,vector4 *vout)
{
    int i;
    vout->x = 0;
    for(i=0;i<4;i++)
    {
        vout->x += vin->v[i]*m->x[i];
        vout->y += vin->v[i]*m->y[i];
        vout->z += vin->v[i]*m->z[i];
        vout->w += vin->v[i]*m->w[i];
    }
    return vout;
}
