from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def init_driver():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5500/index.html")
    driver.maximize_window()
    return driver, WebDriverWait(driver, 10)

def click_element(wait, by, value, info):
    try:
        element = wait.until(EC.element_to_be_clickable((by, value)))
        element.click()
        print(f"[INFO] {info}")
    except Exception as e:
        print(f"[ERREUR] Impossible de cliquer sur {info} - {str(e)}")

def fill_input(driver, element_id, value):
    try:
        field = driver.find_element(By.ID, element_id)
        field.clear()
        field.send_keys(value)
    except Exception as e:
        print(f"[ERREUR] Impossible de remplir {element_id} - {str(e)}")

def process_estimation(driver, wait, dev_effort, test_effort, current_dev_effort):
    fill_input(driver, "dev_effort", dev_effort)
    fill_input(driver, "test_effort", test_effort)

    click_element(wait, By.XPATH, "//button[@onclick='calculateRatio()']", "Calcul de ratio effectué")

    try:
        wait.until(EC.presence_of_element_located((By.ID, "result")))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        result_ratio = driver.find_element(By.ID, "result").text.strip()
        if result_ratio:
            print(f"[RESULTAT] Ratio calculé : {result_ratio}")
        else:
            print("[INFO] Aucun ratio affiché.")
    except Exception as e:
        print(f"[ERREUR] Échec du chargement du ratio - {str(e)}")
        return  # Arrête l'exécution si le ratio ne peut pas être calculé

    fill_input(driver, "current_dev_effort", current_dev_effort)
    click_element(wait, By.XPATH, "//button[@onclick='calculateTestEffortForCurrentProject()']", "Calcul de l'effort de test effectué")

    try:
        wait.until(EC.presence_of_element_located((By.ID, "current_test_effort_result")))
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        result_effort = driver.find_element(By.ID, "current_test_effort_result").text.strip()
        if result_effort:  # Vérifie si la valeur n'est pas vide
            print(f"[RESULTAT] Effort de test calculé : {result_effort}")
    except Exception as e:
        print(f"[ERREUR] Échec du chargement de l'effort de test - {str(e)}")

driver, wait = init_driver()
click_element(wait, By.CLASS_NAME, "calcul", "Bouton estimation de test")
Select(driver.find_element(By.ID, "method")).select_by_value("ratio")
print("[INFO] L'option estimation par ratio a été sélectionnée")
time.sleep(3)

# Tests avec différentes entrées
scenarios = [
    ("10", "15", "12"),  # valeurs valides
    ("-10", "tetete", "100000"),  # valeurs invalides
    ("", "", "")  # cellules vides
]

for dev, test, current in scenarios:
    process_estimation(driver, wait, dev, test, current)

driver.quit()
