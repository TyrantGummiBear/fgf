> **Machine translation (es).** English source: [rotations-and-stacking.md](../../rotations-and-stacking.md). Report fixes in guild chat or a GitHub issue.

# Rotaciones y apilamiento

El modo de control vive o muere dependiendo de **cuándo apilar** y **cuándo rotar**. ShadowFront es lo mismo, pero recuerda, los **números en el círculo** ganan capturas, no el poder bruto de la flota.

---

## Apilamiento (predeterminado)

**Acumular = enviar suficientes flotas a un círculo de captura para superar en número al enemigo.**

### Cuándo apilar
- El coordinador llama a un objetivo de salto.
- El enemigo tiene más números en el círculo.
- Estamos disputando una ventana de cuenta regresiva o de bonificación; consulte [Puntos de bonificación](bonus-points.md)
- La torre está caída (o a punto de caer) y necesitamos cuerpos en el círculo.

### Cómo apilar
1. Misma bóveda, mismo momento
2. Todas las flotas **dentro del círculo de captura** — ver [Lucha en el círculo](fight-on-the-point.md)
3. Elimina a los jugadores enemigos del círculo; No extiendas el daño fuera de la zona.

**Regla:** Cinco flotas promedio en el círculo vencen a una flota fuerte fuera de él.

---

## Rotaciones

**Rotar = abandonar tu bóveda actual y apilar un nuevo círculo de captura como grupo.**

Sólo rotar cuando el coordinador lo llame o la situación esté claramente perdida.

### Buenos desencadenantes de rotación
| Situación | Acción |
|-----------|----------------|
| Aquí no podemos ganar la pelea numérica | Girar hacia la bóveda que se puede ganar |
| El coordinador llama **"Rotar a [bóveda]"** | Mover inmediatamente |
| Enemigo sobrecargado en otros lugares | Girar si la bóveda actual se pierde porque |
| Al final del juego, el salto del líder importa más | Abandonar bóveda de bajo valor, acumular números en el objetivo |

### Desencadenantes de mala rotación
| Situación | Por qué está mal |
|-----------|----------------|
| Salir mientras todavía tengamos ventaja numérica | Paradas de captura |
| Persiguiendo un barco fuera del círculo | Llevan la cuenta |
| Rotación en solitario sin llamada | Dividir la pila |
| Una flota fuerte "se las arregla" sola | Los números vencen al poder |

---

## Decisión de dividir versus apilar```
Do we have more numbers in the circle right now?
├── YES → Stay. Remove stragglers. Finish capture.
└── NO  → Can we get 2+ more fleets in the circle soon?
          ├── YES → Call for stack
          └── NO  → Coordinator rotates or calls Deny
```---

## Bóveda local frente a bóveda ausente

- **Bóveda de inicio**: cuerpos mínimos **en el círculo** en todo momento
- **Bóveda de ataque** — pila completa, gana la cuenta
- **Bóveda disputada**: quien tenga más en el círculo captura

Nunca dejes el círculo de inicio vacío mientras el enemigo esté cerca.

---

## El modelo de 2 escuadrones (simple)

| Plantilla | Trabajo |
|-------|-----|
| **Alfa** | Pila principal: bóveda del coordinador, números ganadores |
| **Bravo** | Mantener en casa O reforzar Alpha de guardia |

Bravo no deambula. Mantienen un círculo o responden a **"Necesita pila en [bóveda]"**.

---

## Control paralelo de CoD

| Hábito de control | Hábito de ShadowFront |
|---------------|-------------------|
| "¡Se están llevando B!" | Apilar números en el círculo de B |
| "Deja de alimentar a B solo" | Una flota no puede ganar el conteo |
| "Comercio en la colina" | Muere en el círculo para que tu compañero mantenga la cuenta |
| "Juega el punto" | Juega la pelea de números, no las estadísticas de daño |

---

## Resumen

- **Predeterminado:** Apila un círculo, supera en número al enemigo dentro de él.
- **Rotar:** De guardia o cuando no se puede ganar el conteo
- **Nunca:** Difunde sin nadie en ningún círculo