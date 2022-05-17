# docs
<p align="center">
    <img src="src/assets/logo.png" alt="Bug's Bunny logo" width="220">
</p>

[![Build Latex documents](https://github.com/Bug-s-Bunny-Team/docs/actions/workflows/build.yml/badge.svg?branch=master)](https://github.com/Bug-s-Bunny-Team/docs/actions/workflows/build.yml)

## Introduzione
Questo repository mantiene gli strumenti e i sorgenti *Latex* per compilare la documentazione. 
I documenti compilati in formato *PDF*, e in versione stabile, si trovano nella [cartella condivisa](https://drive.google.com/drive/folders/10DP1cbC-0y9jEtLmrsuktEG1M7PgSoOk).

## Prerequisiti
### Latex
È necessario installare una [distribuzione Latex](https://www.latex-project.org/get/) prima di poter compilare i documenti. Per esempio, su Windows (🤢), usando [Chocolatey](https://chocolatey.org/install#individual):
```sh
choco install miktex.install
```

### Wizard
Per generare documenti a partire da alcuni template predefiniti, si può usare lo script [wizard.py](wizard.py). È necessario avere [Python](https://wiki.python.org/moin/BeginnersGuide/Download) installato.

Per installare le dipendenze:
```sh
pip install -r requirements.txt
```
Per eseguire lo script:
```sh
python wizard.py
```
In alternativa allo script, si possono creare nuovi documenti prendendo spunto da quelli già esistenti.

## Struttura
| Cartella                | Contenuto                      |
|-------------------------|--------------------------------|
| [~~docs~~](docs/)           | ~~Documenti in formato *PDF*~~ (la cartella e il contenuto vengono mantenuti solo per retrocompatibilità)  |
| [src](src/)             | Sorgenti dei documenti *Latex*, con suddivisione fra [interni](src/Interni/) ed [esterni](src/Esterni/) |
| [templates](templates/) | Sorgenti dei template *Latex*  |

## Workflow consigliato
- Creare un branch specifico per il documento che si vuole creare. Nel caso dei verbali, ad esempio, è già disponibile il branch *verbali*.
- Creare il documento nella cartella [src](src/), con il *wizard* sopra menzionato oppure manualmente. Nel caso di documenti complessi, se non si utilizza il *wizard*, che necessitano di una cartella a sè, ricordarsi di creare all'interno della cartella i link simbolici alle cartelle [assets](src/assets), [classes](src/classes) e [common](src/common) (se servono). Dentro la cartella del nuovo documento:
    ```sh
    ln -s ../assets assets
    ln -s ../classes classes
    ln -s ../common common
    ```
- Finito di redigere il documento, fare il merge del branch in *master*. Prestare attenzione ad eventuali conflitti, è buona norma fare il pull da *master* di tanto in tanto mentre si lavora al documento. Il documento verrà compilato e caricato nella [cartella condivisa](https://drive.google.com/drive/folders/10DP1cbC-0y9jEtLmrsuktEG1M7PgSoOk) su *Drive*, ci pensa automagicamente il [workflow *build*](.github/workflows/build.yml).

## Strumenti consigliati
- [VSCode](https://code.visualstudio.com/Download)
