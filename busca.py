from selenium import webdriver

driver = webdriver.Firefox()

driver.get('http://www.caixa.gov.br/voce/habitacao/imoveis-venda/Paginas/default.aspx')

element = driver.find_element_by_id('ctl00_ctl58_g_0c6d5adc_cb0c_4029_b628_a2a49e120f91_button')

element.click()

estado = driver.find_element_by_css_selector("#cmb_estado [value='SP']").click()