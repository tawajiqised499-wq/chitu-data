# 赤兔数据

赤兔数据是一个专业的足球博彩分析系统，提供赔率数据收集、趋势分析和投注价值识别。

## 主要功能

- **赔率数据收集**: 从多个博彩公司收集实时赔率数据
- **趋势分析**: 分析赔率变化趋势，识别市场热度
- **投注价值识别**: 找出有投注价值的比赛机会
- **数据存储**: 将历史数据保存用于后续分析
- **预测模型**: 基于历史数据进行比赛预测

## 系统要求

- Python 3.8+
- pip (Python 包管理工具)

## 安装步骤

1. 克隆仓库到本地:
```bash
git clone https://github.com/tawajiqised499-wq/chitu-data.git
cd chitu-data
```

2. 安装依赖包:
```bash
pip install -r requirements.txt
```

## 使用方法

运行程序的主文件:
```bash
python main.py
```

按照程序菜单提示进行操作即可。

## 项目结构

```
chitu-data/
├── main.py              # 程序入口
├── requirements.txt     # 项目依赖
├── config/              # 配置文件
├── crawler/             # 数据爬虫模块
├── analyzer/            # 数据分析模块
├── models/              # 预测模型
├── data/                # 数据存储目录
└── logs/                # 日志文件目录
```

## 免责声明

本项目仅供学习和研究使用，用户需自行承担使用本项目的所有责任。请遵守当地法律法规。

## 许可证

MIT License