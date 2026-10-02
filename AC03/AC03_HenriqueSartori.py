import bpy
import math

# Busca a coleção da atividade
colecao = bpy.data.collections.get("AC03_transformacoes")

# ========================================================
# OBJETO 2D CRIADO POR PYTHON
# ========================================================

bpy.ops.mesh.primitive_circle_add(
    vertices=32,
    radius=1,
    fill_type='NGON',
    location=(3, 2, 0)
)

circulo = bpy.context.active_object
circulo.name = "obj2d_circulo_script"

# Move para a coleção correta
for c in list(circulo.users_collection):
    c.objects.unlink(circulo)

colecao.objects.link(circulo)

# Transformações via Python
circulo.location = (3, 2, 0)
circulo.rotation_euler = (
    0,
    0,
    math.radians(30)
)
circulo.scale = (1.2, 0.8, 1.0)


# ========================================================
# OBJETO 3D CRIADO POR PYTHON
# ========================================================

bpy.ops.mesh.primitive_uv_sphere_add(
    location=(3, 0, 1.2)
)

esfera = bpy.context.active_object
esfera.name = "obj3d_esfera_script"

# Move para a coleção correta
for c in list(esfera.users_collection):
    c.objects.unlink(esfera)

colecao.objects.link(esfera)

# Transformações via Python
esfera.location = (3, 0, 1.2)

esfera.rotation_euler = (
    math.radians(25),
    math.radians(35),
    math.radians(15)
)

esfera.scale = (
    0.8,
    1.2,
    1.0
)

print("Objetos da AC03 criados com sucesso!")
