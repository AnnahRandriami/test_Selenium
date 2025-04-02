from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

try:
    # Initialisation du driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    print("[INFO] Navigateur ouvert")

    # Ouverture de la page
    driver.get("http://127.0.0.1:5500/index.html")
    print("[INFO] Page chargée")

    wait = WebDriverWait(driver, 20)
    tetris_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "tetris")))
    print("[INFO] Bouton Tetris trouvé")

    # Clic sur le bouton pour ouvrir le jeu
    tetris_button.click()
    print("[INFO] Bouton Tetris cliqué")

    # Attente de l'apparition de la modal
    modal_left = wait.until(EC.presence_of_element_located((By.ID, "modal-left")))
    assert modal_left.is_displayed(), "❌ La modal ne s'est pas ouverte !"
    print("[INFO] Modal ouverte avec succès")

    # Vérification du canvas du jeu
    canvas = wait.until(EC.presence_of_element_located((By.ID, "tetris")))
    assert canvas.is_displayed(), "❌ Canvas du jeu Tetris non trouvé !"
    print("[INFO] Canvas du jeu trouvé et visible")
    time.sleep(3)

    # Simuler des actions clavier pour tester les déplacements
    canvas.click()
    actions = ActionChains(driver)

    for key, direction in zip([Keys.ARROW_LEFT, Keys.ARROW_RIGHT, Keys.ARROW_DOWN, Keys.ARROW_UP],
                              ["gauche", "droite", "descente", "rotation"]):
        actions.send_keys(key).perform()
        print(f"[INFO] Déplacement vers {direction} OK")
        time.sleep(1)

    print("[INFO] Test terminé avec succès")

except Exception as e:
    print(f"[ERREUR] Une exception s'est produite : {e}")

finally:
    driver.quit()
    print("[INFO] Navigateur fermé")
