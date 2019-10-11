CFLAGS=$(pkg-config --cflags sdl2)
LDFLAGS=$(pkg-config --libs sdl2)
gcc -c main.c -o main.o $CFLAGS
gcc -c vector.c -o vector.o $CFLAGS
gcc main.o vector.o -o main $LDFLAGS
gcc sdltest.c -o sdltest $CFLAGS $LDFLAGS
