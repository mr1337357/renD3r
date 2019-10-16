#include <stdint.h>
#define FDIV(a,b) (int16_t)((((int32_t)a)<<14)/b)
#define FMUL(a,b) (int16_t)(((int32_t)a*(int32_t)b)>>14)