#ifdef FIXED

typedef struct
{
    union
    {
        struct
        {
            short x;
            short y;
            short z;
            short w;
        };
        short v[4];
    };
} vector4;

typedef struct
{
    short x[4];
    short y[4];
    short z[4];
    short w[4];
} matrix4x4;

#else

typedef struct
{
    union
    {
        struct
        {
            float x;
            float y;
            float z;
            float w;
        };
        float v[4];
    };
} vector4;

typedef struct
{
    float x[4];
    float y[4];
    float z[4];
    float w[4];
} matrix4x4;
#endif

vector4 *transform(matrix4x4 *m,vector4 *vin,vector4 *vout);
vector4 *project(vector4 *vin);
void dump_vector(vector4 *vin);
void dump_matrix(matrix4x4 *m);

void vector4_setx(vector4 *v,float x);
void vector4_sety(vector4 *v,float y);
void vector4_setz(vector4 *v,float z);
void vector4_setw(vector4 *v,float w);
float vector4_getx(vector4 *v);
float vector4_gety(vector4 *v);
void matrix4x4_set(matrix4x4 *m,int i, int j,float f);