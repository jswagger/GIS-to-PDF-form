from unittest import TestCase
from mock import patch, MagicMock
import gis_to_pdf_form
import arcpy

class TestGisToPDF(TestCase):
  @patch('arcpy.ListFields')
  def test_getting_domain_fields(self, mock_list):
    fake_layer = self.get_fake_layer()
    mock_list.return_value = fake_layer['fields']
    fake_domains = gis_to_pdf_form.get_domain_fields(fake_layer)
    expected_domain_list = []
    self.assertEqual(fake_domains, expected_domain_list)
    
   @static
   def get_fake_layer():
      layer = MagicMock()
      layer.fields = [
        
      ]
      return layer
    
  
  
