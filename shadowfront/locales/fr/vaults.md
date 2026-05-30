> **Traduction automatique (fr).** Source anglaise : [vaults.md](../../vaults.md).

# Coffres & gardiens

Comment fonctionne la carte ShadowFront — ce pour quoi nous combattons, et ce qui se passe après une capture.

Voir aussi : [Combattre dans le cercle](fight-on-the-point.md) · [Points bonus](bonus-points.md)

---

## Disposition de la carte

ShadowFront a **10 coffres** sur le champ de bataille :

| Type | Nombre | Placement |
|------|--------|-----------|
| **Petits coffres** | 8 | **2 par quadrant** — répartis sur les quatre quadrants de la carte |
| **Grands coffres** | 2 | Objectifs majeurs (valeur plus élevée — voir score ci-dessous) |

```
        [Q1: 2 small]     |     [Q2: 2 small]
    ──────────────────────┼──────────────────────
              [ LARGE ]   |   [ LARGE ]
    ──────────────────────┼──────────────────────
        [Q3: 2 small]     |     [Q4: 2 small]
```

**Conseil coordinateur :** Nommer les coffres par quadrant + taille en comms (ex. *"Stack Q1 small north"*, *"Rotate to large east"*) jusqu'à ce que la guilde fixe des callouts permanents.

---

## Cycle de capture

Chaque coffre suit la même boucle :

```
1. CONTESTED  →  fight in capture circle (most numbers wins)
        ↓
2. CAPTURED   →  one team completes the countdown
        ↓
3. GUARDED    →  a Vault Guardian spawns for the capturing team
        ↓
4. LOCKED     →  capture is DISABLED until the guardian is killed
        ↓
5. CONTESTED  →  guardian dead → circle opens again
```

### Gardien du coffre

Après une **capture réussie**, un **gardien du coffre** apparaît pour l'équipe qui a pris le coffre.

- Le gardien **appartient à l'équipe qui tient** — il défend leur capture
- **La capture ne peut pas reprendre** tant que le gardien n'est **pas tué**
- Pour flip un coffre, les ennemis doivent : **tuer le gardien → gagner le combat de nombres dans le cercle → compléter la nouvelle capture**

C'est pourquoi nous ne combattons pas que les joueurs — voir la priorité gardien / tour dans [Combattre dans le cercle](fight-on-the-point.md).

| Phase | Notre objectif si nous **tenons** | Notre objectif si nous **attaquons** |
|-------|-----------------------------------|--------------------------------------|
| Gardien up | Le protéger ; farmer les points de maintien | Tuer le gardien d'abord, puis contester le cercle |
| Gardien down | Recapturer avant qu'ils flip | Gagner les nombres dans le cercle, finir la capture |

**Call :** **"Guardian [vault]"** ou **"Tower [vault]"** — tuer ou défendre le gardien (même objectif).

---

## Points de maintien (score)

Les points s'accumulent pendant que votre guilde **tient** un coffre capturé (gardien vivant, votre équipe en contrôle). **Les grands coffres rapportent plus par temps de maintien que les petits** — les prioriser lors de la coordination des stacks et rotations.

> **Valeurs des points — vérifier en jeu.** Les taux exacts de maintien ne sont pas publiés dans les guides communautaires consultés. Remplir le tableau ci-dessous depuis l'**UI de l'événement** lors de votre prochain match (tap coffre → taux de maintien / points par intervalle).

| Type de coffre | Nombre | Points par maintien (TBD) | Notes |
|----------------|--------|---------------------------|-------|
| **Petit coffre** | 8 | _record from UI_ | 2 par quadrant ; bons pour les footholds et fenêtres bonus |
| **Grand coffre** | 2 | _record from UI_ | Paiement plus élevé — vaut généralement des stacks plus lourds |

### Comment enregistrer les valeurs (un match)

1. Ouvrir le score ShadowFront / détail coffre dans l'UI de l'événement
2. Noter **points par tick** (ou par minute) pour un coffre **petit** et un **grand**
3. Mettre à jour ce tableau — le coordinateur l'utilise pour les calls de priorité fin de partie

**Jusqu'à remplissage :** supposer **grand > petit** pour la priorité de rotation ; confirmer les chiffres après le premier match documenté.

---

## Implications stratégiques

### Petits coffres (8)
- Rapides à contester ; bons pour les **footholds précoces** et les fenêtres de **points bonus**
- Répartis sur les quadrants — ne pas essayer de tenir les 8 ; choisir base + cibles d'attaque
- Plus facile de rotate entre deux dans le même quadrant

### Grands coffres (2)
- **Valeur de maintien plus élevée** — souvent la condition de victoire en fin de partie
- Attendre des stacks ennemis plus lourds ; engager des nombres, pas des baleines solo
- Les kills de gardien ici ont un fort impact — flip ou deny peuvent basculer le classement

### Gardien + cercle ensemble
- **Impossible de capturer avec le gardien up** — le tuer est l'étape un pour tout flip
- Ne pas brûler le gardien **en infériorité numérique dans le cercle** — ils recaptureront quand il tombe ([Combattre dans le cercle](fight-on-the-point.md))
- **Exception :** grosse pression entrante sur le gardien → **"Guardian first"** / **"Tower first"**

---

## Priorité coordinateur (rapide)

```
Early   → 1 small vault foothold per squad (numbers in circle)
Mid     → Bonus windows on best-value vault we can win
Late    → Large vault hold OR deny enemy large + protect ours
Flip    → Kill guardian → win circle count → finish capture
Deny    → Break bonus when we can't win full flip ([Bonus Points](bonus-points.md))
```

---

## Callouts associés

| Call | Signification |
|------|-------------|
| **"Guardian [vault]"** | Focus le gardien du coffre |
| **"Guardian first [vault]"** | Tuer le gardien avant le combat de cercle |
| **"Guardian down [vault]"** | Capture ouverte — stack le cercle maintenant |
| **"Hold large"** | Priorité sur les points de maintien du grand coffre |

Liste complète : [Communication](communication.md)

---

*Dernière mise à jour : mai 2026 — tableau de score en attente de vérification en jeu.*
