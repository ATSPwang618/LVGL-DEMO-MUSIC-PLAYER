# PSV-LVGL-DEMO MUSIC PLAYER

![图片描述](https://github.com/ATSPwang618/LVGL-DEMO-MUSIC-PLAYER/blob/main/%E6%BC%94%E7%A4%BA%E6%88%AA%E5%9B%BE/1.png)

#### 介绍
这只是lvgl的一个Demo

移植作者：@刘斌
开源地址：https://gitee.com/chumenzuoguai/psv_lvgl9

#### 软件架构

1.暂时未使用GPU做渲染，仅使用SDL2渲染
帧数偏低，但是我相信使用gxm渲染后帧数会大大提示！

2.跑的只是一个demo，纯ui界面，没有集成 PSVita 音频 API (SceAudio)，也没有添加音频解码库（如 libvorbis, libmpg123 等）以及实现文件系统访问和音频文件读取，


#### 安装教程

1.sdk：https://vitasdk.org/

2.环境搭建教程：https://www.bilibili.com/video/BV1KG41137iE/?spm_id_from=333.337.search-card.all.click

3.演示 https://www.bilibili.com/video/BV1Vpnrz3Eig/?spm_id_from=333.1387.homepage.video_card.click


#### 使用说明

1. 需要linux 环境,可以是wsl
2. 需要配置网络环境访问代理，否则下载不了sdk


#### 构建方法

```bash
cd psv_lvgl9
mkdir -p build
cd build
cmake ..
make -j$(nproc)
```
