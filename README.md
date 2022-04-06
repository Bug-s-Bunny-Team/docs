# docs
<p align="center">
    <img src="src/assets/logo.png" alt="Bug's Bunny logo" width="220">
</p>

[![Build Latex documents](https://github.com/Bug-s-Bunny-Team/docs/actions/workflows/build.yml/badge.svg?branch=master)](https://github.com/Bug-s-Bunny-Team/docs/actions/workflows/build.yml)

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
| [docs](docs/)           | Documenti in formato **PDF**   |
| [src](src/)             | Sorgenti dei documenti *Latex* |
| [templates](templates/) | Sorgenti dei template *Latex*  |

## Strumenti consigliati
- [VSCode](https://code.visualstudio.com/Download)
- [TeXstudio](https://www.texstudio.org/#download)
