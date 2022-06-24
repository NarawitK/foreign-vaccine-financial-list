class HosxpDataset:

    @property
    def immunization_date(self):
        return self.__immunization_date
        
    @property
    def cid(self):
        return self.__cid

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def vaccine_name(self):
        return self.__vaccine_name

    @property
    def dose(self):
        return self.__dose

    @property
    def vaccine_lot_no(self):
        return self.__vaccine_lot_no

    def __init__(self, immunization_date, cid, name, age, vaccine_name, dose, vaccine_lot_no):
        self.__immunization_date = immunization_date
        self.__cid = cid
        self.__name = name
        self.__age = age
        self.__vaccine_name = vaccine_name
        self.__dose = dose
