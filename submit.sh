#!/bin/bash

## Nombre del trabajo
#SBATCH --job-name=MinimaHop
## Archivo de salida
#SBATCH --output=../ExpResults/MinimaHop.txt
### Partición (Cola de trabajo)
##SBATCH --partition=512x1024
## Solicitud de cpus
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
## Solicitud de memoria RAM en GB
#SBATCH --mail-user=econtreraslazcano@uc.cl
#SBATCH --mail-type=ALL

python main.py
