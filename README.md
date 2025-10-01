# psv_lvgl9

#### 介绍
LVGL 是最流行的免费开源嵌入式图形库，可为任何 MCU、MPU 和显示类型创建漂亮的 UI。 从消费电子产品到工业自动化，任何应用程序都可以利用 LVGL 的 30 多个内置小部件、100 多个样式属性、受网络启发的布局以及支持多种语言的排版系统。

移植作者：@刘斌
开源地址：https://gitee.com/chumenzuoguai/psv_lvgl9

#### 软件架构

1.暂时未使用GPU做渲染，仅使用SDL2渲染
帧数偏低，但是我相信使用gxm渲染后帧数会大大提示！

#### 安装教程

1.sdk：https://vitasdk.org/
2.环境搭建教程：https://www.bilibili.com/video/BV1KG41137iE/?spm_id_from=333.337.search-card.all.click
3.演示 https://www.bilibili.com/video/BV1Vpnrz3Eig/?spm_id_from=333.1387.homepage.video_card.click

#### 使用说明

1. 需要linux 环境,可以是wsl
2. 需要配置网络环境访问代理，否则下载不了sdk


#### 构建方法

进入项目目录后
mkdir -p build && cd build && cmake ..
build && make -j$(nproc)

生成文件在build目录下的为vpk格式