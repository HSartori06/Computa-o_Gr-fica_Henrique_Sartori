import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

OUT = Path("graficos_ac02")
OUT.mkdir(exist_ok=True)

def finish(title, filename):
    plt.title(title)
    plt.axhline(0, linewidth=0.8)
    plt.axvline(0, linewidth=0.8)
    plt.grid(True)
    plt.axis("equal")
    plt.legend()
    plt.savefig(OUT / filename, dpi=160, bbox_inches="tight")
    plt.close()

def plot_point(original, transformed, title, filename):
    plt.figure()
    plt.scatter([original[0]], [original[1]], label=f"Original {tuple(original)}")
    plt.scatter([transformed[0]], [transformed[1]], label=f"Transformado {tuple(np.round(transformed, 4))}")
    finish(title, filename)

def plot_polygon(original, transformed, title, filename):
    original = np.asarray(original, dtype=float)
    transformed = np.asarray(transformed, dtype=float)
    o = np.vstack([original, original[0]])
    t = np.vstack([transformed, transformed[0]])
    plt.figure()
    plt.plot(o[:,0], o[:,1], marker="o", label="Original")
    plt.plot(t[:,0], t[:,1], marker="o", linestyle="--", label="Transformado")
    finish(title, filename)

# 1 — Translação
P = np.array([2.0, 3.0])
P1 = P + np.array([4.0, -2.0])
plot_point(P, P1, "Exercício 1 — Translação", "ex01_translacao.png")

# 2 — Escala uniforme
tri = np.array([[1,1], [3,1], [2,4]], dtype=float)
tri2 = tri * 2
plot_polygon(tri, tri2, "Exercício 2 — Escala uniforme", "ex02_escala_uniforme.png")

# 3 — Escala não uniforme
S = np.array([2.0, 0.5])
tri3 = tri * S
plot_polygon(tri, tri3, "Exercício 3 — Escala não uniforme", "ex03_escala_nao_uniforme.png")

# 4 — Rotação 90° anti-horária
theta = np.radians(90)
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])
P = np.array([1.0, 0.0])
P4 = R @ P
plot_point(P, P4, "Exercício 4 — Rotação 90°", "ex04_rotacao_90.png")

# 5 — Quadrado, rotação 45° horário
square = np.array([[1,1], [1,4], [4,4], [4,1]], dtype=float)
theta = np.radians(-45)
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])
square5 = square @ R.T
plot_polygon(square, square5, "Exercício 5 — Rotação -45°", "ex05_rotacao_quadrado.png")

# 6 — Reflexão no eixo y
P = np.array([2.0, 5.0])
P6 = np.array([-P[0], P[1]])
plot_point(P, P6, "Exercício 6 — Reflexão no eixo y", "ex06_reflexao_y.png")

# 7 — Reflexão no eixo x
tri7 = np.array([[2,3], [4,3], [3,5]], dtype=float)
tri7_ref = tri7 * np.array([1.0, -1.0])
plot_polygon(tri7, tri7_ref, "Exercício 7 — Reflexão no eixo x", "ex07_reflexao_x.png")

# 8 — Cisalhamento horizontal
P = np.array([2.0, 3.0])
k = 2.0
H = np.array([[1.0, k],
              [0.0, 1.0]])
P8 = H @ P
plot_point(P, P8, "Exercício 8 — Cisalhamento horizontal", "ex08_cisalhamento.png")

# 9 — Composição
P = np.array([3.0, 2.0])
p9_t = P + np.array([1.0, -1.0])
theta = np.radians(90)
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta),  np.cos(theta)]])
p9_r = R @ p9_t
p9_f = 2 * p9_r

plt.figure()
plt.scatter([P[0]], [P[1]], label="Original")
plt.scatter([p9_t[0]], [p9_t[1]], label="Após translação")
plt.scatter([p9_r[0]], [p9_r[1]], label="Após rotação")
plt.scatter([p9_f[0]], [p9_f[1]], label="Final")
finish("Exercício 9 — Composição", "ex09_composicao.png")

# 10 — Retângulo: translação -> escala -> reflexão y
rect = np.array([[1,1], [5,1], [5,3], [1,3]], dtype=float)
rect_t = rect + np.array([-2.0, 3.0])
rect_s = rect_t * np.array([1.5, 0.5])
rect_f = rect_s * np.array([-1.0, 1.0])

plt.figure()
for points, label, linestyle in [
    (rect, "Original", "-"),
    (rect_t, "Após translação", "--"),
    (rect_s, "Após escala", "-."),
    (rect_f, "Final", ":"),
]:
    closed = np.vstack([points, points[0]])
    plt.plot(closed[:,0], closed[:,1], marker="o", linestyle=linestyle, label=label)
finish("Exercício 10 — Combinação de transformações", "ex10_combinacao.png")

print("Resultados numéricos:")
print("Ex1:", P1)
print("Ex2:", tri2)
print("Ex3:", tri3)
print("Ex4:", np.round(P4, 4))
print("Ex5:", np.round(square5, 4))
print("Ex6:", P6)
print("Ex7:", tri7_ref)
print("Ex8:", P8)
print("Ex9:", np.round(p9_f, 4))
print("Ex10:", rect_f)
print(f"\nGráficos salvos em: {OUT.resolve()}")
