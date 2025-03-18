from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialisation du driver
driver = webdriver.Chrome()

# Ouverture de la page
driver.get("http://127.0.0.1:5500/index.html")  # Remplacez cette URL par celle de votre page locale ou en ligne

# Attente que l'élément "tetris" (bouton ou modal) soit visible
wait = WebDriverWait(driver, 40)
element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "tetris")))

print("✅ tetris trouvé")

# Attendre que le bouton pour démarrer le jeu soit visible et cliquable
tetris_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "tetris")))
print("✅ bouton tetris trouvé")

# Simuler un clic avec ActionChains pour démarrer le jeu
tetris_button.click()

print("✅ Le bouton pour ouvrir tetris a été cliqué")

# Attendre que la modal du jeu soit visible
modal_left = wait.until(EC.presence_of_element_located((By.ID, "modal-left")))

# Vérifier que la modal est bien dans le DOM et visible
assert modal_left.is_displayed(), "❌ La modal ne s'est pas ouverte !"
print("✅ La modal est ouverte avec succès")

# Attendre que le contenu du jeu (canvas) soit visible dans la modal
canvas = wait.until(EC.presence_of_element_located((By.ID, "tetris")))

assert canvas.is_displayed(), "❌ Canvas du jeu Tetris non trouvé !"
print("✅ Canvas trouvé et visible")


#Attendre que le jeu marche 3 seconde avant de tester
time.sleep(3)

# Simuler des touches du clavier pour déplacer les pièces de Tetris
canvas.click()

actions = ActionChains(driver)

# Simuler la flèche vers la gauche (déplacement vers la gauche)
actions.send_keys(Keys.ARROW_LEFT).perform()
time.sleep(1)  

# Simuler la flèche vers la droite (déplacement vers la droite)
actions.send_keys(Keys.ARROW_RIGHT).perform()
time.sleep(1)

# Simuler la flèche vers le bas (accélérer la descente)
actions.send_keys(Keys.ARROW_DOWN).perform()
time.sleep(1)

# Simuler la flèche vers le haut (rotation de la pièce)
actions.send_keys(Keys.ARROW_UP).perform()
time.sleep(1)

# Attendre un peu pour voir le résultat dans la modal
time.sleep(5)

# Fermer le navigateur après le test
driver.quit()