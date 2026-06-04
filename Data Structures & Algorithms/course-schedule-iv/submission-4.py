from typing import List
from collections import defaultdict


class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]],
    ) -> List[bool]:
        # Grafo invertido: para cada curso, listamos sus prerequisitos directos.
        # Si [pre, course] significa "pre es prerequisito de course",
        # entonces direct_prereqs[course] contiene a pre.
        direct_prereqs: dict[int, List[int]] = defaultdict(list)
        for prereq, course in prerequisites:
            direct_prereqs[course].append(prereq)

        # Cache: para cada curso, el conjunto de TODOS sus prerequisitos
        # (directos e indirectos), más el propio curso.
        # Incluir el curso mismo simplifica la unión durante el DFS:
        # al subir por la cadena, cada nodo aporta su clausura completa.
        transitive_prereqs: dict[int, set[int]] = {}

        def collect_prereqs(course: int) -> set[int]:
            # Memoización: si ya lo calculamos, lo devolvemos.
            if course in transitive_prereqs:
                return transitive_prereqs[course]

            # Reservamos el set ANTES de recursar.
            # En un DAG válido no hay ciclos, pero esto también nos protege
            # de loops infinitos si los hubiera.
            transitive_prereqs[course] = set()

            for prereq in direct_prereqs[course]:
                # Unimos la clausura del prerequisito directo.
                # Como collect_prereqs(prereq) ya incluye a prereq mismo,
                # no hace falta agregarlo aparte.
                transitive_prereqs[course] |= collect_prereqs(prereq)

            # El curso es prerequisito de sí mismo a efectos de propagación
            # hacia arriba (ver comentario del cache).
            transitive_prereqs[course].add(course)
            return transitive_prereqs[course]

        # Precomputamos la clausura transitiva para cada curso.
        # Costo: O(V * E) en el peor caso, O(1) por query después.
        for course in range(numCourses):
            collect_prereqs(course)

        # Para [u, v] preguntamos: "¿u es prerequisito de v?"
        # Equivale a: ¿u está en el conjunto de prereqs transitivos de v?
        return [u in transitive_prereqs[v] for u, v in queries]