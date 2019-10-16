CFLAGS="${CFLAGS} $(pkg-config --cflags sdl2)"
LDFLAGS="${LDFLAGS} $(pkg-config --libs sdl2)"

FILES="main vector"

for FILE in $FILES
do
    OBJS="${OBJS} ${FILE}.o"
done

for FILE in $FILES
do
    gcc -c ${FILE}.c -o ${FILE}.o $CFLAGS
done

gcc ${OBJS} -o 3d.exe $LDFLAGS

