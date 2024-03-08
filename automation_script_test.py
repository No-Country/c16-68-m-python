import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.common.keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=chrome_options)


@pytest.fixture(scope="module")
def driver():
    with webdriver.Chrome() as driver:
        yield driver



# Prueba 01: Verificar que la página inicial se carga correctamente
@pytest.mark.smoke
def test_01_urbanroutes_flow(driver):
    driver.get("BASE_URL")
    assert "Urban Routes" in driver.title

# Prueba 02: Escribir la dirección "East 2nd Street, 601" en el campo "Desde"
@pytest.mark.smoke
def test_02_set_from_address(driver):
    from_input = driver.find_element(By.ID, "from")
    from_input.clear()
    from_input.send_keys("East 2nd Street, 601")
    assert from_input.get_attribute("value") == "East 2nd Street, 601"

# Prueba 03: Escribir la dirección "1300 1st St" en el campo "Hasta"
@pytest.mark.smoke
def test_03_set_to_address(driver):
    to_input = driver.find_element(By.ID, "to")
    to_input.clear()
    to_input.send_keys("1300 1st St")
    assert to_input.get_attribute("value") == "1300 1st St"

# Prueba 04. Hacer click en el botón "Pedir un taxi"
@pytest.mark.smoke
def test_04_click_request_taxi(driver):
    request_taxi_button = driver.find_element(By.XPATH, "//button[text()='Pedir un taxi']")
    request_taxi_button.click()
    assert "Tariff Selection" in driver.page_source

# Prueba 05: Seleccionar la categoría "Comfort"
@pytest.mark.smoke
def test_05_select_category(driver):
    comfort_category = driver.find_element(By.XPATH, "//div[text()='Comfort']")
    comfort_category.click()
    assert "Comfort" in comfort_category.text

# Prueba 06: Hacer click en el campo "Número de teléfono"
@pytest.mark.smoke
def test_06_click_phone_field(driver):
    phone_field = driver.find_element(By.XPATH, "//div[text()='Número de teléfono']")
    phone_field.click()
    assert "Número de teléfono" in driver.page_source

# Prueba 07: Introducir un número válido en el campo "Número de teléfono"
@pytest.mark.smoke
def test_07_enter_phone_number(driver):
    phone_input = driver.find_element(By.ID, "phone")
    phone_input.clear()
    phone_input.send_keys("+12312312312")
    assert phone_input.get_attribute("value") == "+12312312312"

# Prueba 08: Hacer click en el botón "Siguiente"
@pytest.mark.smoke
def test_08_click_next_button(driver):
    next_button = driver.find_element(By.XPATH, "//button[text()='Siguiente']")
    next_button.click()
    assert "Next Page" in driver.title

# Prueba 09: Abrir devtools en Chrome
@pytest.mark.smoke
def test_09_find_tab(driver):
    driver.get("chrome://devtools")
    assert "chrome://devtools" in driver.current_url

# Prueba 010: Hacer click en la pestaña "Network"
@pytest.mark.smoke
def test_010_select_tab(driver):
    network_tab = driver.find_element(By.XPATH, "//div[@class='tab'][text()='Network']")
    network_tab.click()
    assert network_tab.is_selected()

# Prueba 014: Esperar a que las solicitudes en la pestaña "Network" estén completamente cargada
@pytest.mark.smoke
def test_014_webdriverwait(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@class='name']/div"))
    )
    assert len(driver.find_elements(By.XPATH, "//div[@class='name']/div")) > 0

# Prueba 015: Encontrar y hacer click en el último enlace de la columna "Name" en la pestaña "Network"
@pytest.mark.smoke
def test_015_find_and_select_link(driver):
    network_links = driver.find_elements(By.XPATH, "//div[@class='name']/div")
    last_link = network_links[-1]  # Último enlace
    last_link.click()
    assert last_link.is_selected()

# Prueba 016: Esperar a que aparezca el código en la pestaña "Preview"
@pytest.mark.smoke
def test_016_webdriverwait(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='preview']/div"))
    )
    assert driver.find_element(By.XPATH, "//div[@class='preview']/div").is_displayed()

# Prueba 017: Copiar el código de la pestaña "Preview"
@pytest.mark.smoke
def test_017_copy_number(driver):
    code_element = driver.find_element(By.XPATH, "//div[@class='preview']/div")
    verification_code = code_element.text
    assert verification_code != ""

# Prueba 018: Encontrar el campo para ingresar el código SMS y pegar el código
@pytest.mark.smoke
def test_018_enter_number(driver):
    sms_input = driver.find_element(By.ID, "codigo_sms")
    sms_input.clear()
    sms_input.send_keys(verification_code)
    assert sms_input.get_attribute("value") == verification_code

# Prueba 019: Hacer click en el botón "Confirmar"
@pytest.mark.smoke
def test_019_select_button(driver):
    confirm_button = driver.find_element(By.XPATH, "//button[text()='Confirmar']")
    confirm_button.click()
    assert confirm_button.is_displayed()

# Prueba 020: Hacer click en el campo "Forma de pago" en la flecha derecha
@pytest.mark.smoke
def test_020_select_arrow(driver):
    payment_arrow = driver.find_element(By.XPATH, "//img[@alt='Arrow right']")
    payment_arrow.click()
    assert payment_arrow.is_displayed()

# Prueba 021: Hacer click en "Agregar una tarjeta"
@pytest.mark.smoke
def test_021_add_card(driver):
    add_card = driver.find_element(By.XPATH, "//div[text()='Agregar una tarjeta']")
    add_card.click()
    assert add_card.is_displayed()

# Prueba 022: Escribir el número de tarjeta y su código de verificación
@pytest.mark.smoke
def test_022_enter_number(driver):
    card_number_input = driver.find_element(By.ID, "number")
    card_number_input.clear()
    card_number_input.send_keys("1234 0000 4321 1234")
    assert card_number_input.get_attribute("value") == "1234 0000 4321 1234"

# Prueba 023: Escribir el código de verificación de la tarjeta
@pytest.mark.smoke
def test_023_enter_number(driver):
    code_input = driver.find_element(By.ID, "code")
    code_input.clear()
    code_input.send_keys("12")
    assert code_input.get_attribute("value") == "12"

# Prueba 024. Hacer click (parte blanca) fuera del cuadro principal para activar el botón "Enlace"
@pytest.mark.smoke
def test_024_select_overlay(driver):
    overlay = driver.find_element(By.CLASS_NAME, "overlay")
    overlay.click()
    assert overlay.is_enabled()

# Prueba 025: Hacer click en el botón "Enlace"
@pytest.mark.smoke
def test_025_select_link(driver):
    enlace_button = driver.find_element(By.XPATH, "//button[text()='Enlace']")
    enlace_button.click()
    assert enlace_button.is_displayed()

# Prueba 026: Hacer click en el botón cerrar ventana
@pytest.mark.smoke
def test_026_select_button(driver):
    close_button = driver.find_element(By.CLASS_NAME, "close-button")
    close_button.click()
    assert close_button.is_displayed()

# Prueba 027: Agregar comentario para el conductor
@pytest.mark.smoke
def test_027_add_text(driver):
    omment_input = driver.find_element(By.ID, "comment")
    comment_input.clear()
    comment_input.send_keys("Traer los snacks")
    assert comment_input.get_attribute("value") == "Traer los snacks"

# Prueba 028: Activar el botón "mantas y pañuelos"
@pytest.mark.smoke
def test_028_select_button(driver):
    blankets_button = driver.find_element(By.CLASS_NAME, "slider")
    blankets_button.click()
    assert blankets_button.is_selected()

# Prueba 029: Agregar 2 helados
@pytest.mark.smoke
def test_029_select_button(driver):
    ice_cream_button = driver.find_element(By.CLASS_NAME, "counter-plus")
    ice_cream_button.click()
    ice_cream_button.click()
    assert "counter-plus" in driver.page_source

# Prueba 030: Hacer click en el botón "Pedir un taxi"
@pytest.mark.smoke
def test_030_select_button(driver):
    request_taxi_button_2 = driver.find_element(By.CLASS_NAME, "smart-button-main")
    request_taxi_button_2.click()
    assert request_taxi_button_2.is_displayed()

# Prueba 031: Esperar a que aparezca la figura de "Bender"
@pytest.mark.smoke
def test_031_webdriverwait(driver):
    bender_image = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//img[@alt='close']"))
    )
    assert bender_image.is_displayed()

# Esperar 5 segundos y cerrar la página
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.common.keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=chrome_options)


@pytest.fixture(scope="module")
def driver():
    with webdriver.Chrome() as driver:
        yield driver



# Prueba 01: Verificar que la página inicial se carga correctamente
@pytest.mark.smoke
def test_01_urbanroutes_flow(driver):
    driver.get("BASE_URL")
    assert "Urban Routes" in driver.title

# Prueba 02: Escribir la dirección "East 2nd Street, 601" en el campo "Desde"
@pytest.mark.smoke
def test_02_set_from_address(driver):
    from_input = driver.find_element(By.ID, "from")
    from_input.clear()
    from_input.send_keys("East 2nd Street, 601")
    assert from_input.get_attribute("value") == "East 2nd Street, 601"

# Prueba 03: Escribir la dirección "1300 1st St" en el campo "Hasta"
@pytest.mark.smoke
def test_03_set_to_address(driver):
    to_input = driver.find_element(By.ID, "to")
    to_input.clear()
    to_input.send_keys("1300 1st St")
    assert to_input.get_attribute("value") == "1300 1st St"

# Prueba 04. Hacer click en el botón "Pedir un taxi"
@pytest.mark.smoke
def test_04_click_request_taxi(driver):
    request_taxi_button = driver.find_element(By.XPATH, "//button[text()='Pedir un taxi']")
    request_taxi_button.click()
    assert "Tariff Selection" in driver.page_source

# Prueba 05: Seleccionar la categoría "Comfort"
@pytest.mark.smoke
def test_05_select_category(driver):
    comfort_category = driver.find_element(By.XPATH, "//div[text()='Comfort']")
    comfort_category.click()
    assert "Comfort" in comfort_category.text

# Prueba 06: Hacer click en el campo "Número de teléfono"
@pytest.mark.smoke
def test_06_click_phone_field(driver):
    phone_field = driver.find_element(By.XPATH, "//div[text()='Número de teléfono']")
    phone_field.click()
    assert "Número de teléfono" in driver.page_source

# Prueba 07: Introducir un número válido en el campo "Número de teléfono"
@pytest.mark.smoke
def test_07_enter_phone_number(driver):
    phone_input = driver.find_element(By.ID, "phone")
    phone_input.clear()
    phone_input.send_keys("+12312312312")
    assert phone_input.get_attribute("value") == "+12312312312"

# Prueba 08: Hacer click en el botón "Siguiente"
@pytest.mark.smoke
def test_08_click_next_button(driver):
    next_button = driver.find_element(By.XPATH, "//button[text()='Siguiente']")
    next_button.click()
    assert "Next Page" in driver.title

# Prueba 09: Abrir devtools en Chrome
@pytest.mark.smoke
def test_09_find_tab(driver):
    driver.get("chrome://devtools")
    assert "chrome://devtools" in driver.current_url

# Prueba 010: Hacer click en la pestaña "Network"
@pytest.mark.smoke
def test_010_select_tab(driver):
    network_tab = driver.find_element(By.XPATH, "//div[@class='tab'][text()='Network']")
    network_tab.click()
    assert network_tab.is_selected()

# Prueba 014: Esperar a que las solicitudes en la pestaña "Network" estén completamente cargada
@pytest.mark.smoke
def test_014_webdriverwait(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@class='name']/div"))
    )
    assert len(driver.find_elements(By.XPATH, "//div[@class='name']/div")) > 0

# Prueba 015: Encontrar y hacer click en el último enlace de la columna "Name" en la pestaña "Network"
@pytest.mark.smoke
def test_015_find_and_select_link(driver):
    network_links = driver.find_elements(By.XPATH, "//div[@class='name']/div")
    last_link = network_links[-1]  # Último enlace
    last_link.click()
    assert last_link.is_selected()

# Prueba 016: Esperar a que aparezca el código en la pestaña "Preview"
@pytest.mark.smoke
def test_016_webdriverwait(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='preview']/div"))
    )
    assert driver.find_element(By.XPATH, "//div[@class='preview']/div").is_displayed()

# Prueba 017: Copiar el código de la pestaña "Preview"
@pytest.mark.smoke
def test_017_copy_number(driver):
    code_element = driver.find_element(By.XPATH, "//div[@class='preview']/div")
    verification_code = code_element.text
    assert verification_code != ""

# Prueba 018: Encontrar el campo para ingresar el código SMS y pegar el código
@pytest.mark.smoke
def test_018_enter_number(driver):
    sms_input = driver.find_element(By.ID, "codigo_sms")
    sms_input.clear()
    sms_input.send_keys(verification_code)
    assert sms_input.get_attribute("value") == verification_code

# Prueba 019: Hacer click en el botón "Confirmar"
@pytest.mark.smoke
def test_019_select_button(driver):
    confirm_button = driver.find_element(By.XPATH, "//button[text()='Confirmar']")
    confirm_button.click()
    assert confirm_button.is_displayed()

# Prueba 020: Hacer click en el campo "Forma de pago" en la flecha derecha
@pytest.mark.smoke
def test_020_select_arrow(driver):
    payment_arrow = driver.find_element(By.XPATH, "//img[@alt='Arrow right']")
    payment_arrow.click()
    assert payment_arrow.is_displayed()

# Prueba 021: Hacer click en "Agregar una tarjeta"
@pytest.mark.smoke
def test_021_add_card(driver):
    add_card = driver.find_element(By.XPATH, "//div[text()='Agregar una tarjeta']")
    add_card.click()
    assert add_card.is_displayed()

# Prueba 022: Escribir el número de tarjeta y su código de verificación
@pytest.mark.smoke
def test_022_enter_number(driver):
    card_number_input = driver.find_element(By.ID, "number")
    card_number_input.clear()
    card_number_input.send_keys("1234 0000 4321 1234")
    assert card_number_input.get_attribute("value") == "1234 0000 4321 1234"

# Prueba 023: Escribir el código de verificación de la tarjeta
@pytest.mark.smoke
def test_023_enter_number(driver):
    code_input = driver.find_element(By.ID, "code")
    code_input.clear()
    code_input.send_keys("12")
    assert code_input.get_attribute("value") == "12"

# Prueba 024. Hacer click (parte blanca) fuera del cuadro principal para activar el botón "Enlace"
@pytest.mark.smoke
def test_024_select_overlay(driver):
    overlay = driver.find_element(By.CLASS_NAME, "overlay")
    overlay.click()
    assert overlay.is_enabled()

# Prueba 025: Hacer click en el botón "Enlace"
@pytest.mark.smoke
def test_025_select_link(driver):
    enlace_button = driver.find_element(By.XPATH, "//button[text()='Enlace']")
    enlace_button.click()
    assert enlace_button.is_displayed()

# Prueba 026: Hacer click en el botón cerrar ventana
@pytest.mark.smoke
def test_026_select_button(driver):
    close_button = driver.find_element(By.CLASS_NAME, "close-button")
    close_button.click()
    assert close_button.is_displayed()

# Prueba 027: Agregar comentario para el conductor
@pytest.mark.smoke
def test_027_add_text(driver):
    omment_input = driver.find_element(By.ID, "comment")
    comment_input.clear()
    comment_input.send_keys("Traer los snacks")
    assert comment_input.get_attribute("value") == "Traer los snacks"

# Prueba 028: Activar el botón "mantas y pañuelos"
@pytest.mark.smoke
def test_028_select_button(driver):
    blankets_button = driver.find_element(By.CLASS_NAME, "slider")
    blankets_button.click()
    assert blankets_button.is_selected()

# Prueba 029: Agregar 2 helados
@pytest.mark.smoke
def test_029_select_button(driver):
    ice_cream_button = driver.find_element(By.CLASS_NAME, "counter-plus")
    ice_cream_button.click()
    ice_cream_button.click()
    assert "counter-plus" in driver.page_source

# Prueba 030: Hacer click en el botón "Pedir un taxi"
@pytest.mark.smoke
def test_030_select_button(driver):
    request_taxi_button_2 = driver.find_element(By.CLASS_NAME, "smart-button-main")
    request_taxi_button_2.click()
    assert request_taxi_button_2.is_displayed()

# Prueba 031: Esperar a que aparezca la figura de "Bender"
@pytest.mark.smoke
def test_031_webdriverwait(driver):
    bender_image = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//img[@alt='close']"))
    )
    assert bender_image.is_displayed()

# Esperar 5 segundos y cerrar la página
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
