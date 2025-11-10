import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_homepage(driverFixture):

    # Pesquisar tomate
    wait = WebDriverWait(driverFixture, 10)
    campo_pesquisa = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='search']")))
    campo_pesquisa.send_keys("Tomato")

    # Espera até o tomate aparecer
    Produto_nome_locator = (By.XPATH, "//h4[contains(.,'Tomato - 1 Kg')]")
    elemento_visivel= wait.until(EC.visibility_of_element_located(Produto_nome_locator))
    assert "Tomato" in elemento_visivel.text, "produto não encontrado!"

    

    # Espera até o botão incrementar estar clicavel
    incrementar = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".increment")))
    incrementar.click()
    # Encontra o campo quantidade após o incremento
    quantidade_produto = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='number']")))
    quantidade_atual = quantidade_produto.get_attribute("value")

    assert int(quantidade_atual) == 2, f"O valor esperado era 2, mas foi igual a {quantidade_atual}"
    print(f"A quantidade do produto é :{quantidade_atual}")

    # Adiciona o produto no carrinho
    driverFixture.find_element(By.XPATH, "//button[text()='ADD TO CART']").click()

   
