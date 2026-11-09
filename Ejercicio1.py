curso_A = {
    "Ana", "Carlos", "Laura", "Pedro",
    "Sofia", "Andres", "Camila"
}

curso_B = {
    "Laura", "Pedro", "Daniel", "Sofia",
    "Mateo", "Valentina"
}


def mostrar_resultados(curso_A, curso_B):
    print("\n===== ESTUDIANTES POR CURSO =====")
    print("Curso A (Fundamentos de programación):", curso_A)
    print("Curso B (Introducción a bases de datos):", curso_B)

    todos = curso_A | curso_B
    print("\nEstudiantes diferentes inscritos:", len(todos))
    print("Listado:", todos)

    ambos = curso_A & curso_B
    print("\nEstudiantes inscritos en ambos cursos:", ambos)

    solo_A = curso_A - curso_B
    print("Estudiantes inscritos únicamente en el curso A:", solo_A)

    solo_B = curso_B - curso_A
    print("Estudiantes inscritos únicamente en el curso B:", solo_B)

    solo_uno = curso_A ^ curso_B
    print("Estudiantes inscritos en exactamente un curso:", solo_uno)

    if curso_A <= curso_B:
        print("\nTodos los estudiantes del curso A también están en el curso B.")
    else:
        print("\nNo todos los estudiantes del curso A están inscritos en el curso B.")


mostrar_resultados(curso_A, curso_B)

while True:
    print("\n===== AGREGAR ESTUDIANTE =====")
    curso = input("¿A qué curso desea agregarlo? (A o B): ").strip().upper()
    while curso != "A" and curso != "B":
        print("Curso no válido.")
        curso = input("¿A qué curso desea agregarlo? (A o B): ").strip().upper()

    nombre = input("Ingrese el nombre del estudiante: ").strip().title()

    if curso == "A":
        curso_A.add(nombre)
    else:
        curso_B.add(nombre)

    print("\nEstudiante agregado. Resultados actualizados:")
    mostrar_resultados(curso_A, curso_B)

    continuar = input("\n¿Desea agregar otro estudiante? (sí/no): ").strip().lower()
    if continuar in ["no", "n"]:
        print("¡Proceso finalizado!")
        break
