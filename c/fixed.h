#include <stdint.h>
#define FDIV(a,b) (int16_t)((((int32_t)a)<<(FRACTIONBITS))/b)
#define FMUL(a,b) (int16_t)(((int32_t)a*(int32_t)b)>>(FRACTIONBITS))