-- scripts/init_mariadb.sql
-- Script para inicializar la base de datos y usuario en MariaDB

-- 1. Crear la base de datos
CREATE DATABASE IF NOT EXISTS taller_mecanico
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_general_ci;

-- 2. Crear el usuario con contraseña
CREATE USER IF NOT EXISTS 'superadmin'@'localhost'
  IDENTIFIED BY '1221';

-- 3. Conceder todos los privilegios sobre la base de datos
GRANT ALL PRIVILEGES ON taller_mecanico.* TO 'superadmin'@'localhost';

-- 4. Aplicar cambios de privilegios
FLUSH PRIVILEGES;
