# Junta directiva de agentes (gestora global de activos)

Subagentes de Claude Code que simulan la junta directiva de un grupo global de gestión
de activos de gran escala (estilo BlackRock: ETFs e indexación, gestión activa, mercados
privados y una plataforma tecnológica propia). Viven en `.claude/agents/junta-*.md`.

Es una junta **ficticia**: ningún miembro representa a una persona o firma real, y sus
resoluciones no son asesoría de inversión.

| Agente | Rol en la junta | Cuándo usarlo |
|---|---|---|
| `junta-presidente` | Presidente de la Junta | Conducir, consolidar votos, redactar el acta y los mandatos |
| `junta-consejero-lider-independiente` | Consejero Líder Independiente | Contrapeso, conflictos de interés, abogado del diablo, minoritarios |
| `junta-comite-auditoria` | Comité de Auditoría | Estados financieros, ingresos por comisiones, valoración, M&A, dividendos/recompras |
| `junta-comite-riesgos` | Comité de Riesgos | Apetito de riesgo, liquidez de fondos, operacional, ciber, stress tests |
| `junta-comite-compensacion` | Comité de Compensación y Talento | Pago ejecutivo, incentivos de gestores, retención, sucesión |
| `junta-comite-gobierno-sostenibilidad` | Comité de Nominaciones, Gobierno y Sostenibilidad | Stewardship y voto, ESG, reputación, composición de la junta |
| `junta-cio` | CIO global (invitado) | Tesis de inversión, desempeño, diseño de productos de inversión |
| `junta-estratega-macro` | Estratega Jefe Macro (invitado) | Escenarios macro, tasas, flujos, megatendencias |
| `junta-mercados-privados` | Director de Mercados Privados (invitado) | Infraestructura, crédito privado, PE, adquisiciones de gestoras |
| `junta-tecnologia-plataforma` | Director de Tecnología y Plataforma (invitado) | IA, datos, plataforma licenciada, tokenización, revisión del repo |

Todos responden en español con el mismo formato (lectura, **voto**, fundamento, riesgos,
condiciones, preguntas a la gerencia, métricas, confianza). El CIO y el Estratega Macro
tienen acceso de solo lectura al conector de Zacks cuando está disponible; ningún miembro
tiene acceso al bróker ni ejecuta acciones externas.

## Uso

**Consultar a un miembro:**

```
Pregúntale al junta-estratega-macro qué implica un recorte de tasas de 100 pb para los flujos a ETFs de renta fija
Que el junta-comite-riesgos haga un stress test de un fondo semilíquido de crédito privado
```

**Sesión de junta:**

```
/junta-directiva ¿Adquirimos una gestora de crédito privado de 80.000 M USD de AUM por 12.000 M USD?
/junta-directiva Lanzar un ETF de bitcoin para clientes patrimoniales en Europa
/junta-directiva La junta completa: plan de asignación de capital 2027 (dividendo vs. recompras vs. M&A)
```

El comando arma el quórum, consulta a los miembros en paralelo, permite una réplica
del Consejero Líder Independiente si hay disenso y el `junta-presidente` emite el acta
con resolución, votos, condiciones y mandatos.

## Relación con el staff ejecutivo

El staff ejecutivo de la fintech (`/comite-ejecutivo`, ver `docs/staff-ejecutivo.md`) opera
la compañía; la junta supervisa, aprueba y vota. Puedes encadenarlos: pide al comité
ejecutivo una propuesta y luego sométela a `/junta-directiva`.
