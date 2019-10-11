#include "SDL.h"
#include "vector.h"
#include <stdio.h>

#define DEBUG() printf("DEBUG: %d\n",__LINE__)

char colormap[8][3];

vector4 cube[8];

matrix4x4 movecube;

void move_cube()
{
    movecube.x[0]=1;
    movecube.y[1]=1;
    movecube.z[2]=1;
    movecube.w[3]=1;
    movecube.z[3]=2.5;
}

void make_cube(vector4 *cube)
{
    int i;
    float x = -.5;
    float y = -.5; 
    float z = -.5;
    float w = 1.0;
    for(i=0;i<8;i++)
    {
        cube[i].x = x+!!(i&1);
        cube[i].y = y+!!(i&2);
        cube[i].z = z+!!(i&4);
        cube[i].w = w;
    }
}

void setcolor(char color,char r,char g,char b)
{
    colormap[color][0]=r;
    colormap[color][1]=g;
    colormap[color][2]=b;
}

void make_colors()
{
    int i;
    for(i=0;i<8;i++)
    {
        setcolor(i,16*i,16*i,16*i);
    }
}

void drawpixel(unsigned char *pxbuf,int x, int y,char color,int pitch)
{
    int i;
    int offset;
    if(color<0)
    {
        return;
    }
    offset = y * pitch + x * 4;
    for(i=0;i<3;i++)
    {
        pxbuf[offset+i]=colormap[color][i];
    }
}

void draw(unsigned char *pxbuf,int pitch)
{
    vector4 n;
    int i;
    int x;
    int y;
    for(i=0;i<8;i++)
    {

        transform(&movecube,&cube[i],&n);
        project(&n);
        x = n.x*320+320;
        y = 240-n.y*240;
        drawpixel(pxbuf,x,y,7,pitch);
    }
    //drawpixel(pxbuf,5,5,1,pitch);
    //drawpixel(pxbuf,5,6,1,pitch);
    //drawpixel(pxbuf,6,5,1,pitch);
    //drawpixel(pxbuf,6,6,1,pitch);
}

int main(int argc, char* argv[]) {

    SDL_Window *window;                    // Declare a pointer
    SDL_Surface *surface;
    
    SDL_Event e;

    SDL_Init(SDL_INIT_VIDEO);              // Initialize SDL2

    // Create an application window with the following settings:
    window = SDL_CreateWindow(
        "An SDL2 window",                  // window title
        SDL_WINDOWPOS_UNDEFINED,           // initial x position
        SDL_WINDOWPOS_UNDEFINED,           // initial y position
        640,                               // width, in pixels
        480,                               // height, in pixels
        SDL_WINDOW_OPENGL                  // flags - see below
    );

    // Check that the window was successfully created
    if (window == NULL) {
        // In the case that the window could not be made...
        printf("Could not create window: %s\n", SDL_GetError());
        return 1;
    }

    make_colors();
    make_cube(cube);
    move_cube();

    surface = SDL_GetWindowSurface( window );

    while(1)
    {
        if(SDL_PollEvent(&e))
        {
            if(e.type == SDL_QUIT)
            {
                break;
            }
        }
        //Fill the surface white
        SDL_FillRect( surface, NULL, SDL_MapRGB( surface->format, 0, 0, 0 ) );
        draw(surface->pixels,surface->pitch);
        
        //Update the surface
        SDL_UpdateWindowSurface( window );
    }

    // Close and destroy the window
    SDL_DestroyWindow(window);

    // Clean up
    SDL_Quit();
    return 0;
}

