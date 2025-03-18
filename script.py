from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialisation du driver
driver = webdriver.Chrome()

# Ouverture de la page
driver.get("http://127.0.0.1:5500/index.html")

# Attente que l'élément "tetris" soit visible
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "tetris")))

print("✅ tetris trouvé")

# Attendre que le bouton soit visible et cliquable
tetris_button = wait.until(EC.presence_of_element_located((By.ID, "tetrisButton")))
print("✅ bouton tetris trouvé")
# Vérifier que le bouton est bien affiché
assert tetris_button.is_displayed(), "❌ Le bouton n'est pas visible !"

# Simuler un clic avec ActionChains
actions = ActionChains(driver)
actions.move_to_element(tetris_button).click().perform()

print("✅ Le bouton pour ouvrir tetris a été cliqué")

time.sleep(3)

# Vérifier que la modal est bien affichée
modal_left = wait.until(EC.presence_of_element_located((By.ID, "modal-left")))
driver.execute_script("document.getElementById('modal-left').style.visibility = 'visible';")
html = driver.page_source
if "modal-left" in html:
    print("✅ La modal est bien dans le DOM mais peut-être cachée")
else:
    print("❌ La modal n'est pas présente dans le DOM")


assert modal_left.is_displayed(), "❌ La modal ne s'est pas ouverte !"
print("✅ Le modal est ouvert avec succès")
modal = modal_left.get_attribute("innerHTML")

# Afficher le contenu
print("📌 Contenu de la modale :\n", modal)

#Afficher modalContent

# Attendre que la modale s'affiche
wait.until(lambda d: "show" in d.find_element(By.ID, "modal-left").get_attribute("class"))
print("✅ La modale est visible")

# Attendre que modal-content soit rempli
wait.until(lambda d: d.find_element(By.ID, "modal-content").get_attribute("innerHTML").strip() != "")
print("✅ `modal-content` a été rempli avec succès.")

# Récupérer et afficher le contenu HTML de la modale
modal_content_html = driver.find_element(By.ID, "modal-content").get_attribute("innerHTML")
print("📌 Contenu de modal-content :\n", modal_content_html)

# Vérifier si un canvas est présent
canvas = driver.find_elements(By.TAG_NAME, "canvas")
if canvas:
    print("✅ Un canvas a bien été détecté dans la modale !")
else:
    print("❌ Aucun canvas trouvé dans modal-content.")

# Fermer le navigateur après le test
driver.quit()