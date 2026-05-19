#!/usr/bin/env python3

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "knowledge_graphs" / "catalog.json"
README_PATH = ROOT / "README.md"


def build_readme(catalog: dict) -> str:
    pages_url = catalog["metadata"]["pages_url"]
    repo_url = catalog["metadata"]["repo_url"]
    live_topics = catalog["live_topics"]
    future_topics = catalog["future_topics"]

    lines = [
        "# awesome_knowledge",
        "",
        "一个持续扩展的知识图谱仓库，用来沉淀不同主题下的**观点、人物、著作、关系网络与发展轨迹**，并同时提供可交互 HTML 页面用于浏览。",
        "",
        "## 在线入口",
        "",
        f"- GitHub Pages 首页：<{pages_url}>",
        f"- GitHub 仓库：<{repo_url}>",
        "",
        "## 当前已上线主题",
        "",
    ]

    for index, topic in enumerate(live_topics, start=1):
        lines.extend([
            f"### {index}. {topic['title']}",
            "",
            f"- 在线访问：<{pages_url}{topic['path'].replace('./', '')}>",
            f"- 本地目录：`{topic['path'].replace('./', '')}`",
        ])
        if topic.get("tags"):
            lines.append(f"- 内容方向：{'、'.join(topic['tags'])}")
        lines.extend([
            "",
            "包含：",
            "",
        ])
        for feature in topic.get("features", []):
            lines.append(f"- {feature}")
        lines.append(f"- 结构化数据文件 `{topic['data_path'].replace('./', '')}`")
        slug = topic["slug"]
        source_path = f"knowledge_graphs/{slug}/sources.json"
        if (ROOT / source_path).exists():
            lines.append(f"- 来源文件 `{source_path}`")
        lines.extend(["", ""])

    lines.extend([
        "## 未来图谱目录",
        "",
        "以下主题已经进入总站目录管理，首页与 README 通过同一份 `knowledge_graphs/catalog.json` 统一维护：",
        "",
    ])
    for topic in future_topics:
        lines.append(f"- **{topic['title']}**（{topic['status']}）：`{topic['path'].replace('./', '')}`")
    lines.extend([
        "",
        "## 项目结构",
        "",
        "```text",
        "awesome_knowledge/",
        "├── index.html                       # 总导航首页 / GitHub Pages 入口",
        "├── README.md                        # 项目说明（由 catalog 同步维护）",
        "├── scripts/",
        "│   └── sync_catalog.py              # 用统一目录数据生成 README",
        "└── knowledge_graphs/",
        "    ├── catalog.json                # 统一目录索引（已上线 + 未来主题）",
        "    ├── child_education/",
        "    │   ├── index.html               # 孩子教育交互图谱",
        "    │   ├── graph.json               # 图谱结构化数据",
        "    │   └── sources.json             # 资料来源",
        "    ├── economics/",
        "    │   ├── index.html               # 经济学交互图谱",
        "    │   ├── graph.json               # 图谱结构化数据",
        "    │   └── sources.json             # 资料来源",
        "    ├── learning_science/",
        "    │   ├── index.html               # 模板页",
        "    │   └── graph.json               # 空模板数据",
        "    ├── family_socialization/",
        "    │   ├── index.html               # 模板页",
        "    │   └── graph.json               # 空模板数据",
        "    ├── ai_knowledge_representation/",
        "    │   ├── index.html               # 模板页",
        "    │   └── graph.json               # 空模板数据",
        "    └── philosophy_education/",
        "        ├── index.html               # 模板页",
        "        └── graph.json               # 空模板数据",
        "```",
        "",
        "## 本地运行",
        "",
        "由于页面内部通过 `fetch()` 加载 JSON 数据，不建议直接双击 HTML 文件。",
        "",
        "推荐在仓库根目录启动本地静态服务器：",
        "",
        "```bash",
        f'cd "{ROOT}"',
        "python3 -m http.server 8000",
        "```",
        "",
        "然后在浏览器打开：",
        "",
        "```text",
        "http://localhost:8000",
        "```",
        "",
        "这样可以直接从首页进入所有图谱页面。",
        "",
        "## 首页能力",
        "",
        "首页 `index.html` 目前支持：",
        "",
        "- 统一导航入口",
        "- 图谱实时预览",
        "- 搜索",
        "- 分类筛选",
        "- 未来图谱目录",
        "- GitHub Pages 与本地运行说明",
        "- 主题统计与更新日志",
        "",
        "## 自动同步说明",
        "",
        "- 首页中的未来目录与统计信息来自 `knowledge_graphs/catalog.json`",
        "- README 通过 `scripts/sync_catalog.py` 基于同一份目录数据生成",
        "- 若未来目录有变更，可运行：",
        "",
        "```bash",
        "python3 scripts/sync_catalog.py",
        "```",
        "",
        "## 说明",
        "",
        "这个仓库当前更偏向“静态站点 + 结构化数据”的知识组织方式。后续如果需要，可以进一步扩展为：",
        "",
        "- 更多主题图谱",
        "- 统一搜索页",
        "- 自动生成截图或预览图",
        "- 图谱之间的跨主题链接",
        "- 更完整的知识库首页与目录系统",
        "",
    ])
    return "\n".join(lines)


def main() -> None:
    catalog = json.loads(CATALOG_PATH.read_text())
    README_PATH.write_text(build_readme(catalog))
    print(f"Synced README from {CATALOG_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
