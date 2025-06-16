# Créer une base de données :
 CREATE DATABASE testvault;
 # Créer un utilisateur et accorder des privilèges : 
 CREATE USER 'testvault'@'localhost' IDENTIFIED BY 'vaultpassword';
 GRANT ALL PRIVILEGES ON testvault.* TO 'testvault'@'localhost';
 FLUSH PRIVILEGES;

 # Vérifier la base de données et l'utilisateur : 
 mysql -u testvault -p -D testvault
# Créer une table livre :
CREATE TABLE livre (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titre VARCHAR(255) NOT NULL
);

# Insérer des exemples de données
INSERT INTO livre (titre) VALUES ('Book One'), ('Book Two'), ('Book Three');

# Étape 4 : Créer une application Flask Python pour afficher le contenu d'un tableau
Voir le fichier python 
