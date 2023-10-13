brands = ["apple", "infinix", "oppo", "realme", "samsung", "vivo", "xiaomi"]

for i in brands:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service
    import time
    import csv

    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")

    service = Service(executable_path = 'C:/Users/marce/Desktop/chromedriver-win64/chromedriver.exe') 

    driver = webdriver.Chrome(service = service, options = options)

    url = f"https://www.arenadigital.id/brand/{i}/"
    
    driver.get(url) 

    driver.find_element(By.CSS_SELECTOR, value = '.re_ajax_pagination .def_btn').click()

    time.sleep(3)

    try:
        driver.find_element(By.CSS_SELECTOR, value = '.re_ajax_pagination .def_btn').click()

        time.sleep(3)
    except:
        print("continue")
    
    try:
        driver.find_element(By.CSS_SELECTOR, value = '.re_ajax_pagination .def_btn').click()

        time.sleep(3)
    except:
        print("continue")

    try:
        driver.find_element(By.CSS_SELECTOR, value = '.re_ajax_pagination .def_btn').click()

        time.sleep(3)
    except:
        print("continue")

    try:
        driver.find_element(By.CSS_SELECTOR, value = '.re_ajax_pagination .def_btn').click()

        time.sleep(3)
    except:
        print("continue")


    csvfile = open(f"{i}.csv", 'w', newline='', encoding='utf-8')
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Name', 'Price', 'Brand', 'Chipset', 'CPU', 'GPU', 'RAM', 'Weight', 'Storage', 'Screen Type', 'Screen Size', 'Resolution', 'Pixel Density', 'Total camera', 'Battery Capacity'])

    all_phones = driver.find_elements(by = By.XPATH, value = '//div[@class="product col_item offer_grid woo_compact_grid rehub-sec-smooth mobile_compact_grid offer_act_enabled no_btn_enabled type-product  "]')
    
    for phone in all_phones:
        name = phone.find_element(by = By.XPATH, value = './/h3/a').text
        links = phone.find_element(by = By.XPATH, value = './/h3/a').get_attribute("href")
        print(name)

        driver.get(links)

        time.sleep(1)

        price = driver.find_element(by = By.CSS_SELECTOR, value = '#section-additional_information > div.rh-tabletext-block-wrapper.padd20 > table > tbody > tr.attribute_row.attribute_row_umum > td > table > tbody > tr.woocommerce-product-attributes-item.woocommerce-product-attributes-item--attribute_pa_harga-rilis > td > p').text
    
        brand = f"{i}"
    
        chipset = driver.find_element(by = By.CSS_SELECTOR, value = '#section-additional_information > div.rh-tabletext-block-wrapper.padd20 > table > tbody > tr.attribute_row.attribute_row_platform > td > table > tbody > tr.woocommerce-product-attributes-item.woocommerce-product-attributes-item--attribute_pa_prosesor > td > p > a').text
    
        CPU = driver.find_element(by = By.CSS_SELECTOR, value = '#section-additional_information > div.rh-tabletext-block-wrapper.padd20 > table > tbody > tr.attribute_row.attribute_row_platform > td > table > tbody > tr.woocommerce-product-attributes-item.woocommerce-product-attributes-item--attribute_pa_cpu > td > p').text
    
        GPU = driver.find_element(by = By.CSS_SELECTOR, value = '#section-additional_information > div.rh-tabletext-block-wrapper.padd20 > table > tbody > tr.attribute_row.attribute_row_platform > td > table > tbody > tr.woocommerce-product-attributes-item.woocommerce-product-attributes-item--attribute_pa_gpu > td > p').text
    
        RAM = driver.find_element(by = By.CSS_SELECTOR, value = '#section-additional_information > div.rh-tabletext-block-wrapper.padd20 > table > tbody > tr.attribute_row.attribute_row_memori > td > table > tbody > tr.woocommerce-product-attributes-item.woocommerce-product-attributes-item--attribute_pa_ram > td > p > a').text
 
        try:
            weight = driver.find_element(by = By.CSS_SELECTOR, value = '#section-additional_information > div.rh-tabletext-block-wrapper.padd20 > table > tbody > tr.attribute_row.attribute_row_bodi > td > table > tbody > tr.woocommerce-product-attributes-item.woocommerce-product-attributes-item--attribute_pa_berat > td > p').text
        except:
            weight = '0 gram'
    
        storage = driver.find_element(by = By.CSS_SELECTOR, value = '#section-additional_information > div.rh-tabletext-block-wrapper.padd20 > table > tbody > tr.attribute_row.attribute_row_memori > td > table > tbody > tr.woocommerce-product-attributes-item.woocommerce-product-attributes-item--attribute_pa_internal > td > p').text
    
        tipe_layar = driver.find_element(by = By.CSS_SELECTOR, value = '#section-additional_information > div.rh-tabletext-block-wrapper.padd20 > table > tbody > tr.attribute_row.attribute_row_layar > td > table > tbody > tr.woocommerce-product-attributes-item.woocommerce-product-attributes-item--attribute_pa_tipe-layar > td > p').text

        ukuran_layar = driver.find_element(by = By.CSS_SELECTOR, value = '#section-additional_information > div.rh-tabletext-block-wrapper.padd20 > table > tbody > tr.attribute_row.attribute_row_layar > td > table > tbody > tr.woocommerce-product-attributes-item.woocommerce-product-attributes-item--attribute_pa_layar > td > p > a').text

        resolusi = driver.find_element(by = By.CSS_SELECTOR, value = '#section-additional_information > div.rh-tabletext-block-wrapper.padd20 > table > tbody > tr.attribute_row.attribute_row_layar > td > table > tbody > tr.woocommerce-product-attributes-item.woocommerce-product-attributes-item--attribute_pa_resolusi > td > p').text
    
        try:
            kerapatan_pixel = driver.find_element(by = By.CSS_SELECTOR, value = '#section-additional_information > div.rh-tabletext-block-wrapper.padd20 > table > tbody > tr.attribute_row.attribute_row_layar > td > table > tbody > tr.woocommerce-product-attributes-item.woocommerce-product-attributes-item--attribute_pa_ppi > td > p').text
    
        except:
            kerapatan_pixel = '0'
    
        total_kamera = driver.find_element(by = By.CSS_SELECTOR, value = '#section-additional_information > div.rh-tabletext-block-wrapper.padd20 > table > tbody > tr.attribute_row.attribute_row_kamera-belakang > td > table > tbody > tr.woocommerce-product-attributes-item.woocommerce-product-attributes-item--attribute_pa_jumlah-kamera-belakang > td > p').text

        kapasitas_baterai = driver.find_element(by = By.CSS_SELECTOR, value = '#section-additional_information > div.rh-tabletext-block-wrapper.padd20 > table > tbody > tr.attribute_row.attribute_row_baterai > td > table > tbody > tr.woocommerce-product-attributes-item.woocommerce-product-attributes-item--attribute_pa_baterai > td > p > a').text

        print(price)
        print(brand)
        print(chipset)
        print(CPU)
        print(GPU)
        print(RAM)
        print(weight)
        print(storage)
        print(tipe_layar)
        print(ukuran_layar)
        print(resolusi)
        print(kerapatan_pixel)
        print(total_kamera)
        print(kapasitas_baterai)

        csvwriter.writerow([name, price, brand, chipset, CPU, GPU, RAM, weight, storage, tipe_layar, ukuran_layar, resolusi, kerapatan_pixel,total_kamera, kapasitas_baterai])

        driver.back()

        time.sleep(1)

    driver.quit()
    csvfile.close()
