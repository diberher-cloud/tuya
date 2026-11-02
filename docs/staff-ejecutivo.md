# Staff ejecutivo de agentes

Equipo de subagentes de Claude Code que actúan como el C-suite de la fintech.
Viven en `.claude/agents/` y se cargan automáticamente al abrir Claude Code en este repositorio.

| Agente | Rol | Cuándo usarlo |
|---|---|---|
| `ceo` | CEO / Chief of Staff | Estrategia, prioridades, arbitrar entre áreas, consolidar decisiones |
| `cfo` | CFO | Unit economics, pricing, presupuesto, runway, fundraising, fondeo |
| `cto` | CTO | Arquitectura, ledger, integraciones, build vs. buy, revisión del repo |
| `cro` | Chief Risk Officer | Riesgo de crédito, fraude, provisiones, apetito de riesgo |
| `cco` | Chief Compliance Officer | Licencias, AML/KYC, consumidor financiero, datos personales |
| `general-counsel` | Director jurídico | Contratos, societario, T&C, PI, litigios |
| `ciso` | CISO | Ciberseguridad, PCI DSS, incidentes, revisión de seguridad del repo |
| `coo` | COO | Operaciones, soporte, conciliación, cobranza, ejecución |
| `cmo` | CMO / Growth | Adquisición, marca, GTM, retención, competencia |
| `cpo` | CPO | Roadmap, discovery, diseño de productos financieros |

Todos responden en español con el mismo formato (lectura, recomendación, fundamento,
riesgos y dependencias, KPIs, próximos pasos 30/60/90, nivel de confianza), lo que
permite que el CEO consolide. Ninguno ejecuta acciones externas: recomiendan.

## Uso

**Consultar a un ejecutivo:**

```
Pídele al cfo que calcule el payback de una tarjeta de crédito con CAC de 40 USD...
Que el ciso revise la seguridad de tvconnect/client.py
```

**Convocar al comité completo:**

```
/comite-ejecutivo ¿Lanzamos un producto de BNPL en Colombia en Q1?
```

El comando elige el quórum relevante, consulta a los ejecutivos en paralelo, y el
`ceo` consolida en una decisión con plan de acción.

## Personalizar

Para que las respuestas sean mucho mejores, agrega contexto real de la compañía a cada
agente (o a un `CLAUDE.md` en la raíz): países y licencias, productos, etapa, métricas
actuales, apetito de riesgo, stack tecnológico y aliados.
