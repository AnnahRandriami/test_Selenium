from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialisation du driver
driver = webdriver.Chrome()

# Ouverture de la page
driver.get("http://127.0.0.1:5500/index.html") 

driver.maximize_window() 
time.sleep(3)

# Attente que l'élément "calcul" (bouton ou modal) soit visible
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "calcul")))
print("✅ Bouton estimation de test trouvé")

# Attendre que le bouton pour démarrer l'estimation soit visible et cliquable
estimation_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "calcul")))
print("✅ Bouton estimation de rapport de test cliqué")

estimation_button.click()
print("✅ Le bouton pour ouvrir l'estimation a été cliqué")

# Choisir estimation par ratio
dropdown = Select(driver.find_element(By.ID, "method"))
dropdown.select_by_value("ratio")
time.sleep(3)
print("✅ L'option ratio a été sélectionnée")

# Remplir les cases avec des valeurs valides
champ_dev = driver.find_element(By.ID, "dev_effort")
champ_dev.send_keys("10")
champ_test = driver.find_element(By.ID, "test_effort")
champ_test.send_keys("15")
champ_currentEffort = driver.find_element(By.ID, "current_dev_effort")
champ_currentEffort.send_keys(12)

# Calculer le ratio
ratio_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@onclick='calculateRatio()']"))
    )
ratio_button.click()
print("✅ Bouton cliqué avec succès !")

# Calculer de l'effort du projet actuel
current_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@onclick='calculateTestEffortForCurrentProject()']"))
    )
current_button.click()
print("✅ Bouton cliqué avec succès !")

# Attendre l'affichage du résultat
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "result")))

# Afficher le résultat
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
result_element = driver.find_element(By.ID, "result")
result_text = result_element.text
print("📢 Résultat affiché sur la page :", result_text)

# Insérer des valeurs incorrectes
champ_dev.clear()
champ_dev.send_keys("-10") 
champ_test.clear()
champ_test.send_keys("tetete") 
champ_currentEffort.clear()
champ_test.send_keys("100000") 


# Calculer le ratio avec des valeurs incorrectes
ratio_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@onclick='calculateRatio()']"))
    )
ratio_button.click()
print("✅ Bouton cliqué avec succès !")

# Calculer de l'effort du projet actuel
current_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@onclick='calculateTestEffortForCurrentProject()']"))
    )
current_button.click()
print("✅ Bouton cliqué avec succès !")

# Attendre l'affichage du résultat pour les valeurs incorrectes
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "result")))

# Afficher le résultat
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
result_element = driver.find_element(By.ID, "result")
result_text = result_element.text
print("📢 Résultat affiché sur la page :", result_text)

# Cellule vide
champ_dev.clear()
champ_test.clear()
champ_currentEffort.clear()
# Calculer le ratio avec des valeurs incorrectes

ratio_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@onclick='calculateRatio()']"))
    )
ratio_button.click()
print("✅ Bouton cliqué avec succès !")

# Calculer de l'effort du projet actuel
current_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@onclick='calculateTestEffortForCurrentProject()']"))
    )
current_button.click()
print("✅ Bouton cliqué avec succès !")
# Attendre l'affichage du résultat pour les valeurs incorrectes
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "result")))

# Afficher le résultat
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
result_element = driver.find_element(By.ID, "result")
result_text = result_element.text
print("📢 Résultat affiché sur la page :", result_text)
# Fermer le navigateur


driver.quit()
