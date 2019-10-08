CFLAGS=$(pkg-config --cflags sdl2)
LDFLAGS=$(pkg-config --libs sdl2)
gcc -c main.c -o main.o $CFLAGS
gcc main.o -o main $LDFLAGS
gcc sdltest.c -o sdltest $CFLAGS $LDFLAGS
