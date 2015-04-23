import unittest
import Tarea2
from Tarea2 import calcularPrecio
from datetime import datetime

class Test_testTarea2(unittest.TestCase):

    def testZeroTime(self):
        base = datetime(2015, 1, 1)
        tarifa = Tarea2.Tarifa(1, 1)
        tReservacion = [base, datetime(2015, 1, 1)]
        calcularPrecio(tarifa, tReservacion)

    def testMinimumTime(self):
        base = datetime(2015, 1, 1)
        tarifa = Tarea2.Tarifa(1, 1)
        tReservacion = [base, datetime(2015, 1, 1, minute = 16)]
        tReservacionHora = [base, datetime(2015, 1, 1, hour = 1)]
        self.assertEqual(calcularPrecio(tarifa, tReservacion), calcularPrecio(tarifa, tReservacionHora))
        

if __name__ == '__main__':
    unittest.main()
