/*
 * @Author: bin.liu 2841208085@qq.com
 * @Date: 2025-09-28 22:21:55
 * @LastEditors: bin.liu 2841208085@qq.com
 * @LastEditTime: 2025-09-28 22:21:56
 */
#include <psp2/kernel/processmgr.h>
#include "../lvgl/lvgl.h"
#include "../lvgl/src/drivers/sdl/lv_sdl_window.h"
#include "../lvgl/examples/lv_examples.h"
#include "../lvgl/demos/lv_demos.h"
#include <SDL2/SDL.h>
#include <stdio.h>

/*
 * lvgl start
 */

static lv_display_t *display;
static lv_indev_t *mouse_indev;
static lv_indev_t *keyboard_indev;
static lv_indev_t *mousewheel_indev;

/**
 * 初始化SDL显示和输入设备
 */
void lvgl_sdl_init(void)
{
  /* 初始化LVGL */
  lv_init();

  /* 创建SDL窗口 */
  display = lv_sdl_window_create(960, 544);
  /* 创建鼠标输入设备 */
  mouse_indev = lv_sdl_mouse_create();
  lv_indev_set_display(mouse_indev, display);

  /* 创建键盘输入设备 */
  keyboard_indev = lv_sdl_keyboard_create();
  lv_indev_set_display(keyboard_indev, display);
}

/**
 * 主循环函数
 */
void lvgl_mainloop(void)
{
  while (1)
  {
    /* 处理LVGL任务 */
    lv_timer_handler();
    lv_tick_inc(8);
    /* 延时以控制刷新率 */
    SDL_Delay(8);
  }
}

/*
 * lvgl end
 */

// Screen dimension constants
//  enum {
//    SCREEN_WIDTH  = 960,
//    SCREEN_HEIGHT = 544
//  };

// SDL_Window    * gWindow   = NULL;
// SDL_Renderer  * gRenderer = NULL;

// SDL_Rect fillRect = { SCREEN_WIDTH  / 4,
// 		      SCREEN_HEIGHT / 4,
// 		      SCREEN_WIDTH  / 2,
// 		      SCREEN_HEIGHT / 2
// };

int main(int argc, char *argv[])
{
  // if( SDL_Init( SDL_INIT_VIDEO ) < 0 )
  //     return -1;

  // if ((gWindow = SDL_CreateWindow( "LVGL", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, SCREEN_WIDTH, SCREEN_HEIGHT, SDL_WINDOW_SHOWN)) == NULL)
  //   return -1;

  // if ((gRenderer = SDL_CreateRenderer( gWindow, -1, 0)) == NULL)
  //     return -1;

  // SDL_SetRenderDrawColor( gRenderer, 255,0,0,255);
  // SDL_RenderFillRect( gRenderer, &fillRect );
  // SDL_RenderPresent( gRenderer );
  // SDL_Delay(4000);
  // SDL_DestroyRenderer( gRenderer );
  // SDL_DestroyWindow( gWindow );
  // gWindow = NULL;
  // gRenderer = NULL;

  /* 初始化LVGL和SDL */
  lvgl_sdl_init();

  /* 启动音乐播放器Demo */
  lv_demo_music();
  
  /* 运行主循环 */
  lvgl_mainloop();

  SDL_Quit();
  return 0;
}
