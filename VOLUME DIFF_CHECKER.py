import trimesh

original = trimesh.load(r"D:\SOFTAGE\3. BUTTON\INPUTS\RetroPad - Button.stl")
generated = trimesh.load(r"D:\SOFTAGE\3. BUTTON\FINAL CODE\BUTTON.stl")

print("Original Volume:", original.volume)
print("Generated Volume:", generated.volume)

difference = abs(original.volume - generated.volume)

print("Volume Difference:", difference)

