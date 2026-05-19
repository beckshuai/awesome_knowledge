# awesome_knowledge

一个持续扩展的知识图谱仓库，用来沉淀不同主题下的**观点、人物、著作、关系网络与发展轨迹**，并同时提供可交互 HTML 页面用于浏览。

## 在线入口

- GitHub Pages 首页：<https://beckshuai.github.io/awesome_knowledge/>
- GitHub 仓库：<https://github.com/beckshuai/awesome_knowledge>

## 当前已上线主题

### 1. 孩子教育知识图谱

- 在线访问：<https://beckshuai.github.io/awesome_knowledge/knowledge_graphs/child_education/>
- 本地目录：`knowledge_graphs/child_education/`
- 内容方向：心理学、人类学、脑科学

包含：

- 交互式知识图谱
- 发展轨迹视图
- 关联关系浏览
- 结构化数据文件 `graph.json`
- 来源文件 `sources.json`

### 2. 经济学知识图谱

- 在线访问：<https://beckshuai.github.io/awesome_knowledge/knowledge_graphs/economics/>
- 本地目录：`knowledge_graphs/economics/`

包含：

- 学派 / 人物 / 概念关系图
- 思想史时间线
- 关系说明与交互浏览
- 结构化数据文件 `graph.json`
- 来源文件 `sources.json`

## 项目结构

```text
awesome_knowledge/
├── index.html                       # 总导航首页 / GitHub Pages 入口
├── README.md                        # 项目说明
└── knowledge_graphs/
    ├── child_education/
    │   ├── index.html               # 孩子教育交互图谱
    │   ├── graph.json               # 图谱结构化数据
    │   └── sources.json             # 资料来源
    └── economics/
        ├── index.html               # 经济学交互图谱
        ├── graph.json               # 图谱结构化数据
        └── sources.json             # 资料来源
```

## 本地运行

由于页面内部通过 `fetch()` 加载 JSON 数据，不建议直接双击 HTML 文件。

推荐在仓库根目录启动本地静态服务器：

```bash
cd "/Users/bytedance/repos/github/awesome_knowledge"
python3 -m http.server 8000
```

然后在浏览器打开：

```text
http://localhost:8000
```

这样可以直接从首页进入所有图谱页面。

## 首页能力

首页 `index.html` 目前支持：

- 统一导航入口
- 图谱实时预览
- 搜索
- 分类筛选
- 未来图谱目录
- GitHub Pages 与本地运行说明

## 后续可扩展方向

- 学习科学知识图谱
- 家庭与社会化知识图谱
- AI 与知识表示图谱
- 哲学与教育观知识图谱

## 说明

这个仓库当前更偏向“静态站点 + 结构化数据”的知识组织方式。后续如果需要，可以进一步扩展为：

- 更多主题图谱
- 统一搜索页
- 自动生成截图或预览图
- 图谱之间的跨主题链接
- 更完整的知识库首页与目录系统
