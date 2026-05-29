> **Machine translation (es).** English source: [vaults.md](../../vaults.md). Report fixes in guild chat or a GitHub issue.

# Bóvedas y Guardianes

Cómo funciona el mapa de ShadowFront: por qué estamos peleando y qué sucede después de una captura.

Ver también: [Lucha en el círculo](fight-on-the-point.md) · [Puntos de bonificación](bonus-points.md)

---

## Diseño del mapa

ShadowFront tiene **10 bóvedas** en el campo de batalla:

| Tipo | Contar | Colocación |
|------|-------|-----------|
| **Bóvedas pequeñas** | 8 | **2 por cuadrante**: repartidos en los cuatro cuadrantes del mapa |
| **Grandes bóvedas** | 2 | Objetivos principales (valor más alto; consulte la puntuación a continuación) |```
        [Q1: 2 small]     |     [Q2: 2 small]
    ──────────────────────┼──────────────────────
              [ LARGE ]   |   [ LARGE ]
    ──────────────────────┼──────────────────────
        [Q3: 2 small]     |     [Q4: 2 small]
```**Consejo para el coordinador:** Nombre las bóvedas por cuadrante + tamaño en las comunicaciones (por ejemplo, *"Apilar Q1 norte pequeño"*, *"Girar al este grande"*) hasta que el gremio se decida por llamadas fijas.

---

## Ciclo de captura

Cada bóveda sigue el mismo bucle:```
1. CONTESTED  →  fight in capture circle (most numbers wins)
        ↓
2. CAPTURED   →  one team completes the countdown
        ↓
3. GUARDED    →  a Vault Guardian spawns for the capturing team
        ↓
4. LOCKED     →  capture is DISABLED until the guardian is killed
        ↓
5. CONTESTED  →  guardian dead → circle opens again
```### Guardián de la bóveda

Después de una **captura exitosa**, aparece un **Guardián de la bóveda** para el equipo que tomó la bóveda.

- El guardián **pertenece al equipo de retención** — defiende su captura
- **La captura no se puede reanudar** hasta que el guardián sea **matado**
- Para voltear una bóveda, los enemigos deben: **matar al guardián → ganar la pelea numérica en círculo → completar una nueva captura**

Es por eso que no solo luchamos contra jugadores; consulta la prioridad de guardián/torre en [Fight in the Circle](fight-on-the-point.md).

| Fase | Nuestro objetivo si **mantenemos** | Nuestro objetivo si **atacamos** |
|-------|-------------------------|---------------------|
| Guardián arriba | Protégelo; puntos de espera en granjas | Primero mata al guardián y luego al círculo de competencia |
| Guardián caído | Vuelva a capturar antes de que se volteen | Gana números en círculo, termina la captura |

**Llamar:** **"Guardian [bóveda]"** o **"Torre [bóveda]"**: mata o defiende al guardián (mismo objetivo).

---

## Mantener puntos (puntuación)

Los puntos aumentan mientras tu gremio **tiene** una bóveda capturada (guardián vivo, tu equipo tiene el control). **Las bóvedas grandes pagan más por tiempo de espera que las bóvedas pequeñas**: priorícelas al coordinar pilas y rotaciones.

> **Valores de puntos: verifíquelos en el juego.** Las tasas exactas de tiempo de espera no se publican en las guías comunitarias que verificamos. Complete la siguiente tabla desde la **IU del evento** durante su próxima partida (toque la bóveda → mantenga la tasa/puntos por intervalo).

| Tipo de bóveda | Contar | Puntos por retención (TBD) | Notas |
|------------|-------|------------------------|-------|
| **Bóveda pequeña** | 8 | _registro desde UI_ | 2 por cuadrante; bueno para puntos de apoyo y ventanas extra |
| **Bóveda grande** | 2 | _registro desde UI_ | Mayor pago: generalmente vale la pena acumular más pilas |

### Cómo registrar valores (una coincidencia)

1. Abra los detalles de puntuación/bóveda de ShadowFront en la interfaz de usuario del evento.
2. Anote **puntos por tick** (o por minuto) para una bóveda **pequeña** y otra **grande**
3. Actualice esta tabla: el coordinador la usa para llamadas de prioridad al final del juego.

**Hasta que se complete:** asuma **grande > pequeño** para la prioridad de rotación; Confirme los números después de la primera coincidencia documentada.

---

## Implicaciones estratégicas

### Bóvedas pequeñas (8)
- Rápido para competir; bueno para **primeros puntos de apoyo** y ventanas de **puntos de bonificación**
- Distribuidos en cuadrantes: no intentes mantener los 8; elegir casa + objetivos de ataque
- Más fácil de rotar entre dos en el mismo cuadrante

### Bóvedas grandes (2)
- **Valor de retención más alto**: a menudo, la condición para ganar al final del juego
- Espere acumulaciones de enemigos más pesadas; comprometer números, no ballenas solitarias
- Las muertes de guardianes aquí son de alto impacto: voltear o negar puede cambiar la clasificación

### Guardián + círculo juntos
- **No se puede capturar con el guardián arriba**: matarlo es el primer paso para cualquier lanzamiento.
- No quemes al guardián mientras estés **superado en número en el círculo**: lo recuperarán cuando caiga ([Fight in the Circle](fight-on-the-point.md))
- **Excepción:** entrada grande en guardián → **"Guardián primero"** / **"Torre primero"**

---

## Prioridad del coordinador (rápido)```
Early   → 1 small vault foothold per squad (numbers in circle)
Mid     → Bonus windows on best-value vault we can win
Late    → Large vault hold OR deny enemy large + protect ours
Flip    → Kill guardian → win circle count → finish capture
Deny    → Break bonus when we can't win full flip ([Bonus Points](bonus-points.md))
```---

## Llamadas relacionadas

| Llamar | Significado |
|------|---------|
| **"Guardián [bóveda]"** | Enfoca al guardián de la bóveda |
| **"Guardián primero [bóveda]"** | Mata al guardián antes de la pelea circular |
| **"Guardián caído [bóveda]"** | Captura abierta: círculo de pila ahora |
| **"Mantener grande"** | Prioridad en puntos de retención de grandes saltos |

Lista completa: [Comunicación](communication.md)

---

*Última actualización: mayo de 2026: tabla de puntuación pendiente de verificación en el juego.*