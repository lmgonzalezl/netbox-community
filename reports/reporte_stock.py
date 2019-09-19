from dcim.constants import *
from dcim.models import Device
from extras.models import CustomFieldValue
from tenancy.models import Tenant
from extras.reports import Report
from ipam.constants import *

#El informe muestra el inventario de stock registrado en tenants específicos
########################
# Objeto: Tenant
# ---------------------
# Id - Tenant
# ---------------------
# 77 - Almacén
# 78 - Taller Pascal
# 76 - Taller Sistemas
#
########################
# Objeto: CustomField
# ---------------------
# field_id - name
# ---------------------
#    9     - Cantidad
########################

class Stock_Almacen(Report):
	description = "Reporte de Stock en Almacén"
	def test_stock_almacen(self):
		for device in Device.objects.filter(tenant_id=77):
			for cfv in CustomFieldValue.objects.filter(obj_id=device.id).filter(field_id=9):
				if cfv.serialized_value == 1:
					self.log_info(
						device, 
						"Cantidad: {}. Serial: {}".format(cfv.serialized_value,device.serial)
					)
				else:
					self.log_info(
						device, 
						"Cantidad: {}.".format(cfv.serialized_value)
					)
class Stock_Taller_Pascal(Report):
	description = "Reporte de Stock en el taller de Pascal"
	def test_stock_pascal(self):
		for device in Device.objects.filter(tenant_id=78):
			for cfv in CustomFieldValue.objects.filter(obj_id=device.id).filter(field_id=9):
				if cfv.serialized_value == 1:
					self.log_info(
						device, 
						"Cantidad: {}. Serial: {}".format(cfv.serialized_value,device.serial)
					)
				else:
					self.log_info(
						device, 
						"Cantidad: {}.".format(cfv.serialized_value)
					)
			
class Stock_Taller_Sistemas(Report):
	description = "Reporte de Stock en el taller de Sistemas"
	def test_stock_taller_sistemas(self):
		for device in Device.objects.filter(tenant_id=76):
			for cfv in CustomFieldValue.objects.filter(obj_id=device.id).filter(field_id=9):
				if cfv.serialized_value == 1:
					self.log_info(
						device, 
						"Cantidad: {}. Serial: {}".format(cfv.serialized_value,device.serial)
					)
				else:
					self.log_info(
						device, 
						"Cantidad: {}.".format(cfv.serialized_value)
					)
