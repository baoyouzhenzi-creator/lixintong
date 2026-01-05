import matplotlib.pyplot as plt
import numpy as np

# 设置绘图风格和中文显示
plt.rcParams['font.sans-serif'] = ['SimHei'] 
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('ggplot')

# 创建画布，包含 1 行 2 列
fig = plt.subplots(figsize=(14, 6))

# --- 左侧子图：性能测试对比 (柱状+折线图) ---
ax1 = plt.subplot(121)
labels = ['CBAC 关闭', 'CBAC 启用']
time_data = [12.3, 12.7]         # 传输时间 (s)
rate_data = [65.04, 63.0]        # 传输速率 (Mbps)
x = np.arange(len(labels))
width = 0.4

# 绘制左轴-传输时间
bars = ax1.bar(x, time_data, width, color='steelblue', alpha=0.7, label='传输时间 (s)')
ax1.set_ylabel('时间 (秒)', color='steelblue', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(labels)
ax1.set_ylim(0, 16)

# 绘制右轴-平均速率
ax1_2 = ax1.twinx()
ax1_2.plot(x, rate_data, marker='D', color='firebrick', linewidth=2, label='平均速率 (Mbps)')
ax1_2.set_ylabel('速率 (Mbps)', color='firebrick', fontsize=12)
ax1_2.set_ylim(50, 70)

# 添加数值标签
ax1.bar_label(bars, padding=3)
for i, v in enumerate(rate_data):
    ax1_2.text(i, v + 0.5, f'{v}', ha='center', color='firebrick', fontweight='bold')

ax1.set_title('图 A：启用前后网络性能对比', fontsize=14, pad=15)
ax1.legend(loc='upper left')
ax1_2.legend(loc='upper right')

# --- 右侧子图：安全维度对比 (雷达图) ---
ax2 = plt.subplot(122, polar=True)
categories = ['状态感知', '安全性', '配置灵活性', '协议兼容性', '可用性', '维护成本']
n_attr = len(categories)

# 评分数据
static_acl = [2, 3, 4, 3, 5, 3]
cbac_scheme = [9, 8, 7, 8, 9, 8]

angles = np.linspace(0, 2 * np.pi, n_attr, endpoint=False).tolist()
static_acl += static_acl[:1]
cbac_scheme += cbac_scheme[:1]
angles += angles[:1]

# 绘制雷达图
ax2.fill(angles, static_acl, color='grey', alpha=0.2, label='传统静态 ACL')
ax2.plot(angles, static_acl, color='grey', linewidth=1.5, linestyle='--')

ax2.fill(angles, cbac_scheme, color='seagreen', alpha=0.3, label='本设计方案 (CBAC)')
ax2.plot(angles, cbac_scheme, color='seagreen', linewidth=2.5)

ax2.set_xticks(angles[:-1])
ax2.set_xticklabels(categories, fontsize=11)
ax2.set_yticklabels([]) # 隐藏极轴数值
ax2.set_title('图 B：方案综合安全维度评估', fontsize=14, pad=30)
ax2.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))

plt.tight_layout()
plt.show()