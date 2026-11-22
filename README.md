# pairwise-ssr-roughness-step

## 领域

游戏、图形与多媒体

## 主题

SSR 粗糙度步长

## 说明

步长随粗糙度、射线抖动与探针回退。

初始状态下 `render/ssr_roughness_step.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
