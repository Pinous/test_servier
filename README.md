## Installation

```conda create -n servier python=3.10```

```conda activate servier```

```pip install -r requirements/requirements.txt```

**Pour lancer des tests**

```pip install -r requirements/requirements-test.txt```

```git clone https://github.com/Pinous/test_servier.git```

```cd test_servier```

```pytest .```

## 6. Pour aller plus loin

Quels sont les éléments à considérer pour faire évoluer votre code afin qu’il puisse gérer de grosses volumétries de données (fichiers de plusieurs To ou millions de fichiers par exemple) ?
Pourriez-vous décrire les modifications qu’il faudrait apporter, s’il y en a, pour prendre en considération de telles volumétries ?

1) Comprendre mieux la donnée business
   - Structurer la source de données pour avoir un format unique et sans erreur. Le code n'est pas gérable avoir des modèles de données flexibles.
   - Importer les colonnes nécessaires et formatter la donnée sur le type qui lui convient le mieux (int64 -> int8)
   - Cela permettra également de rendre le code générique (la partie ingestion doit etre supprimée par une classe générique)
2) Réadapter l'existant
   - Notamment regarder les opérations Pandas qui prennent du temps. Si possible passer par Numpy
   - Faire des requêtes sql pour la plupart des opérations directement
   - Clean architecture
3) Ajout des éléments pour être plus carré
   - Logging/Monitoring
   - Gestion des exceptions
   - CI /CD
   - tests e2e
   - change log
   - etc
4) Passer à un système distribué avec une base optimisée
   - Notamment Spark avec une gestion des fichiers en Parquet avec Delta
   - On pourrait fragmenter les fichiers par date
   - ajouter un système de queue pour manager la volumétrie
5) Aller voir gentiment son manager pour lui annoncer que la facture cloud va augmenter

## SQL

### Première partie du test

```
SELECT date, SUM(prod_price * prod_qty) as ventes
FROM TRANSACTION
WHERE date >= '2019-01-01' AND date <= '2019-12-31'
GROUP BY date
```

### Seconde partie du test

```
SELECT  transaction.client_id,
        SUM(
            CASE WHEN product_nomenclature.product_type = 'MEUBLE' THEN transaction.prod_price * transaction.prod_qty ELSE 0 END
        ) AS ventes_meuble,
        SUM(
            CASE WHEN product_nomenclature.product_type = 'DECO' THEN transaction.prod_price * transaction.prod_qty ELSE 0 END
        ) AS ventes_deco
FROM transaction
JOIN product_nomenclature ON (transaction.prop_id = product_nomenclature.product_id)
WHERE date >= '2019-01-01' AND date <= '2019-12-31'
GROUP BY transaction.client_id
```
