# get_goal_str_from_chrome
使用python3控制chrome，并从网页上提取到需要的内容

## 依赖
从http://chromedriver.storage.googleapis.com/index.html 添加与电脑chrome对因版本的chromedriver.exe，放到chrome安装目录下

```
$ pip3 install Cython
$ pip3 install lxml
$ pip3 install selenium
$ pip3 install Splinter
```

并在chrome的快捷方式上添加 --remote-debugging-port=9222