from rest_framework.test import APITestCase
from products.models import Product
from inventories.models import Inventory


class ProductViewTest(APITestCase):


    


    def test__response_of_product_view_should_be_success(self):

        self.client.post('/api/signup/', {
            "username": "jaja",
            "password": "jaja",
            "is_superuser": False,
            "is_staff": True
            }, format='json')

     
        token = self.client.post('/api/login/' , { 
            "username": "jaja",
            "password": "jaja",
        },  format='json').json()["token"]

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        payload = {    
        "name": "chocolate",
        "price": 4.5,
        "description": "chocolate Laka",
        "category": "doce",
        "image":"image.png",
        "amount": 10
        }

        expected = {
        "id": 1,
        "name": "chocolate",
        "price": "4.5",
        "description": "chocolate Laka",
        "category": "doce",
        "image":"image.png",
        "amount": "10"
        }

        response = self.client.post('/api/products/register', payload)
        print(response)
        self.assertEquals(response.data, expected)
        self.assertEquals(response.status_code, 201)

    def test__response_of_product_view_should_be_failed(self):
        payload = {    
        "name": "chocolate",
        "price": 5,
        "description": "chocolate Laka",
        "category": "doce",
         "image":"image.png",
        "amount": 10
        }

        expected = {
            'data': {
                'message': 'Não foi possível criar o produto, tente novamente', 
                'error_code': 400
            }
        }

        response = self.client.post('/api/products/register', payload)
        print(response)
        #self.assertEquals(response.data, expected)
        #self.assertEquals(response.status_code, 400)