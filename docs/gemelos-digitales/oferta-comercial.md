# Gemelos digitales operativos: oferta comercial y data request

*Material de primeras reuniones (Colombia). Elaborado por el CPO (simulado) a partir de las decisiones del comité ejecutivo.*

- Marca neutra: **[NOMBRE COMERCIAL]**. No se menciona el Grupo financiero.
- Las cifras de ahorro son rangos típicos a validar en el piloto. Ninguna es una garantía.
- Lo marcado *[supuesto]* debe validarlo el CFO o el área responsable antes de usarse con clientes.
- Antes del primer envío, Legal y el CCO revisan la nota de tratamiento de datos y el NDA.

**Sectores, en orden de prioridad:**
1. Edificios corporativos y centros comerciales.
2. Cadena de frío.
3. Solar distribuida (solo software, con decisión de seguir o cerrar al día 60).

---

## A. Propuesta de valor por sector

### 1. Edificios corporativos y centros comerciales

**Titular:** "Su edificio ya tiene los datos para gastar menos energía. Nosotros le decimos dónde, cuánto y qué hacer primero."

| Elemento | Contenido |
|---|---|
| Problema (en palabras del cliente) | "La factura sube y no sé por qué." "El chiller falla en la peor semana." "El BMS genera cientos de alarmas que nadie mira." "El contratista de mantenimiento cobra por visitas, no por resultados." |
| Qué entregamos | Leemos el sistema de gestión del edificio (BMS, por BACnet o Modbus) y los medidores, **sin escribir nunca en ellos**. Entregamos: <br>• consumo de referencia en kWh/m²; <br>• detección de consumo anómalo (horarios, temperaturas de consigna, equipos encendidos sin ocupación); <br>• diagnóstico de fallas en aire acondicionado y chillers; <br>• lista de acciones priorizada por su valor en COP al mes. |
| Beneficios cuantificables | **Energía: ahorro típico de 4% a 9%.** <br>• Fuente: LBNL, *Smart Energy Analytics Campaign*, informe del año 3 (nov-2019), en sitios de EE.UU. con 2 años de uso. <br>• Mediana de 4% con sistemas de información energética y de 9% con software de detección y diagnóstico de fallas. <br>• *[supuesto: hay que validar en el piloto que se cumple en Colombia]*. <br>**Correctivos de chillers:** reducción *[supuesto, sin fuente; se mide en el piloto]*. |
| Beneficios cualitativos | Evidencia de kWh y emisiones para informes de sostenibilidad (ESG). Trazabilidad de qué se corrigió y cuándo. Soporte objetivo para auditar al contratista de mantenimiento. |
| Por qué nosotros | **Frente al BMS tradicional:** el BMS controla y alarma, pero no dice cuánto cuesta cada falla ni cuál atender primero. <br>**Frente al integrador:** no vendemos hardware ni horas; cobramos por resultado verificado. <br>**Sin obras:** funciona con lo que ya tiene y arranca en semanas, no en meses. |

**Objeciones típicas**

| Objeción | Respuesta |
|---|---|
| "Ya tengo BMS." | Lo usamos como fuente. El BMS le dice qué pasa; nosotros, cuánto le cuesta y qué arreglar primero. |
| "Riesgo de ciberseguridad." | Solo lectura, con una conexión aislada de su red corporativa. Nunca escribimos al BMS, y su equipo de TI valida la arquitectura antes de conectar. |
| "¿Por qué pagar desde el día 1 si no sé si voy a ahorrar?" | El piloto dura 12 semanas y los criterios de éxito se firman al inicio. El bono sobre el ahorro solo empieza cuando el ahorro está verificado, a partir del mes 7. |
| "Mi contratista de mantenimiento ya hace esto." | Lo hacemos más efectivo: recibe las fallas priorizadas y con evidencia. Lo invitamos al piloto. |

### 2. Cadena de frío (exportadores de flores y alimentos, operadores logísticos)

**Titular:** "Sepa en menos de 15 minutos cuándo su carga está en riesgo, y demuéstrele a su cliente y a su aseguradora que la cuidó."

| Elemento | Contenido |
|---|---|
| Problema | "Me entero de que la temperatura se salió de rango cuando el cliente rechaza el despacho." "Las mermas se discuten sin datos." "Los compresores consumen cada vez más y no sé si es una falla." |
| Qué entregamos | • Monitoreo 24x7 de temperatura y consumo de los cuartos fríos. <br>• Alertas en menos de 15 minutos cuando la temperatura se sale de rango, por WhatsApp, SMS o correo, con escalamiento. <br>• Detección del desgaste de los equipos a partir de ciclos, aperturas de puertas y deshielos. <br>• Informe de trazabilidad por lote o por cuarto. |
| Beneficios cuantificables | **Contexto:** la falta de refrigeración efectiva causó la pérdida de cerca del 12% de la producción mundial de alimentos (UNEP/FAO, *Sustainable Food Cold Chains*, 2022, con datos de 2017). <br>**Reducción de mermas del cliente:** *[supuesto: el rango se define en la semana 2 con su historial de mermas]*. <br>**Ahorro de energía en frío:** *[supuesto, a validar]*. |
| Beneficios cualitativos | Registro auditable para clientes importadores, certificaciones y reclamos a aseguradoras. Defensa en disputas por la calidad de la carga. |
| Por qué nosotros | **Frente a registradores de temperatura y rastreo de camiones:** esas herramientas cubren el camión o el lote. Nosotros cubrimos la bodega completa y cruzamos temperatura con energía y estado del equipo, así que la alerta llega antes de que la temperatura salga de rango. <br>**Frente al fabricante del equipo de refrigeración:** somos independientes de la marca. |

**Objeciones típicas**

| Objeción | Respuesta |
|---|---|
| "Ya tengo registradores de temperatura (dataloggers)." | Muy bien, los integramos. El registrador anota lo que ya pasó; nosotros alertamos en tiempo real y anticipamos la falla. |
| "Mis cuartos no tienen sensores conectados." | Si falta menos del 30% de la medición, instalamos sensores que no intervienen sus equipos, en alquiler y cobrados aparte. Si falta más, se lo decimos con franqueza y no avanzamos. |
| "¿Quién atiende las alertas a las 3 a.m.?" | Usted define a quién se escala. Nosotros garantizamos que la alerta llegue en menos de 15 minutos y medimos el tiempo de respuesta. |
| "Mi merma es baja." | Medimos su línea base en la semana 2. Si el problema no existe, se lo diremos. |

### 3. Solar distribuida (solo software; se decide al día 60 si sigue)

**Titular:** "Cada kWh que su planta no genera es dinero perdido. Le mostramos cuánto, en qué planta y qué visita de mantenimiento hacer primero."

| Elemento | Contenido |
|---|---|
| Problema | "Tengo 15 plantas y 3 portales distintos de inversores." "Me entero de la falla cuando el cliente reclama." "No sé qué planta visitar primero." |
| Qué entregamos | • Un tablero único para varias marcas de inversores, conectado por API. <br>• Rendimiento de cada planta frente a lo esperado (performance ratio, PR). <br>• Generación perdida en kWh y en COP, con su causa probable: disponibilidad, suciedad, falla de un string o recorte del inversor. <br>• Lista de visitas de operación y mantenimiento ordenada por valor. |
| Beneficios cuantificables | **Generación recuperada:** *[supuesto, sin fuente verificada; se cuantifica en la línea base del piloto]*. <br>**Visitas de mantenimiento improductivas evitadas:** *[supuesto]*. |
| Beneficios cualitativos | Reporte uniforme a los clientes con contrato de compra de energía o de autoconsumo. Evidencia para reclamar garantías a fabricantes y aseguradoras. |
| Por qué nosotros | **Frente al portal del fabricante:** cada portal ve solo su marca y no traduce las pérdidas a dinero ni prioriza visitas. Nosotros consolidamos plantas de varias marcas y ordenamos el mantenimiento por impacto. |

**Objeciones típicas**

| Objeción | Respuesta |
|---|---|
| "El portal del inversor es gratis." | Sí, para ver una sola marca. El valor está en ver toda la cartera junta y priorizar por dinero. |
| "Mis plantas son pequeñas." | Por eso calificamos por cartera (varias plantas), no por planta. |
| "No tengo medición de radiación solar." | Usamos datos satelitales como alternativa. La precisión es menor y se lo decimos de entrada. |

---

## B. Oferta de piloto (12 semanas, común a los tres sectores)

**Alcance:**
- **Edificios:** 1 edificio.
- **Frío:** 1 bodega, o de 4 a 6 cuartos *[supuesto]*.
- **Solar:** cartera de 5 a 20 plantas *[supuesto]*, con decisión de seguir o cerrar al día 60.

| Semana | Entregable |
|---|---|
| 0 (firma) | Reunión de arranque, NDA firmado, revisión de la arquitectura de conexión con TI y data request firmado. |
| 1–2 | Conexión de solo lectura validada e inventario de los datos disponibles. **Informe de calidad de datos:** si falta más del 30% de la medición, el piloto no sigue. |
| 3–4 | **Diagnóstico de línea base** (kWh/m², mermas o rendimiento de las plantas) con la metodología acordada. |
| 5 | **Tablero en vivo** y alertas activas. En frío, monitoreo 24x7 con alertas en menos de 15 minutos. |
| 6–7 | **Primer informe de hallazgos:** las 10 acciones principales, cada una con valor estimado y responsable. |
| 8–11 | Acompañamiento mientras el cliente o su contratista ejecutan las acciones, y medición de resultados. |
| 12 | **Informe de ahorro o impacto** frente a la línea base, con recomendación y propuesta de contrato anual. |

| El cliente pone | Nosotros ponemos |
|---|---|
| Sponsor con presupuesto, contacto técnico y contacto financiero | Software, analítica, ingeniero asignado y soporte |
| Acceso de solo lectura (BMS, medidores o API) y 12 meses de historia | Conexión aislada de su red y sensores para cubrir huecos (cobrados aparte) |
| Ejecución de las acciones correctivas | Metodología para medir y verificar el ahorro |

**Precio y condiciones** *[supuesto: lo valida el CFO]*:
- Implementación de unos USD 5.000, pagada a la firma.
- Suscripción del piloto de unos USD 1.000 al mes por edificio o sitio, desde el día 1. Falta definir la unidad de cobro para frío y para solar.
- Sensores en alquiler, cotizados aparte.
- No hay ahorro garantizado ni esquemas en los que se cobre solo un porcentaje del ahorro.

**Criterios de éxito.** Se eligen 3 y se firman en la semana 0:
1. Conexión y datos completos en menos de 4 semanas.
2. Al menos X hallazgos accionables, con un valor anual estimado de al menos Y.
3. Según el sector:
   - Edificios: reducción medida de kWh/m² frente a la línea base, ajustada por clima y ocupación.
   - Frío: el 100% de las salidas de rango alertadas en menos de 15 minutos.
   - Solar: generación perdida identificada y recuperada.
4. Satisfacción del sponsor de al menos 8 sobre 10.

**Paso a contrato anual.** En la semana 10 se presenta la propuesta. Si se cumplen los criterios, se firma una carta de intención hacia un contrato anual con:
- suscripción con un mínimo fijo;
- un bono del 20% al 35% del ahorro verificado a partir del mes 7;
- ampliación a más sitios.

El pago de implementación del piloto se descuenta del primer año *[supuesto]*.

La carta de intención solo cuenta para las metas del programa si tiene cinco elementos: sponsor con presupuesto, problema cuantificado, alcance, acceso a datos y disposición a pagar.

---

## C. Presentación de 60 segundos y preguntas de descubrimiento

**Edificios.** "Los edificios con BMS suelen tener fallas silenciosas: chillers trabajando de más, horarios mal programados, equipos encendidos sin ocupación. El BMS las registra, pero nadie las convierte en pesos. Nosotros nos conectamos en modo de solo lectura a lo que usted ya tiene, sin tocar su control. En 6 semanas le entregamos su consumo por metro cuadrado y las acciones priorizadas por valor. Estudios en EE.UU. reportan ahorros medianos de 4% a 9% con este tipo de analítica, y en su edificio lo comprobamos con un piloto de 12 semanas y criterios de éxito firmados. Si el ahorro se confirma, compartimos una parte de él. Si no, usted se queda con un diagnóstico serio de su edificio."

**Frío.** "Una temperatura fuera de rango que se detecta tarde le cuesta un despacho, un cliente y a veces un reclamo. Nosotros vigilamos sus cuartos fríos 24x7 y le avisamos en menos de 15 minutos. Además cruzamos la temperatura con el comportamiento del compresor para anticipar la falla, y le dejamos un registro auditable para su cliente y su aseguradora. Usamos los sensores que ya tiene y solo completamos los huecos. En 12 semanas medimos sus mermas frente al historial."

**Solar.** "Si opera varias plantas con distintas marcas de inversores, hoy revisa varios portales y se entera tarde de las fallas. Nosotros juntamos toda su cartera y le mostramos cuántos kWh y cuántos pesos pierde cada planta, por qué, y qué visita de mantenimiento hacer primero. No instalamos nada. A los 60 días sabrá cuánta generación estaba perdiendo."

**Cinco preguntas para la primera reunión** (ajustar el vocabulario a cada sector):
1. ¿Cuánto paga al año en energía (o cuánto pierde en mermas o en generación), y quién responde por esa cifra?
2. ¿Cuál fue el último incidente costoso (falla de chiller, temperatura fuera de rango, planta caída)? ¿Cuánto costó y cómo se enteró?
3. ¿Qué sistemas de medición tiene hoy (BMS, medidores, registradores de temperatura, inversores)? ¿Cuánta historia guardan y quién tiene el acceso?
4. Si el piloto demuestra ahorro, ¿quién se queda con ese ahorro y quién firma el presupuesto? Esto confirma si la persona es propietaria, operadora o arrendataria.
5. ¿Qué tendríamos que mostrarle en 12 semanas para que esto pase a contrato anual?

---

## D. Primer data request (lista de información)

Prioridad: **I** = imprescindible, **D** = deseable. Si un formato no está disponible, sirve el alternativo: preferimos datos imperfectos pronto que datos perfectos tarde.

### Edificios

| # | Qué | Periodo / frecuencia | Formato (preferido / alternativo) | Prioridad | Para qué lo usamos |
|---|---|---|---|---|---|
| 1 | Consumo eléctrico del medidor principal | 12–24 meses, cada 15 min | CSV del operador de red o de los submedidores / facturas en PDF | I | Calcular el consumo de referencia por m² y detectar anomalías |
| 2 | Facturas de energía | 12 meses | PDF | I | Pasar kWh a COP y verificar el ahorro |
| 3 | Historial del BMS: chillers, unidades de aire, temperaturas, valores de consigna y estados | 12 meses, cada 5–15 min | Exportación CSV / acceso de solo lectura por BACnet o Modbus | I | Diagnosticar fallas de aire acondicionado y chillers |
| 4 | Lista de puntos de medición del BMS y su arquitectura | Actual | Excel / capturas de pantalla | I | Ver qué existe y si falta menos del 30% |
| 5 | Área en m² por zona, horarios y ocupación | Actual | Excel | I | Normalizar el consumo |
| 6 | Fichas técnicas de chillers y equipos principales | Actual | PDF | D | Comparar el desempeño real con el de diseño |
| 7 | Contrato de mantenimiento y registro de órdenes de trabajo | 12 meses | PDF / Excel | D | Relacionar fallas con intervenciones y validar el mantenimiento predictivo |
| 8 | Submedidores por tablero o zona | 12 meses, cada 15 min | CSV | D | Ubicar el desperdicio con más precisión |

### Cadena de frío

| # | Qué | Periodo / frecuencia | Formato | Prioridad | Para qué lo usamos |
|---|---|---|---|---|---|
| 1 | Temperatura por cuarto o cámara | 12 meses, cada 1–5 min | CSV del registrador / exportación del portal | I | Medir cuántas veces se sale de rango hoy |
| 2 | Registro de mermas o rechazos: fecha, lote, causa y valor | 12–24 meses | Excel | I | Cuantificar el problema y medir el impacto |
| 3 | Consumo eléctrico de la planta de frío | 12 meses, cada 15 min | CSV / facturas | I | Relacionar consumo con el estado de los equipos |
| 4 | Inventario de cuartos, equipos y sensores existentes | Actual | Excel / plano | I | Ver qué está cubierto y qué sensores faltan |
| 5 | Rangos de temperatura por producto y protocolo de respuesta actual | Actual | PDF | I | Configurar las alertas (menos de 15 min) y el escalamiento |
| 6 | Registro de mantenimiento de refrigeración | 12 meses | Excel / PDF | D | Anticipar fallas |
| 7 | Requisitos de trazabilidad de clientes, certificaciones o aseguradora | Actual | PDF | D | Diseñar el informe auditable |

### Solar

| # | Qué | Periodo / frecuencia | Formato | Prioridad | Para qué lo usamos |
|---|---|---|---|---|---|
| 1 | Acceso de solo lectura a la API de los inversores, por marca | — | API / exportación CSV del portal | I | Juntar la generación de todas las plantas |
| 2 | Lista de plantas: potencia (kWp), ubicación, marca y modelo de inversor y módulo, fecha de entrada en operación | Actual | Excel | I | Calcular el rendimiento esperado |
| 3 | Generación histórica | 12 meses, cada 15 min a 1 h | CSV / API | I | Calcular la línea base de rendimiento y pérdidas |
| 4 | Radiación solar, si hay estación meteorológica | 12 meses | CSV / API | D (si no hay, usamos datos satelitales) | Medir el rendimiento con precisión |
| 5 | Órdenes de mantenimiento, limpiezas y fallas | 12 meses | Excel | D | Identificar causas y priorizar visitas |
| 6 | Tarifa o contrato de venta de energía por planta | Actual | Excel | D | Pasar los kWh perdidos a COP |

**Contactos que necesitamos:**

| Contacto | Prioridad |
|---|---|
| Técnico (responsable del BMS, de la bodega o del mantenimiento) | I |
| TI o ciberseguridad | I (en solar, D) |
| Financiero (dueño de la factura o del estado de resultados) | I |
| Sponsor ejecutivo | I |

**Nota de tratamiento de datos (va en el envío):**

> Accedemos en modo **solo lectura**: no escribimos ni modificamos sus sistemas de control. La conexión está aislada de su red corporativa y su área de TI la valida antes de activarla. Toda la información se trata como **confidencial** bajo el **NDA** firmado antes del intercambio y se usa solo para el piloto. **No pedimos datos personales**, salvo los nombres y contactos de los responsables designados. Si algún archivo los contiene (por ejemplo, registros de acceso u ocupación por persona), le pedimos anonimizarlo antes de enviarlo. Los datos personales que tratemos se manejarán conforme al régimen colombiano de protección de datos (Ley 1581 de 2012 y sus normas reglamentarias) y a nuestra política de tratamiento. Al terminar el piloto, devolvemos o eliminamos los datos, según usted decida.

---

## E. Plantilla de correo

**Asunto:** [Empresa] – primer paso del piloto: información para la línea base

Hola, [Nombre]:

Gracias por la reunión del [fecha]. Como acordamos, para arrancar el piloto en [edificio, bodega o cartera de plantas] le adjunto la lista de información inicial.

- **Lo imprescindible** está marcado con "I". Con eso basta para empezar, y en 2 semanas le entregamos el informe de calidad de datos.
- Cada punto explica **para qué lo usamos**. Si algún formato no está disponible, el alternativo nos sirve.
- Nuestro acceso es **de solo lectura**, aislado de su red y cubierto por el NDA adjunto. No necesitamos datos personales.

¿Podemos agendar 30 minutos esta semana con [contacto técnico] y [TI] para revisar los accesos? Propongo [fecha 1] o [fecha 2].

Nuestra meta común es tener el piloto activo antes del [fecha = firma + 8 semanas].

Saludos,
[Nombre] · [Cargo] · [NOMBRE COMERCIAL]

---

## Pendientes antes de salir a clientes

| Pendiente | Responsable |
|---|---|
| Arquitectura de referencia de la conexión de solo lectura, documentada para mostrar a TI | CTO / CISO |
| Metodología para medir y verificar el ahorro (por ejemplo, un protocolo reconocido como IPMVP, a confirmar) | CTO |
| Validar precios: USD 1.000 al mes, USD 5.000 de implementación y unidad de cobro para frío y solar | CFO |
| NDA, política de tratamiento de datos y revisión de la nota de datos | CCO / Legal |
| Costo de las guardias 24x7 para cumplir las alertas de frío en menos de 15 minutos | COO / CTO |
| Lista de 15 a 20 prospectos (10 de edificios, 5 de frío, 3 a 5 de solar) y primeras 8 reuniones | CPO / CMO |

## Fuentes (consultadas el 2-nov-2026)

- [LBNL – Smart Energy Analytics Campaign, informe del año 3 (nov-2019)](https://buildings.lbl.gov/sites/default/files/Smart%20Energy%20Analytics%20Campaign%20Year%203%20Report_LBNL_11.1.19.pdf)
- [DOE – resumen de la campaña](https://www.energy.gov/cmei/buildings/articles/smart-energy-analytics-campaign-reveals-continued-energy-and-cost-savings)
- [UNEP/FAO – Sustainable Food Cold Chains (resumen)](https://www.downtoearth.org.in/food/sustainable-cold-chains-can-address-climate-food-crises-unep-fao-report-85966); IIR (2020) da una cifra cercana, 13%, con otro método: [IIR](https://iifiir.org/en/fridoc/the-role-of-refrigeration-in-worldwide-nutrition-2020-142029)
