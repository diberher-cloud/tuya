---
name: comite-ejecutivo
description: Convoca al staff ejecutivo de la fintech (CEO, CFO, CTO, CRO, CCO, General Counsel, CISO, COO, CMO, CPO, CHRO) para analizar un tema, y consolida sus opiniones en una decisión con plan de acción. Úsalo cuando el usuario pida la opinión del comité, del board, del staff o de "los C-levels" sobre una iniciativa, problema o decisión.
argument-hint: "<tema o decisión a analizar>"
---

# Comité ejecutivo

Tema a tratar: $ARGUMENTS

Si el tema está vacío o es ambiguo, pide al usuario el tema, el país/jurisdicción y los datos disponibles antes de convocar.

## Procedimiento

1. **Encuadre.** Reformula el tema en una pregunta de decisión concreta e identifica qué información falta. Anota los supuestos (país, producto, etapa de la compañía, cifras).

2. **Selección del quórum.** Elige solo a los ejecutivos relevantes (normalmente 3–6). Guía:
   - Nuevo producto financiero → CPO, CFO, CRO, CCO, CMO, CTO
   - Fundraising / presupuesto → CFO, CEO, General Counsel
   - Incidente de seguridad o fraude → CISO, CRO, CCO, General Counsel, COO
   - Expansión a un país → CCO, General Counsel, CFO, CMO, CTO, COO, CHRO
   - Alianza / contrato con tercero → General Counsel, CFO, CTO, CISO, CCO
   - Organización, talento, compensación o reestructuración → CHRO, CFO, General Counsel, CEO
   - Cambio técnico en este repositorio → CTO, CISO (+ CPO si cambia el producto)

3. **Convocatoria en paralelo.** Lanza a los subagentes seleccionados con la herramienta Agent en un mismo mensaje (uno por ejecutivo, `subagent_type` = `cfo`, `cto`, `cro`, `cco`, `general-counsel`, `ciso`, `coo`, `cmo`, `cpo`, `chro`). A cada uno pásale: la pregunta de decisión, el contexto completo y los supuestos, y pídele su respuesta en su formato estándar.

4. **Síntesis del CEO.** Lanza al subagente `ceo` con las respuestas completas de los demás y pídele que: identifique consensos, haga explícitos los desacuerdos y cómo los resuelve, tome una decisión y arme el plan.

5. **Entrega al usuario** con esta estructura:
   - **Decisión** (1–3 líneas) y nivel de confianza.
   - **Posición de cada ejecutivo** (una línea cada uno).
   - **Desacuerdos y cómo se resolvieron.**
   - **Riesgos principales y mitigaciones.**
   - **Plan 30/60/90 días** con responsables.
   - **Información faltante** que cambiaría la decisión.

No ejecutes acciones externas (correos, operaciones, firmas, publicaciones) a partir de las recomendaciones sin confirmación explícita del usuario.
