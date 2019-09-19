from dcim.constants import *
from dcim.models import Device
from dcim.models import DeviceType
from extras.reports import Report
from dcim.constants import *

#Porcentaje mínimo de articulos en stock
PERCENT_MIN = 10

class Relacion_Stock_Activos(Report):
	description = "Reporte que muestra la relación en términos porcentuales de tipos de dispositivos activos y en stock. Stock mínimo requerido {} %".format(str(PERCENT_MIN))
	def test_reporte(self):
		for device_type in DeviceType.objects.all():
			counter_active = 0
			counter_stock = 0
			
			#Contar todos los dispositivos activos de un tipo
			for device_active in Device.objects.filter(device_type_id=device_type.id).filter(status=DEVICE_STATUS_ACTIVE):
				counter_active += 1
				
			#Contar todos los dispositivos de un tipo registrados con estatus Inventory
			for device_inventory in Device.objects.filter(status=DEVICE_STATUS_INVENTORY).filter(device_type_id=device_type.id):
				counter_stock += 1
				
			#Contar todos los dispositivos de un tipo registrados con estatus Planned
			for device_inventory in Device.objects.filter(status=DEVICE_STATUS_PLANNED).filter(device_type_id=device_type.id):
				counter_stock += 1
			
			if ((counter_active == 0) and (counter_stock == 0)):
				self.log_failure(
					device_type.model,
					"No hay dispositivos activos ni en stock de este artículo"
				)
			elif ((counter_active > 0) and (counter_stock == 0)):
				self.log_failure(
					device_type.model,
					"No hay dispositivos en stock de este artículo y se han encontrado {} activos".format(str(counter_active))
				)
			elif ((counter_active == 0) and (counter_stock > 0)):
				self.log_info(
					device_type.model,
					"No hay dispositivos activos de este modelo. Cantidad en stock: {}".format(str(counter_stock))
				)
			elif (counter_active > counter_stock):
				percent = ((counter_stock * 100)//counter_active)
				if percent > PERCENT_MIN:
					self.log_info(
						device_type.model,
						"Hay un {} % de dispositivos en stock con relación a los activos".format(str(percent))
					)
				else:
					self.log_warning(
						device_type.model,
						"El artículo presenta un stock del {} % en relación a los activos".format(str(percent))
					)
			else:
				self.log_info(
					device_type.model,
					"Dspositivos en Stock: {}. No hay dispositivos activos de este modelo.".format(str(counter_stock))
				)
