## 指南

[指南](http://blog.csdn.net/xluren/article/details/41115045)

setup 中完整的参数及说明可以看 [http://docs.python.org/distutils/setupscript.html#additional-meta-data](http://docs.python.org/distutils/setupscript.html#additional-meta-data)

disutils详细说明看 [https://docs.python.org/2/distutils/index.html](https://docs.python.org/2/distutils/index.html)

## 命令详解

```cmd
# 以下所有生成文件将在当前路径下 dist 目录中
python setup.py bdist_egg # 生成easy_install支持的格式 
python setup.py sdist     # 生成pip支持的格式，下文以此为例
python setup.py register  # 注册package
python setup.py sdist upload # 上传文件
```

pypi还有一个测试服务器，可以在这个测试服务器上做测试，测试的时候需要给命令指定额外的"-r"或"-i"选项，如

```cmd
python setup.py register -r "https://testpypi.python.org/pypi"
python setup.py sdist upload -r "https://testpypi.python.org/pypi"
pip install -i "https://testpypi.python.org/pypi" simpletest。
```

发布到测试服务器的时候，建议在linux或cygwin中发布，如果是在windows中，参考文档，需要生成.pypirc文件