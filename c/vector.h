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

