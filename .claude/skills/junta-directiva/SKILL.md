---
name: junta-directiva
description: Convoca a la junta directiva simulada de un grupo global de gestión de activos (tipo BlackRock) — Presidente, Consejero Líder Independiente, comités de Auditoría, Riesgos, Compensación y Gobierno/Sostenibilidad, más CIO, Estratega Macro, Mercados Privados y Tecnología como invitados — para deliberar y votar sobre un asunto, y produce un acta con resolución, votos, condiciones y mandatos. Úsalo cuando el usuario pida la opinión o el voto de "la junta", "el board", "el consejo de administración" o "los directores" sobre una estrategia, adquisición, producto de inversión o tesis de mercado.
argument-hint: "<asunto a someter a la junta>"
---

# Sesión de la Junta Directiva

Asunto: $ARGUMENTS

Si el asunto está vacío o es ambiguo, pide al usuario el asunto, el contexto (cifras, jurisdicciones, horizonte) y si se trata de una decisión para aprobar o de una consulta estratégica, antes de convocar.

> Junta **simulada y ficticia**. Los miembros no representan a personas ni firmas reales. Nada de lo que produzca es asesoría de inversión ni orden de operar.

## Procedimiento

1. **Orden del día.** Reformula el asunto como una moción concreta ("Se propone que el Grupo ...") e identifica la información faltante. Anota supuestos explícitos (cifras, mercado, jurisdicción, horizonte).

2. **Quórum.** El Consejero Líder Independiente asiste siempre (contrapeso). Añade los demás según el asunto (normalmente 5–7 en total):
   - Adquisición o fusión → `junta-comite-auditoria`, `junta-comite-riesgos`, `junta-comite-compensacion`, `junta-mercados-privados` y/o `junta-tecnologia-plataforma` según el objetivo
   - Nuevo producto de inversión (ETF, fondo, vehículo semilíquido, activos digitales) → `junta-cio`, `junta-comite-riesgos`, `junta-comite-gobierno-sostenibilidad`, `junta-estratega-macro`
   - Tesis de mercado / asignación de activos / impacto del ciclo → `junta-estratega-macro`, `junta-cio`, `junta-comite-riesgos`, `junta-comite-auditoria`
   - Dividendos, recompras, deuda, presupuesto → `junta-comite-auditoria`, `junta-comite-riesgos`, `junta-estratega-macro`
   - Sucesión, compensación ejecutiva, talento → `junta-comite-compensacion`, `junta-comite-gobierno-sostenibilidad`, `junta-comite-auditoria`
   - Stewardship, voto, ESG, reputación, escrutinio político → `junta-comite-gobierno-sostenibilidad`, `junta-comite-riesgos`, `junta-cio`
   - Tecnología, IA, ciberseguridad, tokenización, este repositorio → `junta-tecnologia-plataforma`, `junta-comite-riesgos`, `junta-cio`
   Si el usuario pide "la junta completa", convoca a todos.

3. **Deliberación en paralelo.** Lanza a los miembros seleccionados con la herramienta Agent en un mismo mensaje (uno por miembro, `subagent_type` = el nombre del agente). A cada uno pásale la moción, el contexto completo y los supuestos, y pídele su respuesta y voto en su formato estándar.

4. **Réplica (opcional).** Si hay votos opuestos sobre un punto material, comparte al Consejero Líder Independiente las posiciones en conflicto y pídele una réplica breve antes de consolidar.

5. **Resolución.** Lanza a `junta-presidente` con las respuestas completas de todos y pídele: consensos, disensos y cómo se resuelven, conteo de votos, resolución en formato de acta, condiciones y mandatos a la gerencia.

6. **Entrega al usuario** como acta:
   - **Moción** y **Resolución** ("La Junta resuelve...": aprobada / aprobada con condiciones / rechazada / aplazada pendiente de información) y nivel de confianza.
   - **Votos** — tabla miembro | voto | argumento principal (una línea).
   - **Disensos** y cómo se resolvieron.
   - **Condiciones y salvaguardas.**
   - **Riesgos principales** y mitigaciones.
   - **Mandatos a la gerencia** con responsable y plazo, y fecha de revisión.
   - **Información faltante** que podría cambiar la resolución.

No ejecutes acciones externas (órdenes en el bróker, correos, firmas, publicaciones) a partir de la resolución sin confirmación explícita del usuario.
