> **Machine translation (fr).** English source: [rotations-and-stacking.md](../../rotations-and-stacking.md). Report fixes in guild chat or a GitHub issue.

# Rotations et empilage

Le mode de contrôle vit ou meurt selon **quand empiler** et **quand faire pivoter**. ShadowFront est le même – mais rappelez-vous que les **chiffres dans le cercle** gagnent les captures, pas la puissance brute de la flotte.

---

## Empilement (par défaut)

**Stack = envoyez suffisamment de flottes dans un cercle de capture pour surpasser l'ennemi en nombre.**

### Quand empiler
- Le coordinateur appelle une cible de coffre-fort
- L'ennemi a plus de chiffres dans le cercle
- Nous contestons un compte à rebours ou une fenêtre de bonus — voir [Points bonus](bonus-points.md)
- La tour est en panne (ou sur le point de tomber) et nous avons besoin de corps dans le cercle

### Comment empiler
1. Même coffre-fort, même timing
2. Toutes les flottes **à l'intérieur du cercle de capture** — voir [Combattre dans le cercle] (fight-on-the-point.md)
3. Retirez les joueurs ennemis du cercle ; ne propagez pas les dégâts en dehors de la zone

**Règle :** Cinq flottes moyennes dans le cercle ont battu une flotte forte à l'extérieur.

---

## Rotations

**Rotation = quittez votre coffre-fort actuel et empilez un nouveau cercle de capture en groupe.**

Ne faites une rotation que lorsque le coordinateur l'appelle ou que la situation est clairement perdue.

### Bons déclencheurs de rotation
| Situation | Actions |
|-----------|--------|
| Nous ne pouvons pas gagner la bataille des chiffres ici | Passer au coffre-fort gagnable |
| Le coordinateur appelle **"Tourner vers [vault]"** | Déménagez immédiatement |
| Ennemi surempilé ailleurs | Faire pivoter si le coffre-fort actuel est perdu |
| En fin de partie, le saut de leader compte davantage | Abandonnez le coffre-fort de faible valeur, empilez les numéros sur la cible |

### Déclencheurs de mauvaise rotation
| Situation | Pourquoi c'est faux |
|---------------|----------------|
| Partir alors que nous avons encore l'avantage numérique | Arrêts de capture |
| Poursuivre un navire en dehors du cercle | Ils tiennent le compte |
| Rotation solo sans appel | Diviser la pile |
| Une flotte puissante « s'en occupe » seule | Les chiffres battent le pouvoir |

---

## Décision fractionnée ou pile```
Do we have more numbers in the circle right now?
├── YES → Stay. Remove stragglers. Finish capture.
└── NO  → Can we get 2+ more fleets in the circle soon?
          ├── YES → Call for stack
          └── NO  → Coordinator rotates or calls Deny
```---

## Coffre-fort à domicile contre Coffre-fort à l'extérieur

- **Coffre-fort** — nombre minimum de corps **dans le cercle** à tout moment
- **Attaquer le coffre-fort** — pile complète, gagnez le décompte
- **Coffre-fort contesté** — celui qui en a le plus dans le cercle capture

Ne laissez jamais le cercle de départ vide lorsque l'ennemi est à proximité.

---

## Le modèle à 2 équipes (simple)

| Escouade | Emploi |
|-------|-----|
| **Alpha** | Pile principale — coffre-fort du coordinateur, numéros gagnants |
| **Bravo** | Maintien à domicile OU renforcement Alpha sur appel |

Bravo ne se déplace pas. Ils tiennent un cercle ou répondent à **"Besoin d'une pile sur [vault]"**.

---

## Contrôle CoD parallèle

| Habitude de contrôle | Habitude ShadowFront |
|---------------|---------|
| "Ils prennent B !" | Empiler les nombres dans le cercle de B |
| "Arrêtez de nourrir B seul" | Une flotte ne peut pas remporter le décompte |
| "Commerce sur la colline" | Mourez dans le cercle pour que votre coéquipier compte |
| "Jouer le point" | Jouez au combat numérique, pas aux statistiques de dégâts |

---

## Résumé

- **Par défaut :** Empilez un cercle, dépassez en nombre l'ennemi à l'intérieur
- **Rotation :** Sur appel ou lorsque le décompte est impossible à gagner
- **Jamais :** Éparpillez-vous sans personne dans aucun cercle