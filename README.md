# Taller Mecánico Django

Este repositorio contiene una aplicación Django para gestionar un taller automotriz:

- Registro de vehículos y sus próximas fechas de mantenimiento.  
- Registro de mantenimientos y repuestos asociados.  
- Búsqueda de repuestos por empresa, precio y stock.  

## Requisitos

- Python ≥ 3.10  
- Django 5.2  
- PostgreSQL (recomendado) o SQLite  
- `virtualenv`  

## Instalación

Ejecuta estos comandos **fuera** de cualquier carpeta de proyecto, en el directorio donde quieras clonar:

```bash
git clone https://github.com/AlessandroRG31/taller_mecanico.git
cd taller_mecanico
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
