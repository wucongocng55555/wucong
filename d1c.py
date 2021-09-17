class lei():
    def __init__(self, driver):
        self.driver = driver

    def dz(self, dz):#地址
        self.driver.get(dz)

    def dw(self, *dw):#定位元素
        return self.driver.find_element(*dw)
