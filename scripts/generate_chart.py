
import matplotlib.pyplot as plt
import numpy as np

# Skill labels
labels = [
    "Web Security",
    "Pentesting",
    "Bug Hunting",
    "Python",
    "Linux",
    "GitHub"
]

# Skill levels (0–10 scale)
values = [9, 8, 8, 7, 8, 7]
values += values[:1]  # Close the loop

angles = np.linspace(0, 2 * np.pi, len(values))

plt.figure(figsize=(6, 6))
ax = plt.subplot(111, polar=True)

# Draw chart
ax.plot(angles, values, linewidth=2, linestyle='solid')
ax.fill(angles, values, alpha=0.3)

# Add labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

# Title
plt.title("Deepak Singh — Skill Radar Chart", size=14, pad=20)

# Save chart
plt.savefig("skill_chart.png", dpi=300, bbox_inches="tight")
